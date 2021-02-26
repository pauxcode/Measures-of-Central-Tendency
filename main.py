# Media = Sumatoria de todos los elementos emtre la cantida de numeros
import numpy as np
import statistics as stat
import pandas as pd
import matplotlib.pyplot as plt

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
    lis_lis = []
    N = int(input("Cuantos datos vas a ingresar? "))

    for x in range(N):
        dato = float(input("\nIngresa el dato {}: ".format(x+1)))
        dato2 = [str(x), dato]
        lis.append(dato)
        lis_lis.append(dato2)

    arr = np.array(lis)

    print("\nLos datos ordenados quedan asi: {}".format(sort(arr)))
    print("\nLa suma de los numeros es: {}".format(sum(arr)))
    print("\nLa media de los numeros es: {}".format(mean(arr)))
    print("\nLa mediana de los numeros es: {}".format(median(arr)))
    print("\nLa moda de los numeros es: {}".format(mode(arr)))

    df_nums = pd.DataFrame(lis_lis,
        columns = ['id', 'Calificaciones'])
    
    df_nums_sort = df_nums.sort_values('Calificaciones', ascending=True)
    plt.bar(df_nums_sort['id'], df_nums_sort['Calificaciones'],
            color=['b', 'r', 'g', 'm', 'k', 'c', 'y'])
    plt.show()
