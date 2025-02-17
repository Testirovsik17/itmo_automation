class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def car_start(self):
        print("Автомобиль заведен")

    def car_stop(self):
        print("Автомобиль заглушен")

    def car_year(self):
        print(f"Год выпуска {self.year}")

    def car_type(self):
        print(f"Тип {self.type}")

    def car_color(self):
        print(f"Цвет {self.color}")

vehicle = Car("Синий", "Пикап", "2004")
vehicle.car_start()
vehicle.car_stop()
vehicle.car_year()
vehicle.car_type()
vehicle.car_color()

