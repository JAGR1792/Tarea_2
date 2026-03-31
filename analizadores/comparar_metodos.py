from __future__ import annotations

import csv
import sys
import time
from pathlib import Path

from algoritmo_cyk import AnalizadorCYK
from analizador_lineal_antlr4 import AnalizadorLinealANTLR4


def principal() -> None:
    if len(sys.argv) <= 1:
        print("No se detecto archivo de entrada")
        return

    ruta_entrada = Path(sys.argv[1])
    ruta_csv = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("resultados/mediciones_comparacion.csv")
    ruta_md = Path(sys.argv[3]) if len(sys.argv) > 3 else Path("resultados/comparacion_resultados.md")

    cyk = AnalizadorCYK()
    antlr = AnalizadorLinealANTLR4()

    ruta_csv.parent.mkdir(parents=True, exist_ok=True)
    ruta_md.parent.mkdir(parents=True, exist_ok=True)

    filas = []
    with open(ruta_entrada, "r", encoding="utf-8") as archivo:
        for linea in archivo.read().splitlines():
            if not linea.strip():
                continue

            texto = linea.strip()

            t0 = time.perf_counter()
            res_cyk = cyk.analizar_cyk(texto.split())
            t1 = time.perf_counter()

            t2 = time.perf_counter()
            res_antlr, _ = antlr.analizar(texto)
            t3 = time.perf_counter()

            tiempo_cyk = t1 - t0
            tiempo_antlr = t3 - t2

            filas.append(
                {
                    "entrada": texto,
                    "tokens": len(texto.split()),
                    "cyk_estado": "ACEPTADA" if res_cyk else "RECHAZADA",
                    "antlr_estado": "ACEPTADA" if res_antlr else "RECHAZADA",
                    "cyk_seg": f"{tiempo_cyk:.8f}",
                    "antlr_seg": f"{tiempo_antlr:.8f}",
                }
            )
            print(
                f"{texto} -> CYK:{'ACEPTADA' if res_cyk else 'RECHAZADA'} ({tiempo_cyk:.6f} s) "
                f"| ANTLR4:{'ACEPTADA' if res_antlr else 'RECHAZADA'} ({tiempo_antlr:.6f} s)"
            )

    with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo_csv:
        escritor = csv.DictWriter(
            archivo_csv,
            fieldnames=["entrada", "tokens", "cyk_estado", "antlr_estado", "cyk_seg", "antlr_seg"],
        )
        escritor.writeheader()
        escritor.writerows(filas)

    with open(ruta_md, "w", encoding="utf-8") as archivo_md:
        archivo_md.write("# Resultados de Comparacion CYK vs ANTLR4\n\n")
        archivo_md.write("| Entrada | Tokens | CYK | ANTLR4 | Tiempo CYK (s) | Tiempo ANTLR4 (s) |\n")
        archivo_md.write("|---|---:|---|---|---:|---:|\n")
        for fila in filas:
            archivo_md.write(
                f"| {fila['entrada']} | {fila['tokens']} | {fila['cyk_estado']} | {fila['antlr_estado']} | {fila['cyk_seg']} | {fila['antlr_seg']} |\n"
            )


if __name__ == "__main__":
    principal()
