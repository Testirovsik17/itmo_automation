from task_9_checks import Checks

class Input(Checks):
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

class Button(Checks):
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

class Title(Checks):
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

class Link(Checks):
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search = Input("inputLoc", "inputText")
print(search.check_text())
print(search.text)

butoon_Obj = Button("buttonLoc", "buttonText")
print(butoon_Obj.check_text())
print(butoon_Obj.text)

title_Obj = Title("titleLoc", "titleText")
print(title_Obj.check_text())
print(title_Obj.text)

link_Obj = Link("linkLoc", "linkText")
print(link_Obj.check_text())
print(link_Obj.text)
