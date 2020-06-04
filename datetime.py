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


Rect1=Rectangle(200,300)
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



x = 10
y = 30
width = Rect1.width
height = Rect1.height
print(draw_rectangle(x, y, width, height))

x = 2
y = 5
width = Rect2.width
height = Rect2.height
print(draw_rectangle(x, y, width, height))

x = 2
y = 5
width = Rect3.width
height = Rect3.height
print(draw_rectangle(x, y, width, height))

turtle.done()