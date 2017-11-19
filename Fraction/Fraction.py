"""Создать класс Fraction, который должен иметь два поля: числитель a и знаменатель b.
Оба поля должны быть типа int.
Реализовать методы: сокращение дробей, сравнение, сложение и умножение.
"""


def find_nod(n, d):

    """find highest common divisor"""

    while d:
        n, d = d, n % d
    return n


def make_common_den(first, second):

    """make new two fractions with a common denominator"""

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


class Fraction:

    def __init__(self, a=1, b=1):

        """initialize a two variables: num (numerator) and den (denominator);
        if denominator have a negative value then minus is assigned to the numerator;
        if numerator or denominator are empty then they equal to 1;
        numerator and denominator can't be zero
        accept only int;
        """

        if a != 0 and b != 0:
            if type(a) is int:
                self.num = a
            else:
                raise TypeError('numerator is not int')
            if type(b) is int:
                if b < 0:
                    self.den = -b
                    self.num = -self.num
                else:
                    self.den = b
            else:
                raise TypeError('denominator is not int')
        else:
            raise ZeroDivisionError

    def reducing(self):

        """reduces numerator and denominator
        (if they have greatest common divisor)
        """

        common_nod = find_nod(self.num, self.den)
        self.num = int(self.num / common_nod)
        self.den = int(self.den / common_nod)

    def compare(self, other):

        """displays two fractions with sign comparison between them"""

        new_self, new_other = make_common_den(self, other)
        if new_self.num > new_other.num:
            sign = ">"
        if new_self.num == new_other.num:
            sign = "="
        if new_self.num < new_other.num:
            sign = "<"
        print('{} {} {}'.format(self, sign, other))

    def __add__(self, other):

        """overloads the addition operator"""

        new_self, new_other = make_common_den(self, other)
        new_num = new_self.num + new_other.num
        new_fraction = Fraction(new_num, new_self.den)
        new_fraction.reducing()
        return new_fraction

    def __mul__(self, other):

        """overloads the multiplication operator"""

        other_fraction = Fraction(other)
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        new_fraction = Fraction(new_num, new_den)
        new_fraction.reducing()
        return new_fraction

    def __str__(self):

        """output to the screen numerator and denominator separated by a slash;
        if denominator equals 1 then output without denominator and slash"""

        if self.den == 1:
            out = str(self.num)
        else:
            out = '{}/{}'.format(self.num, self.den)
        return out

    def __repr__(self):
        return self.__str__()

    def __call__(self):
        return self.__str__()
