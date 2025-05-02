import math

def metEuler(f, x0, y0, xn, h):
    table = [(x0, y0)]
    x = x0
    y = y0
    while x < xn:
        y = y + h * f(x, y)
        x = x + h
        table.append((x, y))
    return table

def main():
    print("Resolviendo por Euler")
    print("-----------------------")
    
    eq_str = input("Ingresa la ecuación f(x, y) en términos de x e y (por ejemplo, '2*x - 3*y + 1'): ")
    
    # Se define la función evaluando la cadena ingresada.
    def f(x, y):
        return eval(eq_str, {"x": x, "y": y, "math": math})
    
    # Solicita las condiciones iniciales y otros parámetros.
    x0 = float(input("Ingresa el x0: "))
    y0 = float(input("Ingresa el y0: "))
    xn = float(input("Ingresa el valor final xn: "))
    h = float(input("Ingresa el tamaño de paso h: "))
    
    # Calcula los valores usando Euler.
    table = metEuler(f, x0, y0, xn, h)
    
    # Imprime la tabla de resultados.
    print("\nTabla de valores:")
    print("{:<10}{:<10}".format("x", "y"))
    print("-" * 20)
    for (x, y) in table:
        print("{:<10.4f}{:<10.4f}".format(x, y))

if __name__ == '__main__':
    main()
