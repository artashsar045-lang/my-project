# 1. Գրել Animal ծնող class՝ eat() և sleep() մեթոդներով:
#    - Այս մեթոդներից յուրաքանչյուրը պետք է վերադարձնի համապատասխան հաղորդագրություն, երբ կանչ է արվում։
#    - eat()-ը պետք է վերադարձնի "Animal is eating..." հաղորդագրությունը
#    - sleep()-ը պետք է վերադարձնի "Animal is sleeping..." հաղորդագրությունը
#    Ծրագիրը պետք է ներառի նաև երկու ժառանգ class-ներ, որոնք ժառանգում են Animal class-ը՝ Bird և Fish:
#    Այս class-ները Animal class-ից պետք է ժառանգեն sleep() մեթոդը, բայց նաև պետք է ներառեն իրենց մեթոդները՝ ներկայացնելու համար կենդանիներին բնորոշ վարքագիծը:
#    - Bird class-ում, փոփոխեք eat() մեթոդը՝ "Bird is pecking at its food..." հաղորդագրությունը վերադարձնելու համար։
#    - Բացի այդ, ներառեք fly() մեթոդը, որը վերադարձնում է "Bird is flying..." հաղորդագրությունը:
#    - Fish class-ում ներառեք swim() մեթոդը, որը վերադարձնում է "Fish is swimming..." հաղորդագրությունը:
#
# class Animal:
#
#     def eat(self):
#         return "Animal is eating..."
#
#     def sleep(self):
#         return "Animal is sleeping"
#
# class Bird(Animal):
#     def eat(self):
#         return "Bird is pecking at its food..."
#     def fly(self):
#         return "Bird is flying"
#
#
# class Fish(Animal):
#     def swim(self):
#         return "Fish is swimming..."

#
# a = Animal()
# b = Bird()
# f = Fish()
# print(b.eat())
# print(b.fly())
# print(f.swim())


"""
2․ Գրել Shape abstract class, որը․
   - կունենա __init__(), perimetr(), area() աբստրակտ մեթոդներ։
   Գրել Circle class, որը կժառանգի Shape class-ից, որը․
   - __init__() -ում կընդունի շրջանագծի շառավիղը,
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտը ճիշտ մուտքագրված լինի (պետք է լինի դրական թիվ),
   - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները շրջանագծի համար։
   Գրել Rectangle class, որը կժառանգի Shape class-ից, որը․
   - __init__() -ում կընդունի ուղղանկյան լայնությունը և երկարությունը,
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն (պետք է լինեն դրական թվեր),
   - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները ուղղանկյան համար։
   Գրել Triangle class, որը կժառանգի Shape class-ից, որը․
   - __init__() -ում կընդունի 
     -- կամ եռանկյան երեք կողմերը,
     -- կամ մեկ կողմը և բարձրությունը,
     -- կամ երկու կողմերը և այդ կողմերի կազմած անկյունը, 
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն,
   - կվերախմբագրի Shape class-ի perimetr() մեթոդը եռանկյան համար,
   - եռանկյան մակերեսը կհաշվի 3 տարբերակով, կախված մուտքագրված պարամետրերից․
     1) S = (p * (p - a) * (p - b) * (p - c)) ^ 0.5   , որտեղ a, b, c - եռանկյան կողմերն են, p - եռանկյան կիսապարագիծը,
     2) S = a * h / 2                                 , որտեղ a - եռանկյան կողմը, h = եռանկյան բարձրությունը,
     3) S = a * b * sin(alpha) / 2                    , որտեղ a, b - եռանկյան կողմերն են, alpha - եռանկյան a և b կողմերի կազմած անկյունը։"""
import math
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def perimetr(self):
        ...
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        if radius < 0:
            return False
        True
    def perimetr(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self,width,length):
        self.width = width
        self.length = length
        if width < 0 or length < 0:
            return False
        True

    def perimetr(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, a , b , c , h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        if a < 0 or b < a or c < b:
            return False

    def perimetr(self):
        if self.a and self.b and self.c:
            return self.a + self.b + self.c
        else:
            return False

    def area(self):
        if self.a and self.b and self.c:
            p = (self.a + self.b + self.c) / 2
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        else:
            return  self.a * self.h / 2




c = Circle(5)
print(c.area())
print(c.perimetr())

r = Rectangle(3, 4)
print(r.area())
print(r.perimetr())

t1 = Triangle(3, 4, 5 , 8)
print(t1.area())
print(t1.perimetr())

