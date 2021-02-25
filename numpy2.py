import numpy as np
import statistics as stat

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(type(arr))
print(np.sort(arr))

lista = []
N = int(input("Cuantos datos vas a ingresar? "))

for x in range(N):
    dato = float(input("\nIngresa el dato {}: ".format(x+1)))
    lista.append(dato)

print(type(lista))
arr2 = np.array(lista)
print(arr2)
print(type(arr2))

arr3 = np.concatenate((arr, arr2))
print(np.sort(arr3))

print("\nla suma es: {}".format(np.sum(arr3)))
print("\nla media es: {}".format(np.mean(arr3)))
print("\nla mediana es: {}".format(np.median(arr3)))
print("\nla moda es: {}".format(stat.multimode(arr3)))
