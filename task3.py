# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
# аргументов.

def summ_max(arg_1, arg_2, arg_3):
    arr = [arg_1, arg_2, arg_3]
    a = list(filter(lambda x: x != max(arr), arr))
    return max(arr) + max(a)

print(summ_max(4, 76, 1))


