#HW06 Aleksey Ushakov
#Python 3.7 64bit

import random
import timeit
import math
import numpy
from memory_profiler import profile
import timeit


def time(func):
    def t(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        print(datetime.now() - start)
        return res
    return t



def bubble_sort(lst):

    for j in
        for i in range(j):
            if lst(i) < lst(i+1):
                lst(i + 1), lst(i) = lst(i), lst(i + 1)

    return lst


def fast_sort(lst):
    return (fast_sort([i for i in lst if i < lst[len(lst) // 2]]) + [i for i in lst if i == lst[len(lst) // 2]] + fast_sort([i for i in lst if i > lst[len(lst) // 2]])) if len(lst) > 1 else lst

#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
print("\nЗадача 1")




#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
print("\nЗадача 2")


#3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
print("\nЗадача 3")

lst = [random.randint(0, 100) for i in range(21)]

for j in lst:
    if len([i for i in lst if i >= j]) == len([i for i in lst if i <= j]):
        break
print("Исходный массив: ", lst)
print("Медиана массива: ", j)
print("Cортированный массив для проверки:", sorted(lst))

