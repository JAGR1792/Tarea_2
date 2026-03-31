from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def ejecutar(comando: list[str]) -> None:
    subprocess.run(comando, check=True)


def principal() -> None:
    if len(sys.argv) <= 1:
        print("No se detecto archivo de entrada")
        return

    ruta_entrada = Path(sys.argv[1])
    if not ruta_entrada.exists():
        print(f"No existe el archivo de entrada: {ruta_entrada}")
        return

    ruta_base = Path(__file__).resolve().parent
    ruta_csv = ruta_base / "resultados" / "mediciones_comparacion.csv"
    ruta_png = ruta_base / "resultados" / "grafica_comparacion.png"

    print("Ejecutando comparacion CYK vs ANTLR4...")
    ejecutar(
        [
            sys.executable,
            str(ruta_base / "analizadores" / "comparar_metodos.py"),
            str(ruta_entrada),
            str(ruta_csv),
        ]
    )

    print("Generando grafica PNG de comparacion...")
    ejecutar(
        [
            sys.executable,
            str(ruta_base / "analizadores" / "graficar_comparacion.py"),
            str(ruta_csv),
            str(ruta_png),
        ]
    )

    print("Generando reporte markdown automaticamente...")
    ejecutar(
        [
            sys.executable,
            str(ruta_base / "analizadores" / "generar_reporte.py"),
        ]
    )

    print("\nProceso completado exitosamente.\n")
    print(f"CSV: {ruta_csv}")
    print(f"Grafica: {ruta_png}")
    print(f"Reporte: {ruta_base / 'reportes' / 'comparacion_seria.md'}")


if __name__ == '__main__':
    principal()
