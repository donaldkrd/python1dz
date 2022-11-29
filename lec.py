# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# n = input('Введите вещественное число: ')
# sum = 0
# for i in n: 
#     if i != '.':
#         sum += int(i)
# print(sum)


# # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# n = int(input('Введите число: '))
# list1 = []
# pr = 1
# for i in range(1, n + 1):
#     pr = pr * i
#     list1.append(pr)
# print(list1)


# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# n = int(input('Введите число: '))
# list1 = []
# zapol = 0 
# for i in range(1, n + 1):
#     zapol = (1 + 1 / i) ** i
#     list1.append(zapol)  
# print(list1) 
# print(sum(list1))


# Реализуйте алгоритм перемешивания списка.
# from random import shuffle
# n = [[i] for i in range(100)]
# shuffle(n)
# print(n)