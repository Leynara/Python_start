# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10
# строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт
# средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

def workers_statistics():
    try:
        with open('user_data.txt', 'r+', encoding="utf-8") as file:
            l = file.readlines()
            poor = []
            sum = 0
            for i in range(len(l)):
                salary = int((l[i].split())[1])
                if salary < 20000:
                    poor.append((l[i].split())[0])
                sum += salary
            print(f'Меньше 20 тыс. рублей получает сотрудник: {", ".join(poor)}')
            print(f'Средняя величина дохода сотрудников равна {sum / len(l):.2f}')
    except FileNotFoundError:
        return 'Файл не найден.'

workers_statistics()