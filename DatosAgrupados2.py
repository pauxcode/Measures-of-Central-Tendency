from math import sqrt
intervals = []
frequency = []
cumulative_frequency = []
class_mark = []
class_boundaries = []
fx = []
fx2 = []
n = 0

def get_intervals(lower_class, width, aument = False):
    if len(intervals) == (num_intervals * 2):
        return

    if aument:
        upper_class = lower_class + width
        intervals.append(lower_class)
        intervals.append(upper_class)
        get_intervals(upper_class + 1, width, aument=True)
    else:
        upper_class = lower_class + width
        intervals.append(lower_class)
        intervals.append(upper_class)
        get_intervals(upper_class, width)

minimum_value= int(input("Ingrese el valor minimo: "))
width = int(input("Ingrese la anchura: "))
num_intervals = int(input("Ingrese la cantidad de intervalos: "))
aument = input("Los intervalos tendran aumento de 1 entre intervalos? [s/n] ")

aument = True if aument.lower() == 's' else False

get_intervals(minimum_value, width, aument=aument)

# if aument.lower() == 's':
    # get_intervals(minimum_value, width, aument=True)
# else:
#     get_intervals(minimum_value, width)


# Frequency
for x in range(num_intervals):
    res = int(input("Ingrese los valores de f: "))
    frequency.append(res)
n = sum(frequency)

# Cumulative Frequency
acumulator = 0
for x in range(num_intervals):
    acumulator = acumulator + frequency[x]
    cumulative_frequency.append(acumulator)

# Class Mark
for x in range(num_intervals):
    class_mark.append((intervals[x+x] + intervals[x+x+1]) / 2)

# Class Boundaries
for x in range(num_intervals):
    class_boundaries.append(intervals[x+x] - .5)
    class_boundaries.append(intervals[x+x+1] + .5)

# Frequency * Class Mark
for x in range(num_intervals):
    fx.append(frequency[x] * class_mark[x])
sum_fx = sum(fx)

# Frequency * Class Mark squared
for x in range(num_intervals):
    fx2.append(frequency[x]* (class_mark[x] ** 2))
sum_fx2 = sum(fx2)

# Mean
mean = sum(fx) / sum(frequency)

# Median
position = 0
if n % 2:
    n2 = (n + 1) / 2
else:
    n2 = n / 2
for x in range(num_intervals):
    # print(x, cumulative_frequency[x])
    if cumulative_frequency[x] >= n2:
        position = x
        break
median = class_boundaries[position*2] + ((n2 - cumulative_frequency[position - 1]) / frequency[position + 0] * (width + 1))

# Mode
posicion = 4
d1 = frequency[position] - frequency[position - 1]
d2 = frequency[position] - frequency[position + 1]
mode = class_boundaries[position * 2] + (d1 / (d1 + d2)) * (width + 1)

# Quartiles
def get_qudepe(k, pp, lri, f, F, C):
    np = n / pp
    p = k * np
    P = 0
    for x in range(num_intervals):
        if F[x] >= p:
            P = x
            break
    # print('P',P)
    # print('lri', lri[P*2])
    # print('p', p)
    # print('F', F[P-1])
    # print('f', f[P])
    # print('C', C)
    return lri[P*2] + ((p - F[P-1]) / f[P]) * C

Q1 = get_qudepe(1, 4, class_boundaries, frequency, cumulative_frequency, width + 1)
Q3 = get_qudepe(3, 4, class_boundaries, frequency, cumulative_frequency, width + 1)
Qm = (Q1 + Q3) / 2

# Deciles
ND = int(input('Cuantos deciles requerira? '))
deciles = []
for x in range(ND):
    decil = int(input('Ingrese el decil: '))
    deciles.append(get_qudepe(decil, 10, class_boundaries, frequency, cumulative_frequency, width + 1))

# Percentiles
NP = int(input('Cuantos percentiles requerira? '))
percentiles = []
for x in range(NP):
    percentil = int(input('Ingrese el percentil: '))
    percentiles.append(get_qudepe(percentil, 100, class_boundaries, frequency, cumulative_frequency, width + 1))

# Variance
s2 = (sum_fx2 - ((sum_fx ** 2) / n)) / (n - 1)

# Standar Deviation
s = sqrt(s2)

# CV
CV = (s / mean) * 100



# 
Sf_list = []
for x in range(num_intervals):
    # print(class_mark[x])
    # print(mean)
    # print(class_mark[x] - mean)
    # print()
    Sf_list.append((class_mark[x] - mean) ** 3)
Sf = ((1/n) * sum(Sf_list)) / (s ** 3)


# Apuntamiento o curtosis
Af_list = []
for x in range(num_intervals):
    # print(class_mark[x])
    # print(mean)
    # print(class_mark[x] - mean)
    Af_list.append(frequency[x] * ((class_mark[x] - mean) ** 4))

Af = ((1/n) * (sum(Af_list))) / (s ** 4)

# Print
print("-"*160)
print("{:<16} | {:<5} | {:<5} | {:<5} | {:<17} | {:<8} | {:<25} | {:<25} | {:<25}"
        .format("Intervals", "f", "F", "x", "Class Boundaries", "fx", "fx^2", "(x-mean)^3", "f(x-mean)^4"))
for x in range(num_intervals):
    print("{:<5,} {:<4} {:<5,} | {:<5,} | {:<5,} | {:<5,} | {:<7,} {:<3} {:<5,} | {:<8,} | {:<25,} | {:<25,} | {:<25,}"
            .format(
                    intervals[x+x], '-', intervals[x+x+1],
                    frequency[x],
                    cumulative_frequency[x],
                    class_mark[x],
                    class_boundaries[x+x], '-', class_boundaries[x+x+1],
                    fx[x],
                    fx2[x],
                    Sf_list[x],
                    Af_list[x]
                ))


print("{:<16} | {:<5} | {:<5} | {:<5} | {:<17} | {:<8,} | {:<25,} | {:<25,} | {:<25,}"
        .format("Summation", "", "", "", "", sum_fx, sum_fx2, sum(Sf_list), sum(Af_list)))
print("-"*160)

print('\nMean', mean, ', Median', median, ', Mode', mode)
# print("\nd1: ", d1, " d2: ", d2)

print('\nQ1:', Q1, 'Q3:', Q3, 'Qm:', Qm)
print('Deciles:', deciles)
print('Percentiles:', percentiles)

print('\nVariance', s2, 'Standar Deviation', s, 'C.V.', CV)

print('\nAf:', Af, 'Sf:', Sf)
