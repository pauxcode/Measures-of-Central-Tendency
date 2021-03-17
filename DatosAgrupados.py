from math import log, floor
from datos import lis

# Variables
intervals = []
corr_IR = []


# Functions
def my_round(num):
    str_num = str(num)
    if str_num[2] == '5':
        return floor(num)
    return round(num)

def get_intervals(Vmn):
    if Vmn > Vmx: 
        return IR - 1
    corr_IR.append(1)
    If = Vmn + AR
    intervals.append(Vmn)
    intervals.append(If)
    get_intervals(If + 1)

def percentage(parte, total):
    return round(100 * float(parte)/float(total), 2)


ordened_list = sorted(lis)
print(ordened_list)

Vmn = ordened_list[0]
Vmx = ordened_list[-1]
n = len(ordened_list)

# Range
R = Vmx - Vmn

# Intervals
I = 1 + 3.32*log(n, 10)
IR = my_round(I)

# Width
A = R / I
AR = my_round(A)


print("\nValor min: ", Vmn)
print("Valor max: ", Vmx)

print("\nRango: ", R)

print("\nI: ", I)
print("I::", IR)

print("\nA: ", A)
print("A::", AR)

# Intervalos
get_intervals(Vmn)
if len(intervals) / 2 > IR:
    IR = IR + 1


# f
fcontador = []
f = []
counter = 0
print(sum(corr_IR))

if sum(corr_IR) < IR:
    IR = IR - 1

print("I", IR)
for y in range(IR):
    for dato in ordened_list:
        if dato >= intervals[y+y]  and dato <= intervals[y+y+1]:
            fcontador.append(y)
for y in range(IR):
    f.append(fcontador.count(y))

# F
F = []
counter = 0
for y in range(IR):
    counter = counter + f[y]
    F.append(counter)


# x
x = []
for y in range(IR):
    x.append((intervals[y+y] + intervals[y+y+1]) / 2)


# Lim
lim = []
for y in range(IR):
    lim.append((intervals[y+y] - .5))
    lim.append((intervals[y+y+1] + .5))


# fr
fr = []
for y in range(IR):
    fr.append(percentage(f[y], n))


# Fr
Fr = []
counter = 0
for y in range(IR):
    counter = counter + fr[y]
    Fr.append(counter)


# fx
fx= []
for y in range(IR):
    fx.append(f[y] * x[y])
sum_fx = sum(fx)


# Mean
xm = sum(fx) / n


# Median
if n % 2:
    n2 = (n + 1) / 2
else:
    n2 = n / 2
def post():
    for y in range(len(F)):
        print(y, F[y])
        if F[y] >= n2:
            return y
posicion = post()
print("Pos", posicion)
print("lim", lim[posicion*2])
print("n2", n2)
print("F", F[posicion - 1])
print("Resta", n2 - F[posicion - 1])
print("f", f[posicion + 0])
xmd = lim[posicion*2] + ((n2 - F[posicion - 1]) / f[posicion + 0]) * (AR + 1)



# Mode
posicion = 4
print(posicion)
d1 = f[posicion] - f[posicion - 1]
d2 = f[posicion] - f[posicion + 1]
mo = lim[posicion * 2] + (d1 / (d1 + d2)) * (AR + 1)






# Print
print("-"*80)
print("{:<16} | {:<5} | {:<5} | {:<5} | {:<13} | {:<5} | {:<5} | {:<5}"
        .format("Intervalos", "f", "F", "x", "Limites", "fr", "FR", "xf"))
for y in range(IR):
    print("{:<5} {:<4} {:<5} | {:<5} | {:<5} | {:<5} | {:<5} - {:<5} | {:<5} | {:<5} | {:<5}"
            .format(intervals[y+y], '-', intervals[y+y+1],
                    f[y],
                    F[y],
                    x[y],
                    (intervals[y+y] - .5), (intervals[y+y+1] + .5),
                    fr[y],
                    Fr[y],
                    fx[y]))
print("{:<16} | {:<5} | {:<5} | {:<5} | {:<13} | {:<5} | {:<5} | {:<5}"
        .format("", "", "", "", "", "", "", ""))
print("{:<16} | {:<5} | {:<5} | {:<5} | {:<13} | {:<5} | {:<5} | {:<5}"
        .format("Sumatoria", 1, 2, 3, "", 4, 5, sum_fx))
print("-"*80)
# print("Sumatoria de fx", sum_fx)
print("\nMedia", my_round(xm))
print("\nMediana", round(xmd))
print("\nd1: ", d1, " d2: ", d2)
print("Moda: ", my_round(mo))
