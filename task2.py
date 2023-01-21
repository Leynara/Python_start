# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def user_prop(first_name='', last_name='', birth_year='', city='', email='', phone_num=''):

    if first_name:
        print('Имя:', first_name, end = '; ')

    if last_name:
        print('Фамилия:', last_name, end = '; ')

    if birth_year:
        print('Год рождения:', birth_year, end = '; ')

    if city:
        print('Город проживания:', city, end = '; ')

    if email:
        print('e-mail:', email, end = '; ')

    if phone_num:
        print('№ телефона:', phone_num, end = '; ')

    print('\n')

user_prop(first_name = 'Ivan', last_name = 'Ivanov', birth_year = 1995, city='Moscow', email='Ivanov@mail.ru',
          phone_num='89169161616')