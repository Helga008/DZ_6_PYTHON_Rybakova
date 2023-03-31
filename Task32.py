# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)



from random import randint

def FillArray(n):
    arr = [randint(1,10) for _ in range(n)]
    return arr


n = int(input('Введите размер массива: '))
massive = FillArray(n)
print(massive)

num_min = int(input('Введите минимальное значение диапазона: '))
num_max = int(input('Введите максимальное значение диапазона: '))

for i in range(n):
    if massive[i] >= num_min and massive[i] <= num_max:
        print(i)