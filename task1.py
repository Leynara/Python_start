#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    day_month_year = "10-12-2022"

    @classmethod
    def to_split(cls):
        parts = cls.day_month_year.split("-")
        cls.day = int(parts[0])
        cls.month = int(parts[1])
        cls.year = int(parts[2])

    @staticmethod
    def validate_date():

        Date.to_split()
        if Date.year < 1950 or Date.year > 2023:
            raise ValueError(f"Некорректный год")
        if Date.month < 1 or Date.month > 12:
            raise ValueError(f"Некорректный месяц")
        if Date.day < 1 or Date.day > 31:
            raise ValueError(f"Некорректный день")

print(f"{Date.day_month_year}")

Date.day_month_year = "10-13-2022"
print(f"{Date.day_month_year} - ", end='')
try:
    Date.validate_date()
except ValueError as e:
    print(f"Ошибка формата данных! {e.args[0]}")
