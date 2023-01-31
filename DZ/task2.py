"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

first_name = input('Введите имя: ')
second_name = input('Введите фамилию: ')
year_of_birth = int(input('Введите год рождения: '))
place_to_live = input('Введите город проживания: ')
e_mail = input('Введите e-mail: ')
phone = input('Введите телефон: ')


def func_output(param1, param2, param3, param4, param5, param6):
    print(
        f'{param1} {param2} {param3} года рождения, проживает в городе '
        f'{param4},\n email: {param5}, телефон: {param6}')

func_output(first_name, second_name, year_of_birth, place_to_live, e_mail,
            phone)
