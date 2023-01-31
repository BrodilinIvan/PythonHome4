"""
5. Сделайте профилирование кода любого или любых выполненных заданий
с помощью модуля timeit, опишите результат
"""

import timeit

def func1(a, b):
    print(f'Через выражение **: {a ** b}')

def func2(a, b):
    print(f'Через встроенную функцию pow: {pow(a, b)}')

print('Через функции:')

start_time = timeit.default_timer()
func1(20, 5)
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
func2(20, 5)
print(timeit.default_timer() - start_time)

print('Без функций:')

start_time = timeit.default_timer()
print(f'Через выражение **: {20 ** 5}')
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
print(f'Через встроенную функцию pow: {pow(20, 5)}')
print(timeit.default_timer() - start_time)

"""
Расчеты показали, что разница по времени несущественная если стоит выбор 
использования вычисления в формате x ** y или pow(x, y), а использование 
функций при данных вычислениях снижает время многократно!
"""