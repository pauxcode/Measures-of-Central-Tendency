# Media = Sumatoria de todos los elementos emtre la cantida de numeros
import numpy as np
import statistics as stat

def sort(arr):
    return np.sort(arr)

def sum(arr):
    return np.sum(arr)

def mean(arr):
    return np.mean(arr)

def median(arr):
    return np.median(arr)

def mode(arr):
    return stat.multimode(arr)

if __name__ == "__main__":
    lis = []
    N = int(input("Cuantos datos vas a ingresar? "))

    for x in range(N):
        dato = float(input("\nIngresa el dato {}: ".format(x+1)))
        lis.append(dato)

    arr = np.array(lis)

    print("\nLos datos ordenados quedan asi: {}".format(sort(arr)))
    print("\nLa suma de los numeros es: {}".format(sum(arr)))
    print("\nLa media de los numeros es: {}".format(mean(arr)))
    print("\nLa mediana de los numeros es: {}".format(median(arr)))
    print("\nLa moda de los numeros es: {}".format(mode(arr)))
