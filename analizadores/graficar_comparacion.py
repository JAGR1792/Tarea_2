from __future__ import annotations

import csv
import sys
from pathlib import Path

from PIL import Image, ImageDraw


def principal() -> None:
    if len(sys.argv) <= 1:
        print("No se detecto archivo de entrada")
        return

    ruta_csv = Path(sys.argv[1])
    ruta_png = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("resultados/grafica_comparacion.png")

    entradas = []
    tiempos_cyk = []
    tiempos_antlr = []

    with open(ruta_csv, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            entradas.append(fila["entrada"])
            tiempos_cyk.append(float(fila["cyk_seg"]))
            tiempos_antlr.append(float(fila["antlr_seg"]))

    if not entradas:
        print("El archivo de entrada no contiene filas de medicion")
        return

    ancho, alto = 1400, 800
    margen_izq, margen_der, margen_sup, margen_inf = 90, 60, 70, 140
    area_w = ancho - margen_izq - margen_der
    area_h = alto - margen_sup - margen_inf

    max_y = max(max(tiempos_cyk), max(tiempos_antlr)) * 1.2
    if max_y <= 0:
        max_y = 1.0

    imagen = Image.new("RGB", (ancho, alto), "white")
    dibujo = ImageDraw.Draw(imagen)

    # Ejes
    x0, y0 = margen_izq, alto - margen_inf
    x1, y1 = ancho - margen_der, margen_sup
    dibujo.line([(x0, y0), (x1, y0)], fill="black", width=2)
    dibujo.line([(x0, y0), (x0, y1)], fill="black", width=2)

    # Guias horizontales
    divisiones = 5
    for i in range(divisiones + 1):
        y = y0 - (area_h * i / divisiones)
        dibujo.line([(x0, y), (x1, y)], fill="#dddddd", width=1)
        valor = max_y * i / divisiones
        dibujo.text((10, y - 8), f"{valor:.6f}", fill="black")

    # Conversion coordenadas
    n = len(entradas)
    paso_x = area_w / max(n - 1, 1)

    def punto(idx: int, valor: float) -> tuple[float, float]:
        x = x0 + idx * paso_x
        y = y0 - (valor / max_y) * area_h
        return (x, y)

    puntos_cyk = [punto(i, v) for i, v in enumerate(tiempos_cyk)]
    puntos_antlr = [punto(i, v) for i, v in enumerate(tiempos_antlr)]

    # Curvas
    if len(puntos_cyk) > 1:
        dibujo.line(puntos_cyk, fill="#1f77b4", width=3)
    if len(puntos_antlr) > 1:
        dibujo.line(puntos_antlr, fill="#d62728", width=3)

    # Puntos
    radio = 4
    for px, py in puntos_cyk:
        dibujo.ellipse((px - radio, py - radio, px + radio, py + radio), fill="#1f77b4")
    for px, py in puntos_antlr:
        dibujo.ellipse((px - radio, py - radio, px + radio, py + radio), fill="#d62728")

    # Etiquetas de entradas
    for i, etiqueta in enumerate(entradas):
        x = x0 + i * paso_x
        dibujo.text((x - 25, y0 + 10), str(i + 1), fill="black")

    # Titulo y leyenda
    dibujo.text((ancho // 2 - 180, 20), "Comparacion de tiempos: CYK vs ANTLR4", fill="black")
    dibujo.rectangle((ancho - 360, 20, ancho - 340, 40), fill="#1f77b4")
    dibujo.text((ancho - 330, 22), "CYK O(n^3)", fill="black")
    dibujo.rectangle((ancho - 220, 20, ancho - 200, 40), fill="#d62728")
    dibujo.text((ancho - 190, 22), "ANTLR4 lineal O(n)", fill="black")

    # Mapa de indices -> entrada
    y_leyenda = alto - 120
    dibujo.text((margen_izq, y_leyenda), "Indices de entradas:", fill="black")
    for i, etiqueta in enumerate(entradas):
        dibujo.text((margen_izq, y_leyenda + 20 + i * 16), f"{i + 1}. {etiqueta}", fill="black")

    ruta_png.parent.mkdir(parents=True, exist_ok=True)
    imagen.save(ruta_png)
    print(f"Grafica generada: {ruta_png}")


if __name__ == "__main__":
    principal()
