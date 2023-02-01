"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

while True:
    try:
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
        num3 = float(input('Введите третье число: '))
        break
    except ValueError:
        print('Введены некорректные данные!')


def func_sum1(a1, a2, a3):
    lst = list()
    lst.append(a1)
    lst.append(a2)
    lst.append(a3)
    lst.sort(reverse=True)  # Первые два будут самыми большими, вдруг захотим
    # добавить еще елементов
    return lst[0] + lst[1]


print(f'Решение с функцией sort(): {func_sum1(num1, num2, num3)}')


def func_sum2(a1, a2, a3):
    if a1 <= a2 and a1 <= a3:
        return a2 + a3
    elif a2 <= a1 and a2 <= a3:
        return a1 + a3
    else:
        return a1 + a2


print(f'Решение без функции sort(): {func_sum2(num1, num2, num3)}')
