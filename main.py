import random

n = input("Введите количество элементов в массииве: ")
x = input("Введите искомое число: ")
A = []
for i in range(int(n)):
    A.append(random.randint(0, 20))

print(A)

a_near = []
for i in range(int(n)):
    a_near.append(abs(int(x) - A[i]))

a_near_min = min(a_near)
ind_min = a_near.index(a_near_min)
a_near_d = A[ind_min]

print("Ближайшее число к искомому", a_near_d)