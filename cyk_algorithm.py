"""
Algoritmo CYK (Cocke-Younger-Kasami)

Análisis sintáctico bottom-up para gramáticas en Forma Normal de Chomsky (CNF).
Complejidad: O(n³) tiempo, O(n²) espacio.
"""

from typing import Dict, List, Set, Tuple


class CYKParser:
    """
    Implementación del algoritmo CYK.
    
    La gramática debe estar en Forma Normal de Chomsky:
    - A → B C (dos no-terminales)
    - A → a (un terminal)
    - S → ε (solo para símbolo inicial)
    """
    
    def __init__(self):
        """
        Inicializa el parser con una gramática de prueba.
        
        Estructura de gramática:
        - terminal_rules: {no_terminal: [terminales]}
        - binary_rules: {(no_terminal1, no_terminal2): [no_terminal que genera]}
        """
        self.terminal_rules: Dict[str, Set[str]] = {}  # A → a
        self.binary_rules: Dict[Tuple[str, str], Set[str]] = {}  # A → B C
        self.symbols: Set[str] = set()
        self.start_symbol = 'S'
        
        # Gramática de prueba en CNF
        self._load_grammar()
    
    def _load_grammar(self) -> None:
        """Carga gramática en Forma Normal de Chomsky."""
        # Reglas terminales: A → a
        self.terminal_rules = {
            'A': {'a'},
            'B': {'b'},
            'C': {'c'},
            'D': {'d'},
        }
        
        # Reglas binarias: A → B C
        self.binary_rules = {
            ('A', 'B'): {'S'},
            ('C', 'D'): {'S'},
            ('A', 'A'): {'A'},
            ('B', 'B'): {'B'},
            ('C', 'C'): {'C'},
            ('D', 'D'): {'D'},
        }
        
        self.symbols = {'S', 'A', 'B', 'C', 'D'}
    
    def parse(self, cadena: str) -> Tuple[bool, List[List[Set[str]]]]:
        """
        Analiza una cadena usando CYK.
        
        Retorna:
        - (aceptada, tabla): tupla con resultado y tabla de análisis
        """
        n = len(cadena)
        
        # Inicializar tabla: T[i][j] = conjunto de no-terminales que generan s[i:j+1]
        tabla: List[List[Set[str]]] = [[set() for _ in range(n)] for _ in range(n)]
        
        # Llenar diagonal: palabras de longitud 1
        for i in range(n):
            char = cadena[i]
            # Buscar todos los no-terminales A donde A → cadena[i]
            for nt, terminales in self.terminal_rules.items():
                if char in terminales:
                    tabla[i][i].add(nt)
        
        # Llenar tabla: palabras de longitud > 1
        for longitud in range(2, n + 1):  # longitud de subcadena
            for i in range(n - longitud + 1):
                j = i + longitud - 1
                # Dividir subcadena s[i:j+1] en s[i:k] y s[k+1:j]
                for k in range(i, j):
                    # k es el punto de división
                    # tabla[i][k] = conjunto de no-terminales que generan s[i:k+1]
                    # tabla[k+1][j] = conjunto de no-terminales que generan s[k+1:j+1]
                    
                    for nt1 in tabla[i][k]:
                        for nt2 in tabla[k + 1][j]:
                            # Si existe A → B C en gramática
                            pares = (nt1, nt2)
                            if pares in self.binary_rules:
                                # Agregar A a tabla[i][j]
                                tabla[i][j].update(self.binary_rules[pares])
        
        # Aceptada si S está en tabla[0][n-1]
        aceptada = self.start_symbol in tabla[0][n - 1]
        
        return aceptada, tabla
    
    def print_tabla(self, cadena: str, tabla: List[List[Set[str]]]) -> None:
        """Imprime la tabla de análisis de forma legible."""
        n = len(cadena)
        print(f"\nTabla CYK para cadena: '{cadena}'")
        print("=" * 60)
        
        # Encabezado
        print("Posición:", end=" ")
        for i in range(n):
            print(f"{cadena[i]:5s}", end=" ")
        print()
        print("-" * 60)
        
        # Mostrar tabla de arriba hacia abajo (por diagonales)
        for diagonal in range(n):
            for i in range(n - diagonal):
                j = i + diagonal
                simbolos = ', '.join(tabla[i][j]) if tabla[i][j] else "∅"
                print(f"[{i},{j}]({simbolos:15s})", end=" ")
            print()


def main():
    """Programa principal."""
    parser = CYKParser()
    
    # Casos de prueba
    casos = [
        "aaabbb",      # Debe aceptar: A+ B+
        "aabaa",       # Debe rechazar
        "cccdddd",     # Debe aceptar: C+ D+
        "abbab",       # Debe rechazar
        "a",           # Debe aceptar (palabra simple)
        "ab",          # Debe aceptar (A B)
    ]
    
    print("\n" + "=" * 70)
    print("ALGORITMO CYK (Cocke-Younger-Kasami)")
    print("=" * 70)
    print(f"Complejidad: O(n³) donde n = longitud de la cadena")
    print(f"Gramática en Forma Normal de Chomsky (CNF)")
    print("=" * 70)
    
    for cadena in casos:
        aceptada, tabla = parser.parse(cadena)
        
        estado = "✓ ACEPTADA" if aceptada else "✗ RECHAZADA"
        print(f"\nCadena: '{cadena}' → {estado}")
        parser.print_tabla(cadena, tabla)


if __name__ == "__main__":
    main()
