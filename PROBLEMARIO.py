import math

def mostrar_introduccion():
    print("="*70)
    print("INSTITUTO TECNOLÓGICO SUPERIOR DE COMALCALCO")
    print("ALGORITMO PARA ANÁLISIS DE ESFUERZO NORMAL POR FLEXIÓN BIAXIAL")
    print("="*70)
    print("Este programa calcula los esfuerzos normales totales en los puntos")
    print("críticos de tres secciones transversales (L, I, Circular) sometidas")
    print("a momentos flectores Mx = 100 Nm y My = 50 Nm.")
    print("El origen de coordenadas se ubica automáticamente en el centroide.")
    print("="*70 + "\n")

def calcular_esfuerzo(mx, my, ix, iy, x, y):
   
    return (-(mx * y) / ix) + ((my * x) / iy)

def caso_a_L():
    print("\n--- CASO A: SECCIÓN EN L ---")
    b = float(input("Ingrese la base (m): "))
    h = float(input("Ingrese la altura (m): "))
    t = float(input("Ingrese el espesor t (m): "))
    
    
    a1, a2 = h * t, (b - t) * t
    y1, y2 = h / 2, t / 2
    x1, x2 = t / 2, (b + t) / 2
    
   
    cx = (a1 * x1 + a2 * x2) / (a1 + a2)
    cy = (a1 * y1 + a2 * y2) / (a1 + a2)
    
   
    ix = ((t * h**3)/12 + a1*(y1-cy)**2) + (((b-t)*t**3)/12 + a2*(y2-cy)**2)
    iy = ((h * t**3)/12 + a1*(x1-cx)**2) + ((t*(b-t)**3)/12 + a2*(x2-cx)**2)
    
    puntos = {
        'a': (-cx, h-cy), 'b': (t-cx, h-cy), 'c': (-cx, t-cy), 
        'd': (t-cx, t-cy), 'g': (b-cx, t-cy), 'h': (-cx, -cy), 'j': (b-cx, -cy)
    }
    imprimir_resultados(ix, iy, puntos)

def caso_b_I():
    print("\n--- CASO B: SECCIÓN EN I ---")
    b = float(input("Ingrese el ancho del patín b (m): "))
    h = float(input("Ingrese la altura total h (m): "))
    t = float(input("Ingrese el espesor t (m): "))
    
  
    ix = (b * h**3 / 12) - ((b - t) * (h - 2*t)**3 / 12)
    iy = (2 * (t * b**3 / 12)) + ((h - 2*t) * t**3 / 12)
    
    puntos = {
        'a': (-b/2, h/2), 'c': (b/2, h/2), 'e': (-t/2, h/2 - t),
        'f': (t/2, h/2 - t), 'h': (-t/2, 0), 'i': (t/2, 0)
    }
    imprimir_resultados(ix, iy, puntos)

def caso_c_Circular():
    print("\n--- CASO C: SECCIÓN CIRCULAR HUECA ---")
    
    r_int = float(input("Ingrese el radio interior (m): ")) # Ejemplo: 0.15
    r_ext = float(input("Ingrese el radio exterior (m): ")) 
   
    t_pulg = 2.0 
    t_m = t_pulg * 0.0254  
    
    r_ext = r_int + t_m
    
    print(f"Radio exterior calculado: {r_ext:.4f} m")
    
    i_total = (math.pi / 4) * (r_ext**4 - r_int**4)
   
    puntos = {
        'a': (0, r_ext),    
        'b': (0, r_int),     
        'c': (-r_ext, 0),    
        'd': (-r_int, 0),    
        'f': (r_ext, 0),     
        'h': (0, -r_ext)     
    }
    
    imprimir_resultados(i_total, i_total, puntos)

def imprimir_resultados(ix, iy, puntos):
    mx, my = 100.0, 50.0
    print(f"\nResultados (Ix: {ix:.2e} m^4, Iy: {iy:.2e} m^4):")
    print("-" * 40)
    for p, coord in puntos.items():
        esf = calcular_esfuerzo(mx, my, ix, iy, coord[0], coord[1])
        tipo = "Tensión" if esf > 0 else "Compresión"
        print(f"Punto {p}: {esf:12.2f} Pa ({tipo})")

def main():
    mostrar_introduccion()
    while True:
        op = input("Seleccione Caso (1:L, 2:I, 3:Circ, 0:Salir): ")
        if op == '1': caso_a_L()
        elif op == '2': caso_b_I()
        elif op == '3': caso_c_Circular()
        elif op == '0': break
        else: print("Opción inválida.")

if __name__ == "__main__":
    main()