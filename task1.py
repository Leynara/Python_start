#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

task1_list = [ 1, None, 'test', [1, 2], 56.134, True,'seven']
for el in task1_list:
    print(type(el))