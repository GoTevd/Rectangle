import turtle


class Rectangle():
    # ширина квадрата
    width = 20
    # высота квадрата
    height = 10
    # перерисовать квадрат (метод класса )
    def __init__(self,deminsion1,deminsion2):
         self.height = deminsion1
         self.width = deminsion2

    def __str__(self):
        return "квадрат со сторонами " + str(self.height) + " и " + str(self.width)

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
print(Rect1)

print(Rect2)
print(Rect3)

def draw_rectangle(x, y, width, height):
  turtle.up()
  turtle.goto(x, y)
  turtle.down()
  turtle.forward(width)
  turtle.left(90)
  turtle.forward(height)
  turtle.left(90)
  turtle.forward(width)
  turtle.left(90)
  turtle.forward(height)
  turtle.left(90)


x = print(input("Enter x"))
y = print(input("Enter y"))
width = print(input("Enter width"))
height = print(input("Enter height"))
print(draw_rectangle(x, y, width, height))