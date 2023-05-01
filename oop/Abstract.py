from time import localtime

print('# class vs static methods')
class Date:
    def __init__(self,
                year: int,
                month: int,
                day: int) -> None:
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self) -> str:
        return f'{self.day}.{self.month}.{self.year}'

    def print_date(self) -> None:
        print(self)

    @classmethod
    def get_todays_date(cls):
        date = cls.__new__(cls)
        time = localtime()
        date.year = time.tm_year
        date.month = time.tm_mon
        date.day = time.tm_mday
        return date

    @staticmethod
    def is_todays_date(date) -> bool:
        time = localtime()
        return date.year == time.tm_year \
               and date.month == time.tm_mon \
               and date.day == time.tm_mday

date = Date(2023, 4, 22)
print(date)
print(Date.is_todays_date(date))

date2 = Date.get_todays_date()
print(date2)
print(Date.is_todays_date(date2))

print('\n\n# abstract class and methods')
import abc
import math

class Base(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def m1(self):
        return

    @staticmethod
    @abc.abstractmethod
    def m2(self):
        return

    @classmethod
    @abc.abstractmethod
    def m3(self):
        return

class MyClass(Base):
    def m1(self):
        return

    def m2(self):
        return

    def m3(self):
        return

try:
    b = Base()
except Exception as e:
    print(f'Error: {e}')

m = MyClass()
m.m2()


