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
    return np.all((A == 0) | (A != A.T))

def printSTA(A):
    print(A)
    print("La matriz es simetrica: " + str(checkSymmetrical(A)))
    print("La matriz es transitiva: " + str(checkTransitive(A)))
    print("La matriz es antisimetrica: " + str(checkAntisymm(A)) + "\n")

A = np.array([[1, 0, 1], [0, 1, 1]])
B = np.array([[1, 1], [0, 1], [1, 0]])

print(proMatricialBool(A, B))

A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 2], [3, 5]])

print("Es A menor o igual a B: " + str(lessOrEqual(A, B)) + "\n")

A = np.array([[0, 1, 0], 
              [0, 0, 1], 
              [0, 0, 0]])

printSTA(A)

A = np.array([[1, 2, 3], 
              [2, 4, 5], 
              [3, 5, 6]])

printSTA(A)

A = np.array([[1, 1, 0], 
              [0, 1, 1], 
              [1, 0, 1]])

printSTA(A)

# def checkTransitive(A):
#     A_squared = np.dot(A, A)
#     A_squared_boolean = np.where(A_squared > 0, 1, 0)
#     return np.all(A_squared_boolean <= A)