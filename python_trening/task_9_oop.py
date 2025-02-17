class Button:

    def __init__(self, text, link):
        self.text = text
        self.link = link

home = Button("домой", "/home")
catalog_msk= Button("каталог", "/msk/katalog")

print(home.text)
print("кнопка " + home.text + " имеет сслку " + home.link)

print("\n")

print(catalog_msk.text)
print("кнопка " + catalog_msk.text + " имеет сслку " + catalog_msk.link)
