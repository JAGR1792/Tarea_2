from __future__ import annotations

import sys
import time
from typing import Dict, List, Set, Tuple


class AnalizadorCYK:
    """CYK para una version en CNF equivalente a la gramatica de Ejemplo.g4."""

    def __init__(self) -> None:
        self.simbolo_inicial = "S"
        self.reglas_terminales: Dict[str, Set[str]] = {}
        self.reglas_binarias: Dict[Tuple[str, str], Set[str]] = {}
        self._cargar_gramatica_cnf()

    def _cargar_gramatica_cnf(self) -> None:
        # Preterminales
        self.reglas_terminales = {
            "TA": {"a"},
            "TB": {"b"},
            "TBAS": {"bas"},
            "TBIG": {"big"},
            "TBOSS": {"boss"},
            "TC": {"c"},
        }

        # Reglas binarias (CNF) equivalentes al lenguaje del ejemplo:
        # s -> a b c
        # b -> b bas | big c boss
        # c -> c | epsilon
        self.reglas_binarias = {
            ("TA", "R1"): {"S"},
            ("TA", "R2"): {"S"},

            # Rama: a b bas [c]
            ("TB", "TBAS"): {"R1"},
            ("TB", "U1"): {"R1"},
            ("TBAS", "TC"): {"U1"},

            # Rama: a big [c] boss [c]
            ("TBIG", "TBOSS"): {"R2"},
            ("TBIG", "V2"): {"R2"},
            ("TBIG", "V3"): {"R2"},
            ("TBIG", "V4"): {"R2"},
            ("TC", "TBOSS"): {"V2"},
            ("TBOSS", "TC"): {"V3"},
            ("TC", "W1"): {"V4"},
            ("TBOSS", "TC"): {"W1", "V3"},
        }

    def analizar_cyk(self, tokens: List[str]) -> bool:
        n = len(tokens)
        if n == 0:
            return False

        tabla: List[List[Set[str]]] = [[set() for _ in range(n)] for _ in range(n)]

        for i, token in enumerate(tokens):
            for no_terminal, terminales in self.reglas_terminales.items():
                if token in terminales:
                    tabla[i][i].add(no_terminal)

        for longitud in range(2, n + 1):
            for i in range(n - longitud + 1):
                j = i + longitud - 1
                for k in range(i, j):
                    for izq in tabla[i][k]:
                        for der in tabla[k + 1][j]:
                            padres = self.reglas_binarias.get((izq, der), set())
                            if padres:
                                tabla[i][j].update(padres)

        return self.simbolo_inicial in tabla[0][n - 1]


def principal() -> None:
    analizador = AnalizadorCYK()

    if len(sys.argv) <= 1:
        print("No se detecto archivo de entrada")
        return

    ruta_entrada = sys.argv[1]
    with open(ruta_entrada, "r", encoding="utf-8") as archivo:
        lineas = archivo.read().splitlines()

    for linea in lineas:
        if not linea.strip():
            continue
        tokens = linea.strip().split()
        t_0 = time.perf_counter()
        resultado = analizador.analizar_cyk(tokens)
        t_1 = time.perf_counter()
        estado = "ACEPTADA" if resultado else "RECHAZADA"
        print(f"{linea} -> {estado} ({t_1 - t_0:.6f} s)")


if __name__ == "__main__":
    principal()
