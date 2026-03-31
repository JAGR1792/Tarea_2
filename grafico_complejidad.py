"""
Generador de gráficos: Comparación CYK vs Parser LL

Visualización de complejidad temporal y escalabilidad.
"""

import matplotlib.pyplot as plt
import numpy as np


def generar_graficos():
    """Genera gráficos de comparación."""
    
    # Rango de valores n
    n_valores = np.array([5, 10, 15, 20, 25, 30, 35, 40])
    
    # Complejidades teóricas
    cyk_complejo = n_valores ** 3
    ll_complejo = n_valores
    
    # Crear figura con subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Comparación: Algoritmo CYK vs Parser LL(1)', fontsize=16, fontweight='bold')
    
    # ===== GRÁFICO 1: Complejidad Teórica (Escala Normal) =====
    ax1 = axes[0, 0]
    ax1.plot(n_valores, cyk_complejo, 'r-o', linewidth=2, markersize=8, label='CYK O(n³)')
    ax1.plot(n_valores, ll_complejo, 'g-s', linewidth=2, markersize=8, label='LL(1) O(n)')
    ax1.set_xlabel('Longitud de entrada (n)', fontsize=11)
    ax1.set_ylabel('Número de operaciones', fontsize=11)
    ax1.set_title('Complejidad Teórica (Escala Normal)', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # ===== GRÁFICO 2: Complejidad Teórica (Escala Logarítmica) =====
    ax2 = axes[0, 1]
    ax2.loglog(n_valores, cyk_complejo, 'r-o', linewidth=2, markersize=8, label='CYK O(n³)')
    ax2.loglog(n_valores, ll_complejo, 'g-s', linewidth=2, markersize=8, label='LL(1) O(n)')
    ax2.set_xlabel('Longitud de entrada (n)', fontsize=11)
    ax2.set_ylabel('Número de operaciones', fontsize=11)
    ax2.set_title('Complejidad Teórica (Escala Logarítmica)', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    # ===== GRÁFICO 3: Comparación de Ratios =====
    ax3 = axes[1, 0]
    ratio_cyk = cyk_complejo / ll_complejo
    ax3.bar(n_valores, ratio_cyk, color='orange', alpha=0.7, edgecolor='darkorange', linewidth=2)
    ax3.set_xlabel('Longitud de entrada (n)', fontsize=11)
    ax3.set_ylabel('Ratio: CYK / LL(1)', fontsize=11)
    ax3.set_title('Factor de diferencia (CYK es X veces más lento)', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Añadir valores en las barras
    for i, (n, ratio) in enumerate(zip(n_valores, ratio_cyk)):
        ax3.text(n, ratio + 50, f'{ratio:.0f}x', ha='center', fontsize=9, fontweight='bold')
    
    # ===== GRÁFICO 4: Tabla Comparativa =====
    ax4 = axes[1, 1]
    ax4.axis('off')
    
    tabla_data = [
        ['Métrica', 'CYK', 'Parser LL(1)'],
        ['Complejidad', 'O(n³)', 'O(n)'],
        ['Espacio', 'O(n²)', 'O(n)'],
        ['Velocidad', '🐌 Lenta', '⚡ Rápida'],
        ['Gramáticas', 'CNF', 'LL(k)'],
        ['Implementación', 'Moderada', 'Simple'],
        ['Caso de uso', 'Análisis general', 'Compiladores'],
    ]
    
    tabla = ax4.table(cellText=tabla_data, cellLoc='center', loc='center',
                      colWidths=[0.3, 0.35, 0.35])
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(10)
    tabla.scale(1, 2.5)
    
    # Dar color a encabezados
    for i in range(3):
        tabla[(0, i)].set_facecolor('#4CAF50')
        tabla[(0, i)].set_text_props(weight='bold', color='white')
    
    # Alternar colores en filas
    for i in range(1, len(tabla_data)):
        for j in range(3):
            if i % 2 == 0:
                tabla[(i, j)].set_facecolor('#f0f0f0')
            else:
                tabla[(i, j)].set_facecolor('#ffffff')
    
    plt.tight_layout()
    
    # Guardar figura
    plt.savefig('comparacion_cyk_vs_ll.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico guardado: comparacion_cyk_vs_ll.png")
    
    # Mostrar figura
    plt.show()


def generar_analisis_escalabilidad():
    """Genera análisis de escalabilidad para diferentes tamaños."""
    
    print("\n" + "=" * 70)
    print("ANÁLISIS DE ESCALABILIDAD")
    print("=" * 70)
    
    tamaños = [10, 50, 100, 500, 1000]
    
    print(f"\n{'n (longitud)':<15} {'CYK O(n³)':<20} {'LL(1) O(n)':<20} {'Ratio':<15}")
    print("-" * 70)
    
    for n in tamaños:
        ops_cyk = n ** 3
        ops_ll = n
        ratio = ops_cyk / ops_ll
        
        # Formatear con notación científica para números grandes
        if ops_cyk >= 1e9:
            cyk_str = f"{ops_cyk:.2e}"
        else:
            cyk_str = f"{ops_cyk:,}"
        
        print(f"{n:<15} {cyk_str:<20} {ops_ll:<20,} {ratio:.0f}x")
    
    print("\n⚠️  PUNTO CRÍTICO:")
    print("   • Para n=100: CYK requiere 1 millón de operaciones")
    print("   • Para n=1000: CYK requiere 1 billón de operaciones (IMPRACTICABLE)")
    print("   • Parser LL(1) sigue siendo lineal incluso para n=1000")


def main():
    """Programa principal."""
    print("\n" + "=" * 70)
    print("GENERADOR DE GRÁFICOS: CYK vs Parser LL(1)")
    print("=" * 70)
    
    generar_graficos()
    generar_analisis_escalabilidad()
    
    print("\n✓ Análisis completado")


if __name__ == "__main__":
    main()
