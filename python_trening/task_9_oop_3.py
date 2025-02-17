class Soda:

    def __init__(self, ingregient = ""):
        self.ingredient = ingregient

    def show_my_drink(self):
        if self.ingredient != "" :
            print("Газировка и " + self.ingredient)
        else:
            print("Обычная газировка")

withIngredient = Soda("Сахар")
withoutIngredient = Soda()

withIngredient.show_my_drink()
withoutIngredient.show_my_drink()
