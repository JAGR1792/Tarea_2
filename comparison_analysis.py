"""
Análisis comparativo: CYK vs Parser LL

Medición de complejidad, tiempo y recursos.
"""

import time
from typing import List, Tuple
from cyk_algorithm import CYKParser
from ll_parser import LLParser


class ComparativeAnalysis:
    """Análisis comparativo de CYK y Parser LL."""
    
    def __init__(self):
        self.cyk = CYKParser()
        self.ll = LLParser()
        self.resultados_cyk = []
        self.resultados_ll = []
    
    def generar_cadenas_cyk(self) -> List[str]:
        """Genera cadenas de prueba para CYK."""
        return [
            "a",
            "ab",
            "aabb",
            "aaabbb",
            "aaaabbbb",
            "aaaaabbbbb",
            "aaaaaabbbbbb",
            "aaaaaaabbbbbbb",
        ]
    
    def generar_cadenas_ll(self) -> List[str]:
        """Genera cadenas de prueba para Parser LL."""
        return [
            "a",
            "a+b",
            "a*b+c",
            "a+b*c+d",
            "a*b+c*d+e",
            "a+b*c+d*e+f",
            "a*b+c*d+e*f+g",
            "a+b*c+d*e+f*g+h",
        ]
    
    def benchmark_cyk(self) -> None:
        """Mide rendimiento de CYK."""
        print("\n" + "=" * 70)
        print("BENCHMARK: Algoritmo CYK")
        print("=" * 70)
        print(f"{'Longitud (n)':<15} {'Tiempo (ms)':<15} {'Operaciones (n³)':<20}")
        print("-" * 70)
        
        for cadena in self.generar_cadenas_cyk():
            inicio = time.time()
            aceptada, tabla = self.cyk.parse(cadena)
            tiempo_ms = (time.time() - inicio) * 1000
            
            n = len(cadena)
            ops_teoricas = n ** 3
            
            self.resultados_cyk.append((n, tiempo_ms, ops_teoricas))
            
            print(f"{n:<15} {tiempo_ms:<15.4f} {ops_teoricas:<20}")
    
    def benchmark_ll(self) -> None:
        """Mide rendimiento de Parser LL."""
        print("\n" + "=" * 70)
        print("BENCHMARK: Parser LL(1)")
        print("=" * 70)
        print(f"{'Longitud (n)':<15} {'Tiempo (ms)':<15} {'Operaciones (n)':<20}")
        print("-" * 70)
        
        for cadena in self.generar_cadenas_ll():
            inicio = time.time()
            aceptada, error = self.ll.parsear(cadena)
            tiempo_ms = (time.time() - inicio) * 1000
            
            n = len(cadena)
            ops_teoricas = n
            
            self.resultados_ll.append((n, tiempo_ms, ops_teoricas))
            
            print(f"{n:<15} {tiempo_ms:<15.6f} {ops_teoricas:<20}")
    
    def mostrar_comparacion(self) -> None:
        """Muestra comparación teórica y práctica."""
        print("\n" + "=" * 70)
        print("COMPARACIÓN TEÓRICA")
        print("=" * 70)
        
        datos = [
            ("Complejidad temporal", "O(n³)", "O(n)"),
            ("Complejidad espacial", "O(n²)", "O(n)"),
            ("Tipo de análisis", "Bottom-up", "Top-down"),
            ("Gramáticas soportadas", "CNF", "LL(k)"),
            ("Velocidad", "Lenta", "Rápida"),
            ("Facilidad de implementación", "Moderada", "Simple"),
            ("Caso de uso típico", "Análisis general", "Compiladores"),
            ("Recursión por izquierda", "Soporta", "No soporta"),
        ]
        
        print(f"\n{'Característica':<30} {'CYK':<25} {'Parser LL(1)':<25}")
        print("-" * 80)
        for aspecto, cyk_val, ll_val in datos:
            print(f"{aspecto:<30} {cyk_val:<25} {ll_val:<25}")
    
    def analisis_escalabilidad(self) -> None:
        """Análisis de cómo escala cada algoritmo."""
        print("\n" + "=" * 70)
        print("ANÁLISIS DE ESCALABILIDAD")
        print("=" * 70)
        
        if self.resultados_cyk:
            print("\nCYK (O(n³)):")
            print("Si n aumenta de 10 a 20 caracteres:")
            print(f"  - Operaciones teóricas: 1000 → 8000 (8x más)")
            print(f"  - Tiempo esperado: aumenta cúbicamente")
            print(f"  - Para n=100: ~1,000,000 operaciones")
            print(f"  - Para n=1000: ~1,000,000,000 operaciones ❌ IMPRACTICABLE")
        
        if self.resultados_ll:
            print("\nParser LL(1) (O(n)):")
            print("Si n aumenta de 10 a 20 caracteres:")
            print(f"  - Operaciones teóricas: 10 → 20 (2x más)")
            print(f"  - Tiempo esperado: aumenta linealmente")
            print(f"  - Para n=100: ~100 operaciones")
            print(f"  - Para n=1000: ~1000 operaciones ✓ MUY RÁPIDO")
    
    def resumen_final(self) -> None:
        """Proporciona un resumen final."""
        print("\n" + "=" * 70)
        print("RESUMEN Y CONCLUSIONES")
        print("=" * 70)
        
        print("\n1. VENTAJAS DE CYK:")
        print("   ✓ Funciona con cualquier gramática en CNF")
        print("   ✓ Útil para análisis de lenguajes naturales")
        print("   ✓ Garantiza encontrar derivaciones")
        print("   ✗ PERO: O(n³) lo hace impracticable para textos grandes")
        
        print("\n2. VENTAJAS DE PARSER LL(1):")
        print("   ✓ Complejidad O(n) muy eficiente")
        print("   ✓ Fácil de implementar y entender")
        print("   ✓ Ideal para compiladores")
        print("   ✗ PERO: Restricciones en la gramática")
        
        print("\n3. RECOMENDACIONES DE USO:")
        print("   • Para lenguajes de programación → Parser LL/LR (O(n))")
        print("   • Para lenguajes naturales → CYK u otro parser general")
        print("   • Para análisis en tiempo real → Parser lineal obligatorio")
        print("   • Para análisis offline de texto → CYK aceptable si n es pequeño")
        
        print("\n" + "=" * 70)


def main():
    """Programa principal."""
    analisis = ComparativeAnalysis()
    
    # Ejecutar benchmarks
    analisis.benchmark_cyk()
    analisis.benchmark_ll()
    
    # Mostrar comparaciones
    analisis.mostrar_comparacion()
    analisis.analisis_escalabilidad()
    analisis.resumen_final()


if __name__ == "__main__":
    main()
