"""
5. Сделайте профилирование кода любого или любых выполненных заданий
с помощью модуля timeit, опишите результат
"""

from timeit import timeit


def func1(a, b):
    return a ** b


def func2(a, b):
    return pow(a, b)


x1 = lambda a, b: a ** b
x2 = lambda a, b: pow(a, b)

def func_pow(a, b):
    i = 1
    while i < b:
        if b == 1:
            break
        else:
            a *= a
        i += 1
    return a

print('Через именные функции:')

print(timeit("func1(20, 5)", setup="from __main__ import func1", number=10000))
print(timeit("func2(20, 5)", setup="from __main__ import func2", number=10000))

print('Через анонимные функции')

print(timeit("x1(20, 5)", setup="from __main__ import x1", number=10000))
print(timeit("x2(20, 5)", setup="from __main__ import x2", number=10000))

print('Через встроенные функций:')

print(timeit('20 ** 5', number=10000))
print(timeit('pow(20, 5)', number=10000))

print('Через цикл:')

print(timeit("func_pow(20, 5)",
             setup="from __main__ import func_pow", number=10000))

"""
Расчеты показали, что использование функций при данных вычислениях снижает 
время многократно!
"""
