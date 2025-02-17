#1
class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def square(self):
        print(f"Площадь {self.height * self.width}")

    def perimeter(self):
        print(f"Периметр {self.height * 2 + self.width * 2}")

a = Rectangle(3, 4)
b = Rectangle(10, 12)
c = Rectangle(7, 7)

a.square()
a.perimeter()

b.square()
b.perimeter()

c.square()
c.perimeter()


#2
print("\n")
class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(f'Сложение {self.a + self.b}')

    def multiplication(self):
        print(f'Умножение {self.a * self.b}')

    def division(self):
        print(f'Деление {self.a / self.b}')

    def subtraction(self):
        print(f'Вычитание  {self.a - self.b}')

calc = Math(2, 5)
calc.addition()
calc.multiplication()
calc.division()
calc.subtraction()


#3
print("\n")
class Button:

    type: str = "Кнопка"

    def __init__(self, text, loc = None):
        self.text  = text
        self.loc = loc

    def clicked(self):
        print(f'Клик по кнопке {self.text}')

textBox = Button("Text Box")
checkBox = Button("Check Box")
radioButton = Button("Radio Button")

print(textBox.text)
textBox.clicked()

print(checkBox.text)
checkBox.clicked()

print(radioButton.text)
radioButton.clicked()


#4
print("\n")
