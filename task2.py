#2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
# строке.

def count_info():
    try:
        with open('user_data.txt', 'r', encoding="utf-8") as file:
            string = file.readlines()
            for i in range(len(string)):
                word = string[i].split()
                print(f'Количество строк в файле {len(string)}. В {i + 1}-ой строке {len(word)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден.'

count_info()