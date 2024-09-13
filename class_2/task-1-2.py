class Title():
    def __init__(self, text, x, y, visibility = True):
        self.text = text
        self.x = x
        self.y = y
        self.visibility = visibility

    def print_info(self):
        print("===========================")
        print("Інформація про напис:")
        print("Текст:", self.text)
        print("Координати: (", self.x, ",", self.y, ")")
        print("Видимість", self.visibility)
        print("===========================")

    def hide(self):
        self.visibility = False
        print(self.text, "- приховано")

    def show(self):
        self.visibility = True
        print(self.text, "- відображається")


t1 = Title("Дізнатися переможця прямо зараз!", 150, 50)
t2 = Title("Переможець може бути тільки один", 150, -100)

t1.print_info()
t2.print_info()

t2.hide()
t2.print_info()
