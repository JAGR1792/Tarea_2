from __future__ import annotations
import graphviz
import importlib
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


@dataclass
class Token:
    tipo: str
    valor: str


@dataclass
class Nodo:
    etiqueta: str
    hijos: List["Nodo"] = field(default_factory=list)


class LexerError(Exception):
    pass


class ParserError(Exception):
    pass


class Lexer:
    def __init__(self, texto: str) -> None:
        self.texto = texto
        self.pos = 0

    # Convierte la cadena en una lista de tokens
    def tokenizar(self) -> List[Token]:
        tokens: List[Token] = []
        while self.pos < len(self.texto):
            caracter = self.texto[self.pos]

            if caracter.isspace():
                self.pos += 1
                continue

            if caracter.isalpha() or caracter == "_":
                inicio = self.pos
                self.pos += 1
                while self.pos < len(self.texto) and (
                    self.texto[self.pos].isalnum() or self.texto[self.pos] == "_"
                ):
                    self.pos += 1
                lexema = self.texto[inicio:self.pos]
                tokens.append(Token("id", lexema))
                continue

            if caracter.isdigit():
                inicio = self.pos
                self.pos += 1
                while self.pos < len(self.texto) and self.texto[self.pos].isdigit():
                    self.pos += 1
                lexema = self.texto[inicio:self.pos]
                tokens.append(Token("num", lexema))
                continue

            if caracter in "+-":
                tokens.append(Token("opsuma", caracter))
                self.pos += 1
                continue

            if caracter in "*/":
                tokens.append(Token("opmul", caracter))
                self.pos += 1
                continue

            if caracter == "(":
                tokens.append(Token("(", caracter))
                self.pos += 1
                continue

            if caracter == ")":
                tokens.append(Token(")", caracter))
                self.pos += 1
                continue

            raise LexerError(f"Caracter no reconocido: {caracter!r} en posicion {self.pos}")

        tokens.append(Token("FIN", "FIN"))
        return tokens


class Parser:
    """Parser recursivo descendente basado en la gramatica LL(1).

    Cada metodo no terminal (E, Ep, T, Tp, F) implementa una produccion.
    El parser tambien construye el arbol sintactico a medida que reconoce la entrada.
    """

    def __init__(self, tokens: List[Token]) -> None:
        self.tokens = tokens
        self.pos = 0

    # Devuelve el token actual sin consumirlo
    def actual(self) -> Token:
        return self.tokens[self.pos]

    # Consume un token del tipo esperado
    def consumir(self, tipo_esperado: str) -> Token:
        token = self.actual()
        if token.tipo != tipo_esperado:
            raise ParserError(
                f"Se esperaba '{tipo_esperado}', pero se encontro '{token.tipo}' ({token.valor})"
            )
        self.pos += 1
        return token

    # Inicia el analisis desde el simbolo inicial
    def parsear(self) -> Nodo:
        """Aplica el simbolo inicial y verifica que se consuma toda la entrada."""
        raiz = Nodo("Programa", [self.E()])
        self.consumir("FIN")
        return raiz

    # E -> T E'
    def E(self) -> Nodo:
        """Reconoce expresiones de suma/resta con menor precedencia que T."""
        return Nodo("E", [self.T(), self.Ep()])

    # E' -> opsuma T E' | epsilon
    def Ep(self) -> Nodo:
        """Reconoce repeticion de (+|-) T. Si no hay opsuma, deriva a epsilon."""
        token_actual = self.actual()
        if token_actual.tipo == "opsuma":
            operador = self.consumir("opsuma")
            return Nodo("E'", [Nodo(f"opsuma({operador.valor})"), self.T(), self.Ep()])
        return Nodo("E'", [Nodo("vacio")])

    # T -> F T'
    def T(self) -> Nodo:
        """Reconoce terminos con multiplicacion/division (mayor precedencia)."""
        return Nodo("T", [self.F(), self.Tp()])

    # T' -> opmul F T' | epsilon
    def Tp(self) -> Nodo:
        """Reconoce repeticion de (*|/) F. Si no hay opmul, deriva a epsilon."""
        token_actual = self.actual()
        if token_actual.tipo == "opmul":
            operador = self.consumir("opmul")
            return Nodo("T'", [Nodo(f"opmul({operador.valor})"), self.F(), self.Tp()])
        return Nodo("T'", [Nodo("vacio")])

    # F -> id | num | ( E )
    def F(self) -> Nodo:
        """Reconoce factores atomicos: identificador, numero o subexpresion entre parentesis."""
        token_actual = self.actual()
        if token_actual.tipo == "id":
            identificador = self.consumir("id")
            return Nodo("F", [Nodo(f"id({identificador.valor})")])
        if token_actual.tipo == "num":
            numero = self.consumir("num")
            return Nodo("F", [Nodo(f"num({numero.valor})")])
        if token_actual.tipo == "(":
            self.consumir("(")
            nodo_e = self.E()
            self.consumir(")")
            return Nodo("F", [Nodo("("), nodo_e, Nodo(")")])

        raise ParserError(
            f"Token inesperado en F: '{token_actual.tipo}' ({token_actual.valor}) Se esperaba id, num o '('")


def exportar_arbol_png(
    raiz: Nodo, expresion: str, correlativo: int, carpeta_salida: str
) -> Tuple[Optional[str], Optional[str]]:
    # Dibuja el arbol con Graphviz y lo guarda en PNG
    try:
        modulo_graphviz = importlib.import_module("graphviz")
        Digraph = getattr(modulo_graphviz, "Digraph")
    except Exception:
        return None, "No esta instalado el paquete graphviz de Python"

    

    grafico = Digraph(comment="Arbol sintactico")
    grafico.attr(rankdir="TB", bgcolor="white")
    grafico.attr("node", fontname="Helvetica", style="filled,rounded", penwidth="1.2")
    grafico.attr("edge", color="#666666")

    contador = 0
    no_terminales = {"Programa", "E", "E'", "T", "T'", "F"}

    def agregar_nodo(nodo: Nodo, padre_id: Optional[str] = None) -> None:
        nonlocal contador
        nodo_id = f"n{contador}"
        contador += 1

        if nodo.etiqueta in no_terminales:
            color = "#DCEBFF"
        elif nodo.etiqueta == "vacio":
            color = "#FFF4CC"
        else:
            color = "#DDF7E3"

        grafico.node(nodo_id, nodo.etiqueta, fillcolor=color, shape="box")
        if padre_id is not None:
            grafico.edge(padre_id, nodo_id)

        for hijo in nodo.hijos:
            agregar_nodo(hijo, nodo_id)

    agregar_nodo(raiz)
    # Normaliza la expresion para usarla como parte del nombre de archivo:
    # 1) reemplaza cada secuencia de caracteres no alfanumericos por '_',
    # 2) elimina '_' al inicio y al final,
    # 3) si queda vacio, usa "expresion" como valor por defecto.
    base = re.sub(r"[^a-zA-Z0-9]+", "_", expresion).strip("_") or "expresion"

    # Nombre legible y ordenado: arbol_0001_<expresion_sanitizada>.png
    nombre_base = f"arbol_{correlativo:04d}_{base[:30]}"
    os.makedirs(carpeta_salida, exist_ok=True)
    nombre = nombre_base
    ruta_archivo = os.path.join(carpeta_salida, nombre)
    sufijo = 1
    while os.path.exists(f"{ruta_archivo}.png"):
        nombre = f"{nombre_base}_{sufijo}"
        ruta_archivo = os.path.join(carpeta_salida, nombre)
        sufijo += 1

    try:
        ruta_png = grafico.render(filename=ruta_archivo, format="png", cleanup=True)
        return ruta_png, None
    except Exception as exc:
        return None, f"Error al renderizar imagen: {exc}"


def siguiente_correlativo(carpeta_salida: str) -> int:
    """Obtiene el siguiente numero global para arboles dentro de la carpeta de salida."""
    os.makedirs(carpeta_salida, exist_ok=True)
    patron = re.compile(r"^arbol_(\d+)_")
    maximo = 0

    for nombre in os.listdir(carpeta_salida):
        if not nombre.endswith(".png"):
            continue
        coincidencia = patron.match(nombre)
        if coincidencia:
            maximo = max(maximo, int(coincidencia.group(1)))

    return maximo + 1


def abrir_imagen(ruta_imagen: str) -> None:
    # Abre la imagen con el visor por defecto del sistema
    try:
        subprocess.Popen(["xdg-open", ruta_imagen], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass


def analizar_expresion(expresion: str) -> Tuple[bool, Optional[Nodo], Optional[str]]:
    # Ejecuta lexer y parser para una expresion
    try:
        tokens = Lexer(expresion).tokenizar()
        parser = Parser(tokens)
        arbol = parser.parsear()
        return True, arbol, None
    except (LexerError, ParserError) as exc:
        return False, None, str(exc)


def principal() -> None:
    # Lee el archivo pasado por argumento
    if len(sys.argv) < 2:
        print("Uso: python3 analizador_sintactico.py <archivo> [--abrir]")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    abrir_automatico = "--abrir" in sys.argv[2:]
    carpeta_salida = "salida_arboles"
    correlativo = siguiente_correlativo(carpeta_salida)
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.read().splitlines()

    # Analiza cada linea no vacia
    indice = 1
    for linea in lineas:
        if not linea.strip():
            continue

        aceptada, arbol, error = analizar_expresion(linea)
        estado = "ACEPTADA" if aceptada else "RECHAZADA"
        print(f'{estado} "{linea}"')

        if arbol is not None:
            ruta_imagen, error_imagen = exportar_arbol_png(arbol, linea, correlativo, carpeta_salida)
            if ruta_imagen is not None:
                print(f"Imagen generada: {ruta_imagen}")
                correlativo += 1
                if abrir_automatico:
                    abrir_imagen(ruta_imagen)
            else:
                print(f"No se genero imagen: {error_imagen}")
        else:
            print(f"Error: {error}")

        print("=" * 60)
        indice += 1


if __name__ == "__main__":
    principal()
