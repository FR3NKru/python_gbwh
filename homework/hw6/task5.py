class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки РУЧКОЙ')
class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки КАРАНДАШЕМ')
class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки МАРКЕРОМ')

a = Stationery('Рука')
b = Pen('Ручка')
c = Pencil('Карандащ')
d = Handle('Маркер')

a.draw()
b.draw()
c.draw()
d.draw()