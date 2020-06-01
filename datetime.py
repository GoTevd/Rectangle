# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# f = int(input())

class Rectangle():
    # ширина квадрата
    width = 20
    # высота квадрата
    height = 10
    # перерисовать квадрат (метод класса )
    # def __init__(self,deminsion1,deminsion2):
    #     self.height = deminsion1
    #     self.width = deminsion2


    def redraw(self,x,y):
        # передаём значения в высоту
        self.height = x
        # инициализируем член класса параметром У
        self.width = y
    def getArea(self):# getter геттер - выдает площадь
        return self.width * self.height

Rect = Rectangle()
print("Rect.height")
print(Rect.height)
print("Rect.width")
print(Rect.width)
print("Rect.getArea()")
print(Rect.getArea())
#здесь состояние (переменной) объекта Rect пользовательского типа Rectangle, было изменено методом redraw()
Rect.redraw(2,3)#здесь состояние объекта REct класса Rectangle, было изменено методом redraw()
print("Rect.height")
print(Rect.height)
print("Rect.width")
print(Rect.width)
print("Rect.getArea()")
print(Rect.getArea())

#создадим новый объект типа квадрат
newRect = Rectangle()
print (newRect.width)
print (newRect.height)
newRect.redraw(99,22)

anotherRect = Rectangle(33,44)
print (newRect.width)
print (newRect.height)
newRect.redraw(99,22)