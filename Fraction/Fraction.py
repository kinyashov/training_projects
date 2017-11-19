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

    """make new two fractions with the same denominator"""

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

        """Initialize a two variables: num (numerator) and den (denominator).
        If denominator have a negative value then a minus is assigned to the numerator.
        If numerator or denominator are empty then they equal to 1.
        Numerator and denominator can't be zero.

        The first argument can be float (in addition to integer),
        then it will be convert to fraction,
        and the second argument will be ignored.

        The second argument can be only integer.
        """

        if a != 0 and b != 0:
            if type(a) is float:

                # convert float to fraction
                a = str(a)
                i = a.find('.')
                to_point = int(a[:i])
                after_point = int(a[i + 1:])
                self.den = 10 ** len(str(after_point))
                self.num = after_point + self.den * to_point
                self.reducing()
            else:
                if type(a) is int:
                    self.num = a
                else:
                    raise TypeError('numerator is not int or float')
                if type(b) is int:

                    # transfer minus to numerator
                    # if denominator less then zero
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

        if not isinstance(other, Fraction):
            other = Fraction(other)
        new_self, new_other = make_common_den(self, other)
        if new_self.num > new_other.num:
            sign = ">"
        elif new_self.num == new_other.num:
            sign = "="
        else:
            sign = "<"
        print('{} {} {}'.format(self, sign, other))

    def __add__(self, other):

        """It is allowed to multiply integers.
        At the end of the fraction is reduced
        """

        if not isinstance(other, Fraction):
            other = Fraction(other)
        new_self, new_other = make_common_den(self, other)
        new_num = new_self.num + new_other.num
        new_fraction = Fraction(new_num, new_self.den)
        new_fraction.reducing()
        return new_fraction

    def __mul__(self, other):

        """It is allowed to multiply integers.
        At the end of the fraction is reduced
        """

        if not isinstance(other, Fraction):
            other = Fraction(other)
        new_num = self.num * other.num
        new_den = self.den * other.den
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
