# a = int(input("Ingrese el 1er Numero: "))
# b = int(input("Ingrese el 2do Numero: "))

# suma = a+b
# resta = a-b
# multi = a*b
# div = a/b
# mod = a%b
# pot = a**b
# divFloor = a//b

# mensaje = f"""
# Para los numeros {a} y {b}:
# El resultado de la suma es {suma}.
# El resultado de la resta es {resta}.
# El resultado de la multiplicación es {multi}.
# El resultado de la division es {div}.
# """

# print(mensaje)
print("""
    Bienvenido a LA calculadora.
    Para salir, escribe salir
    Las operaciones son suma, reta, multi y div
    """)

entrada = ""
operacion = ""
res = 0
a = 0
b = 0

while not entrada.isdigit() and entrada.lower() != "salir":
    entrada = input("Ingrese un número: ")
    if entrada.isdigit():
        a = int(entrada)
    elif entrada.lower() == "salir":
        continue
    else:
        print("Ingrese un número, no algo con letras")

while entrada.lower() != "salir":

    entrada = input("Ingrese la operacion: ")
    if entrada.lower() == "salir":
        print("Saliendo...")
        continue
    elif not (entrada.lower() == "suma" or entrada.lower() == "resta" or entrada.lower() == "multi" or entrada.lower() == "div"):
        print("Ingrese la operacion de nuevo")
        continue
    else:
        operacion = entrada

    while not entrada.isdigit() and entrada.lower() != "salir":
        entrada = input("Ingrese el segundo número: ")
        if entrada.isdigit():
            b = int(entrada)
        elif entrada.lower() == "salir":
            continue
        else:
            print("Ingrese un número, no algo con letras")

    if entrada.lower() != "salir":
        if operacion == "suma":
            res = a + b
        elif operacion == "resta":
            res = a - b
        elif operacion == "multi":
            res = a * b
        elif operacion == "div":
            res = a / b

        print("El resultado de la ",operacion," es: ", res)
        a = res
    
