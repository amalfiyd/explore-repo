class Button(object):
    html = ""
    def getHTML(self):
        return self.html

class Image(Button):
    html = "<img></img>"

class Input(Button):
    html = "<input></input>"

class ButtonFactory():
    def createButton(self, typ):
        targetClass = typ.capitalize()
        return globals()[targetClass]()

buttonsObj = ButtonFactory()
temp = ['Image', 'Input']
for b in temp:
    print(buttonsObj.createButton(b).getHTML())