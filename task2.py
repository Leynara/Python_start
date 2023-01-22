# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

#Вариант 1
task2_list = list(input('Введите значени из списка: ').split())
new_list = []
for i in range(0, len(task2_list), 2):
    next_i = i + 2
    a = task2_list[i:next_i]
    a.reverse()
    new_list.extend(a)
print(f'Обновленный список: {new_list}')

#Вариант 2

task2_list = list(input('Введите значения: ').split())
for i in range(1, len(task2_list), 2):
    task2_list[i-1], task2_list[i] = task2_list[i], task2_list[i-1]
print(f'Обновленный список: {task2_list}')