import numpy as np;

def proMatricialBool(A, B):
    producto = np.dot(A, B)
    productoBool = np.where(producto > 1, 1, producto)
    productoBool = productoBool.astype(int)
    return productoBool

def lessOrEqual(A, B):
    return np.all(A <= B)

def checkSymmetrical(A):
    return np.array_equal(A, A.T)

def checkTransitive(A):
    return np.all(np.where(np.dot(A, A) > 0, 1, 0) <= A)

def checkAntisymm(A):
    # Convertir la matriz a un array de numpy
    A = np.array(A)
    
    # Calcular la transpuesta de la matriz
    A_T = np.transpose(A)
    
    # Comprobar si la transpuesta es igual a la negativa de la matriz original
    return np.array_equal(A_T, -A)

def checkReflexive(A):
    for i in range(len(A)):
        if A[i][i] != 1:
            return False
    return True

def printPOSET(A):
    print(A)
    print("La matriz es antisimetrica: " + str(checkAntisymm(A)))
    print("La matriz es transitiva: " + str(checkTransitive(A)))
    print("La matriz es reflexiva: " + str(checkReflexive(A)) + "\n")

def printEQUIV(A):
    print(A)
    print("La matriz es simetrica: " + str(checkSymmetrical(A)))
    print("La matriz es transitiva: " + str(checkTransitive(A)))
    print("La matriz es reflexiva: " + str(checkReflexive(A)) + "\n")

def main():
    A = np.array([[1, 0, 0, 0], 
                  [1, 1, 0, 0], 
                  [1, 1, 1, 0],
                  [1, 1, 1, 1]])

    print("Para la matriz de relación del Ejercicio 4:\n")
    printPOSET(A)
    print("\nPor lo tanto, la matriz de relación es una relación de orden parcial")

    A = np.array([[1, 1, 0, 0, 0, 0], 
                  [1, 1, 0, 0, 0, 0], 
                  [0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0],
                  [0, 0, 0, 1, 1, 0],
                  [0, 0, 0, 0, 0, 1]])

    print("Para la matriz de relación del Ejercicio 8:\n")
    printEQUIV(A)
    print("\nPor lo tanto, la matriz de relación es una relación de equivalencia")

    # {(−4/−20),(−3/−9),(−2/−4),(−1/−11),(−1/−3),(1/2),(1/5),(2/10),(2/14),(3/6),(4/8),(4/12)}
    #Orden de los elementos, del 1 al 12
    A = np.array([[1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                  [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                  [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                  [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],])

    print("Para la matriz de relación del Ejercicio 8:\n")
    printEQUIV(A)
    print("\nPor lo tanto, la matriz de relación es una relación de equivalencia")

main()