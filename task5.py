# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить её на экран.

def rewrite_file():
    try:
        with open('user_data.txt', 'r+') as file:
            l = map(int, file.read().split())
            print(sum(l))
    except FileNotFoundError:
        return 'Файл не найден.'

rewrite_file()
