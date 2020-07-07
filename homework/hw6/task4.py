class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'Машина {self.name} поехала!')
    def stop(self):
        print(f'Машина {self.name} остановилась!')
    def turn(self, direction):
        print(f'Машина {self.name} повернула на {direction}!')
    def show_speed(self):
        return print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Машина {self.name} скорость {self.speed}')
            print(f'Машина {self.name} привысила скорость 60 км/час!')
        else:
            print(f'Машина {self.name} скорость {self.speed}')
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Машина {self.name} скорость {self.speed}')
            print(f'Машина {self.name} привысила скорость 40 км/час!')
        else:
            print(f'Машина {self.name} скорость {self.speed}')

class SportCar(Car):
    pass
class PoliceCar(Car):
    pass

car1 = TownCar(70, 'green', 'Ford', False)
car2 = WorkCar(70, 'white', 'Toyota', False)
car3 = SportCar(180, 'red', 'Ferarri', False)
car4 = TownCar(50, 'black', 'Shkoda', False)
pol111 = PoliceCar(150, 'blue', 'Opel', True)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)
print(car4.__dict__)
print(pol111.__dict__)

car1.show_speed()
car2.show_speed()
car3.go()
car4.stop()
pol111.turn('лево')