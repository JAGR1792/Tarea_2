# Tarea 2: Algoritmo CYK vs Parser Lineal

> Análisis comparativo de dos enfoques de análisis sintáctico: CYK O(n³) y parsers lineales O(n).

---

## 1) Objetivo

Comparar el algoritmo **CYK (Cocke-Younger-Kasami)** con algoritmos de análisis sintáctico lineal como **LL** y **LR**, evaluando:
- Complejidad temporal y espacial
- Tipos de gramáticas soportadas
- Facilidad de implementación
- Rendimiento práctico

---

## 2) Algoritmo CYK

### Descripción

CYK es un algoritmo **bottom-up** para análisis sintáctico que funciona con gramáticas en **Forma Normal de Chomsky (CNF)**.

**Forma Normal de Chomsky (CNF):**
```
A → B C          (dos no-terminales)
A → a            (un terminal)
S → ε            (solo para símbolo inicial)
```

### Flujo del algoritmo CYK

1. Crear tabla T de diagonales donde T[i,j] contiene no-terminales que generan la subcadena s[i:j+1].
2. Inicializar diagonal: T[i,i] contiene todos los no-terminales A donde A → s[i].
3. Llenar tabla de abajo hacia arriba:
   - Para cada subcadena s[i:j+1], buscar todas las formas de dividirla en s[i:k] y s[k+1:j].
   - Si T[i,k-1] contiene X y T[k,j] contiene Y, y existe A → X Y, agregar A a T[i,j].
4. La cadena es aceptada si S (símbolo inicial) está en T[0,n-1].

### Complejidad

- **Tiempo:** O(n³) donde n es la longitud de la cadena.
- **Espacio:** O(n² × |V|) donde |V| es el número de no-terminales.

---

## 3) Parsers Lineales (LL y LR)

### Parser LL (Left-to-right, Leftmost derivation)

Análisis **top-down** (descendente), con complejidad **O(n)** para gramáticas LL(1).

**Ventajas:**
- Fácil de implementar manualmente
- Menos requisitos de memoria
- Bueno para lenguajes de propósito general construidos

**Desventajas:**
- No soporta recursión por izquierda directa
- Restricciones en la gramática

**Aplicación:** Compiladores de lenguajes de programación, intérpretes.

### Parser LR (Left-to-right, Rightmost derivation)

Análisis **bottom-up**, con complejidad **O(n)** para gramáticas LR(1).

**Ventajas:**
- Acepta mayor variedad de gramáticas
- Detecta errores más rápidamente
- Puede manejar recursión por izquierda

**Desventajas:**
- Más complejo de implementar
- Requiere más memoria (tabla de parsing)

**Aplicación:** Generadores de parsers (yacc, bison, ANTLR).

---

## 4) Comparación Teórica

| Aspecto | CYK | Parser LL | Parser LR |
|--------|-----|----------|----------|
| **Complejidad** | O(n³) | O(n) | O(n) |
| **Tipo de análisis** | Bottom-up | Top-down | Bottom-up |
| **Gramáticas soportadas** | CNF | LL(k) | LR(k) |
| **Implementación** | Moderada | Simple | Compleja |
| **Caso de uso** | Análisis general | Lenguajes simples | Compiladores |
| **Velocidad práctica** | Lenta (n³) | Rápida (n) | Rápida (n) |
| **Memoria** | O(n²) | O(n) | O(n) |

---

## 5) Ejemplos Prácticos

### Gramática de prueba (CNF)

```
S  → A B | C D
A  → a | a A
B  → b | b B
C  → c | c C
D  → d | d D
```

### Cadenas de prueba

1. `aaabbb` → ✓ Aceptada (A+ B+)
2. `aabaa` → ✗ Rechazada (no sigue patrón)
3. `cccdddd` → ✓ Aceptada (C+ D+)

---

## 6) Estructura y Archivos

```
Tarea_2/
├── README.md
├── cyk_algorithm.py         # Implementación de CYK
├── ll_parser.py             # Implementación de parser LL
├── comparison_analysis.py    # Análisis comparativo
├── benchmark.py             # Medición de complejidad
├── grafico_complejidad.py   # Generador de gráficos
├── test_cases.txt           # Casos de prueba
└── comparacion_cyk_vs_ll.png # Gráfico de resultados
```

---

## 7) Ejecución

### Ejecutar CYK
```bash
python3 cyk_algorithm.py
```

### Ejecutar Parser LL
```bash
python3 ll_parser.py
```

### Análisis completo
```bash
python3 comparison_analysis.py
```

### Generar gráficos de complejidad
```bash
python3 grafico_complejidad.py
```

---

## 8) Conclusiones Esperadas

1. **CYK es versátil pero lento:** Acepta cualquier gramática CNF pero con O(n³), es impracticable para textos grandes.
2. **Parsers lineales son eficientes:** O(n) lo hace ideal para compiladores e intérpretes, pero con restricciones de gramática.
3. **Caso de uso:** Usa CYK para análisis general; usa LL/LR para lenguajes de programación.
