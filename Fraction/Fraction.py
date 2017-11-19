"""Создать класс Fraction, который должен иметь два поля: числитель a и знаменатель b.
Оба поля должны быть типа int.
Реализовать методы: сокращение дробей, сравнение, сложение и умножение.
"""


def find_nod(n, d):
    while d:
        n, d = d, n % d
    return n


class Fraction:

    def __init__(self, a=1, b=1):
        if a is int:
            self.num = a
        else:
            raise TypeError('numerator is not int')
        if b is int:
            self.den = b
        else:
            raise TypeError('denominator is not int')

    @staticmethod
    def make_common_den(first, second):
        common_nod = find_nod(first.den, second.den)
        second_multi = first.den / common_nod
        first_multi = second.den / common_nod
        new_first_den = int(first.den * first_multi)
        new_first_num = int(first.num * first_multi)
        new_second_den = int(second.den * second_multi)
        new_second_num = int(second.num * second_multi)
        new_first_fraction = Fraction(new_first_num, new_first_den)
        new_second_fraction = Fraction(new_second_num, new_second_den)
        return new_first_fraction, new_second_fraction

    def reducing(self):
        common_nod = find_nod(self.num, self.den)
        self.num = int(self.num / common_nod)
        self.den = int(self.den / common_nod)

    def compare(self, other):
        new_self, new_other = self.make_common_den(self, other)
        if new_self.num > new_other.num:
            s = ">"
        if new_self.num == new_other.num:
            s = "="
        if new_self.num < new_other.num:
            s = "<"
        print('{} {} {}'.format(self, s, other))

    def __add__(self, other):
        new_self, new_other = self.make_common_den(self, other)
        new_num = new_self.num + new_other.num
        new_fraction = Fraction(new_num, new_self.den)
        return new_fraction

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        new_fraction = Fraction(new_num, new_den)
        return new_fraction

    def __str__(self):
        if self.den == 1:
            out = self.num
        else:
            out = '{}/{}'.format(self.num, self.den)
        return out

    def __repr__(self):
        return self.__str__()

    def __call__(self):
        return self.__str__()
