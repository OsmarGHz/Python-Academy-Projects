import math
import csv

def resolverEuler(f, x0, y0, x_end, h):
    """
    Resuelve la EDO y' = f(x, y) usando el método de Euler.
    Retorna listas con los valores de x e y.
    """
    x_values = [x0]
    y_values = [y0]
    
    # Avanzar hasta x_end
    while x_values[-1] < x_end:
        x_n = x_values[-1]
        y_n = y_values[-1]
        
        # Cálculo de la pendiente
        dydx = f(x_n, y_n)
        
        # Siguiente valor de y
        y_next = y_n + h * dydx
        
        # Siguiente valor de x
        x_next = x_n + h
        
        x_values.append(x_next)
        y_values.append(y_next)
    
    return x_values, y_values

def resolverRK4(f, x0, y0, x_end, h):
    """
    Resuelve la EDO y' = f(x, y) usando el método de Runge-Kutta de 4º orden (RK4).
    Retorna listas con los valores de x e y.
    """
    x_values = [x0]
    y_values = [y0]
    
    # Avanzar hasta x_end
    while x_values[-1] < x_end:
        x_n = x_values[-1]
        y_n = y_values[-1]
        
        k1 = f(x_n, y_n)
        k2 = f(x_n + h/2, y_n + (h/2)*k1)
        k3 = f(x_n + h/2, y_n + (h/2)*k2)
        k4 = f(x_n + h,   y_n + h*k3)
        
        # Siguiente valor de y
        y_next = y_n + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        
        # Siguiente valor de x
        x_next = x_n + h
        
        x_values.append(x_next)
        y_values.append(y_next)
    
    return x_values, y_values



# Definición de la EDO: y' = 2 cos(x) * y
def f(x, y):
    #return 2*x - 3*y + 1
    #return x + pow(y, 2)
    #return y
    #return 2*x*y
    #return math.exp(-y)
    #return pow(x, 2) + pow(y, 2)
    #return pow(x-y,2)
    #return (x*y) + math.sqrt(y)
    #return (x*(y**2)) - (y/x)
    #return y - (y**2)
    #return 2*math.cos(x)*y
    return y*(10-(2*y))
    #return 2*x*(y**2)

# Condiciones del problema

'''x0 = 1
y0 = 5
x_end = 1.2 #y(1) = 5; y(1.2) = ?
#h = 0.1
h = 0.05'''

'''x0 = 0
y0 = 0
x_end = 0.2
#h = 0.1
h = 0.05'''

'''x0 = 0
y0 = 1
x_end = 1
#h = 0.1
h = 0.05'''

'''x0 = 1
y0 = 1
x_end = 1.5
#h = 0.1
h = 0.05'''

'''x0 = 0
y0 = 0
x_end = 0.5
#h = 0.1
h = 0.05'''

'''x0 = 0
y0 = 1
x_end = 0.5
#h = 0.1
h = 0.05'''

'''x0 = 0
y0 = 0.5
x_end = 0.5
#h = 0.1
h = 0.05'''

'''x0 = 0
y0 = 1
x_end = 0.5
#h = 0.1
h = 0.05'''

'''x0 = 1
y0 = 1
x_end = 1.5
#h = 0.1
h = 0.05'''

'''x0 = 0
y0 = 0.5
x_end = 0.5
#h = 0.1
h = 0.05'''


'''x0 = 0
y0 = 1
x_end = 5
#h = 0.25
#h = 0.1
h = 0.05'''

x0 = 0
y0 = 1
x_end = 5
#h = 0.25
#h = 0.1
h = 0.05

'''x0 = 0
y0 = 1
x_end = 1.0
#h = 0.1
h = 0.05'''

# Resolver con Euler
x_euler, y_euler = resolverEuler(f, x0, y0, x_end, h)

# Resolver con RK4
x_rk4, y_rk4 = resolverRK4(f, x0, y0, x_end, h)

counter = 0  # Inicializamos el contador

# Guardar los resultados de Euler en CSV
with open("euler_data.csv", "w", newline="") as file_e:
    writer = csv.writer(file_e)
    writer.writerow(["#", "x", "y Euler"])  # Encabezados
    
    for x, y in zip(x_euler, y_euler):
        writer.writerow([f"f(x{counter}, y{counter})", x, y])  # Escribimos la fila
        counter += 1  # Incrementamos el contador en cada fila

# Reiniciamos el contador para RK4
counter = 0  

# Guardar los resultados de RK4 en CSV
with open("rk4_data.csv", "w", newline="") as file_r:
    writer = csv.writer(file_r)
    writer.writerow(["#", "x", "y RK4"])  # Encabezados
    
    for x, y in zip(x_rk4, y_rk4):
        writer.writerow([f"f(x{counter}, y{counter})", x, y])  # Escribimos la fila
        counter += 1  # Incrementamos el contador en cada fila



# Imprimir una comparación en pantalla
print(" x      Euler         RK4 ")
for xe, ye, xr, yr in zip(x_euler, y_euler, x_rk4, y_rk4):
    print(f"{xe:4.2f}  {ye:10.6f}  {yr:10.6f}")
