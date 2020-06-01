# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# f = int(input())
from itertools import product


class Rectangle():
    # ширина квадрата
    width = 20
    # высота квадрата
    height = 10
    # перерисовать квадрат (метод класса )
    def __init__(self,deminsion1,deminsion2):
         self.height = deminsion1
         self.width = deminsion2


    def redraw(self,x,y):
        # передаём значения в высоту
        self.height = x
        # инициализируем член класса параметром У
        self.width = y
    def getArea(self):# getter геттер - выдает площадь
        return self.width * self.height


Rect1=Rectangle(2,3)
Rect2=Rectangle(10,10)
Rect3=Rectangle(99,33)

print(Rect1.height)
print(Rect1.width)