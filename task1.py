# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных будет свидетельствовать пустая строка.
with open('user_data.txt', 'a') as file:
    while True:
        user_data = input('Данные: ')
        file.write(user_data + '\n')
        if not user_data:
            break