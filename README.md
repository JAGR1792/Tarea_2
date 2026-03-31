# Tarea 2: Comparacion CYK vs ANTLR4

Este repositorio compara el rendimiento de dos enfoques de analisis sintactico:

- CYK con complejidad $O(n^3)$
- Parser lineal con ANTLR4 (comportamiento $O(n)$ en esta gramatica)

## Estructura del proyecto

```text
.
├── analizadores/
│   ├── algoritmo_cyk.py
│   ├── analizador_lineal_antlr4.py
│   ├── comparar_metodos.py
│   ├── graficar_comparacion.py
│   └── generar_reporte.py
├── entradas/
│   └── entrada_tarea2.txt
├── gramatica/
│   └── Ejemplo.g4
├── reportes/
│   └── comparacion_seria.md
├── resultados/
│   ├── mediciones_comparacion.csv
│   └── grafica_comparacion.png
├── main.py
└── requirements.txt
```

## Instalacion

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecucion recomendada (todo automatico)

```bash
python3 main.py entradas/entrada_tarea2.txt
```

Este comando ejecuta el flujo completo:

1. Corre CYK y ANTLR4 sobre el archivo de entrada
2. Genera el CSV de mediciones
3. Genera la grafica comparativa en PNG
4. Genera el reporte markdown automaticamente con tabla y analisis matematico

Salidas:

- resultados/mediciones_comparacion.csv
- resultados/grafica_comparacion.png
- reportes/comparacion_seria.md

## Ejecucion manual por componentes

```bash
python3 analizadores/algoritmo_cyk.py entradas/entrada_tarea2.txt
python3 analizadores/analizador_lineal_antlr4.py entradas/entrada_tarea2.txt
python3 analizadores/comparar_metodos.py entradas/entrada_tarea2.txt
python3 analizadores/graficar_comparacion.py resultados/mediciones_comparacion.csv resultados/grafica_comparacion.png
python3 analizadores/generar_reporte.py
```

## Formato de entrada

Todos los scripts reciben archivo de entrada por argumento. Si no se pasa archivo, reportan:

```text
No se detecto archivo de entrada
```

## Gramatica utilizada

```antlr
grammar Ejemplo;

s : 'a' b c EOF ;

b : 'b' 'bas'
   | 'big' c 'boss'
   ;

c : 'c'
   |
   ;

WS : [ \t\r\n]+ -> skip ;
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b84acff6-3f85-432b-8f42-2aae7c035deb" />


Nota: la entrada valida mas larga de esta gramatica es corta (maximo 5 tokens), por lo que para evidenciar el crecimiento de CYK se incluyen entradas largas rechazadas en tiempo de analisis.
