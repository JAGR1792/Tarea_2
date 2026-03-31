"""
Parser LL(1) - Análisis descendente recursivo

Complejidad: O(n) donde n = longitud de la cadena.
Características: top-down, predictivo, sin backtracking.
"""

from typing import List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class Token:
    tipo: str
    valor: str


class LLParser:
    """
    Parser LL(1) descendente recursivo.
    
    Gramática (sin recursión por izquierda):
    E  → T E'
    E' → + T E' | ε
    T  → F T'
    T' → * F T' | ε
    F  → ( E ) | id
    """
    
    def __init__(self):
        self.tokens: List[Token] = []
        self.pos = 0
    
    def tokenizar(self, expresion: str) -> List[Token]:
        """Convierte string en lista de tokens."""
        tokens = []
        i = 0
        while i < len(expresion):
            if expresion[i].isspace():
                i += 1
                continue
            elif expresion[i].isalpha():
                # Identificador
                inicio = i
                while i < len(expresion) and expresion[i].isalnum():
                    i += 1
                tokens.append(Token('id', expresion[inicio:i]))
            elif expresion[i].isdigit():
                # Número
                inicio = i
                while i < len(expresion) and expresion[i].isdigit():
                    i += 1
                tokens.append(Token('num', expresion[inicio:i]))
            elif expresion[i] in '+-':
                tokens.append(Token('opsuma', expresion[i]))
                i += 1
            elif expresion[i] in '*/':
                tokens.append(Token('opmul', expresion[i]))
                i += 1
            elif expresion[i] == '(':
                tokens.append(Token('(', '('))
                i += 1
            elif expresion[i] == ')':
                tokens.append(Token(')', ')'))
                i += 1
            else:
                i += 1
        
        tokens.append(Token('FIN', 'FIN'))
        return tokens
    
    def actual(self) -> Token:
        """Token actual sin consumir."""
        return self.tokens[self.pos]
    
    def consumir(self, tipo_esperado: str) -> Token:
        """Consume un token del tipo esperado."""
        token = self.actual()
        if token.tipo != tipo_esperado:
            raise Exception(f"Error: esperado {tipo_esperado}, encontrado {token.tipo}")
        self.pos += 1
        return token
    
    def parsear(self, expresion: str) -> Tuple[bool, Optional[str]]:
        """
        Analiza una expresión aritmética.
        
        Retorna:
        - (aceptada, error): tupla con resultado y mensaje de error si aplica
        """
        try:
            self.tokens = self.tokenizar(expresion)
            self.pos = 0
            self.E()
            self.consumir('FIN')
            return True, None
        except Exception as e:
            return False, str(e)
    
    # Funciones por no-terminal (métodos del parser)
    
    def E(self) -> None:
        """E → T E'"""
        self.T()
        self.Ep()
    
    def Ep(self) -> None:
        """E' → + T E' | ε"""
        token = self.actual()
        if token.tipo == 'opsuma':
            self.consumir('opsuma')
            self.T()
            self.Ep()
        # ε: no hacer nada
    
    def T(self) -> None:
        """T → F T'"""
        self.F()
        self.Tp()
    
    def Tp(self) -> None:
        """T' → * F T' | ε"""
        token = self.actual()
        if token.tipo == 'opmul':
            self.consumir('opmul')
            self.F()
            self.Tp()
        # ε: no hacer nada
    
    def F(self) -> None:
        """F → id | num | ( E )"""
        token = self.actual()
        if token.tipo == 'id':
            self.consumir('id')
        elif token.tipo == 'num':
            self.consumir('num')
        elif token.tipo == '(':
            self.consumir('(')
            self.E()
            self.consumir(')')
        else:
            raise Exception(f"Error en F: token inesperado {token.tipo}")


def main():
    """Programa principal."""
    parser = LLParser()
    
    # Casos de prueba
    casos = [
        "a + b",           # Debe aceptar
        "2 * 3 + 4",       # Debe aceptar
        "( a + b ) * c",   # Debe aceptar
        "a + + b",         # Debe rechazar (error sintáctico)
        "a +",             # Debe rechazar (incompleto)
        "( ( a ) )",       # Debe aceptar
    ]
    
    print("\n" + "=" * 70)
    print("PARSER LL(1) - Análisis Descendente Recursivo")
    print("=" * 70)
    print(f"Complejidad: O(n) donde n = longitud de la cadena")
    print(f"Tipo: Top-down, predictivo, sin backtracking")
    print("=" * 70)
    
    tiempos = []
    for expresion in casos:
        aceptada, error = parser.parsear(expresion)
        
        estado = "✓ ACEPTADA" if aceptada else "✗ RECHAZADA"
        print(f"\nExpresión: '{expresion}'")
        print(f"Resultado: {estado}")
        if error:
            print(f"Error: {error}")
        
        tiempos.append(len(expresion))
    
    print("\n" + "=" * 70)
    print(f"Rango de longitudes analizadas: {min(tiempos)} a {max(tiempos)} caracteres")
    print("Todas las cadenas procesadas en O(n)")


if __name__ == "__main__":
    main()
