from __future__ import annotations

import importlib
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional, Tuple

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener


RUTA_BASE = Path(__file__).resolve().parent
RUTA_GRAMATICA = RUTA_BASE.parent / "gramatica" / "Ejemplo.g4"
RUTA_GENERADO = RUTA_BASE / "antlr_generado"


class EscuchaErrores(ErrorListener):
    def __init__(self) -> None:
        super().__init__()
        self.hubo_error = False
        self.mensaje: Optional[str] = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):  # type: ignore[override]
        self.hubo_error = True
        self.mensaje = f"Linea {line}, columna {column}: {msg}"


def generar_parser_si_falta() -> None:
    requeridos = [
        RUTA_GENERADO / "EjemploLexer.py",
        RUTA_GENERADO / "EjemploParser.py",
    ]
    if all(p.exists() for p in requeridos):
        return

    RUTA_GENERADO.mkdir(parents=True, exist_ok=True)
    ejecutable_antlr4 = shutil.which("antlr4")
    if ejecutable_antlr4 is None:
        candidato_venv = Path(sys.executable).resolve().parent / "antlr4"
        if candidato_venv.exists():
            ejecutable_antlr4 = str(candidato_venv)

    if ejecutable_antlr4 is None:
        raise FileNotFoundError(
            "No se encontro 'antlr4'. Instala antlr4-tools o agrega antlr4 al PATH."
        )

    subprocess.run(
        [
            ejecutable_antlr4,
            "-Dlanguage=Python3",
            "-o",
            str(RUTA_GENERADO),
            str(RUTA_GRAMATICA),
            "-no-listener",
            "-visitor",
        ],
        check=True,
    )


class AnalizadorLinealANTLR4:
    def __init__(self) -> None:
        generar_parser_si_falta()
        sys.path.insert(0, str(RUTA_GENERADO))
        lexer_mod = importlib.import_module("EjemploLexer")
        parser_mod = importlib.import_module("EjemploParser")
        self._lexer_cls = lexer_mod.EjemploLexer
        self._parser_cls = parser_mod.EjemploParser

    def analizar(self, texto: str) -> Tuple[bool, Optional[str]]:
        entrada = InputStream(texto)
        lexer = self._lexer_cls(entrada)
        tokens = CommonTokenStream(lexer)
        parser = self._parser_cls(tokens)

        escucha = EscuchaErrores()
        parser.removeErrorListeners()
        parser.addErrorListener(escucha)

        try:
            parser.s()
        except Exception as exc:
            return False, str(exc)

        if escucha.hubo_error:
            return False, escucha.mensaje
        return True, None


def principal() -> None:
    analizador = AnalizadorLinealANTLR4()

    if len(sys.argv) <= 1:
        print("No se detecto archivo de entrada")
        return

    ruta_entrada = sys.argv[1]
    with open(ruta_entrada, "r", encoding="utf-8") as archivo:
        lineas = archivo.read().splitlines()

    for linea in lineas:
        if not linea.strip():
            continue
        t_0 = time.perf_counter()
        aceptada, _ = analizador.analizar(linea.strip())
        t_1 = time.perf_counter()
        estado = "ACEPTADA" if aceptada else "RECHAZADA"
        print(f"{linea} -> {estado} ({t_1 - t_0:.6f} s)")


if __name__ == "__main__":
    principal()
