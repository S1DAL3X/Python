'''

NAME:           Числа Фибоначчи
AUTHOR:         S1DAL3X
VERSION:        Python v 3.14.2
DATE:           04.02.2026
DESCRIPTION:    None

'''

def fibonacci_numbers(lenght):
    fib_list = list()                                               # создаем список для чисел
    fib_list.append(1)                                              # добавляем первый элемент списка 1
    fib_list.append(1)                                              # добавляем второй элемент списка 1

    n = 2                                                           # n = 2 потому что первые два элемента списка будут одинаковыми (единицы)
    while len(fib_list) < lenght:                                   # пока длина списка Фибоначчи меньше заданной длины выолняем цикл
        i = fib_list[n-2] + fib_list[n-1]                           # вычисление следующего элемента списка
        fib_list.append(i)                                          # добавляем элемент в список
        n += 1                                                      # переходим к следующему элементу в списке (увеличиваем индекс)

    print("Вот " + str(lenght) + " чисел Фибоначчи из списка " + str(fib_list))

fibonacci_numbers(int(input("Введите длину списка Фибоначчи: ")))