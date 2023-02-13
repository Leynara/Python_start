# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H
# + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def fabric_quantity(self):
        return str(f'Суммарный расход ткани \n'
                   f' {round((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3))}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.fabric_coat = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто {self.fabric_coat}'


class Siut(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.fabric_suit = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм {self.fabric_suit}'

Coat = Coat(56, 166)
Siut = Siut(46, 172)
print(Coat)
print(Siut)
print(Siut.fabric_quantity)