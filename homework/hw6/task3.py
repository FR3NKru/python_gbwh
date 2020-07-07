class Worker:
    def __init__(self, name, surname, position, wage, bonus, prpr):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': int(wage), 'bonus': int(bonus)}
        self.__prpr = prpr

class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname
    def get_total_income(self):
        return self._Worker__income['wage'] + self._Worker__income['bonus']

b = Position('Виталий', 'Подвысоцкий', 'Директор', '150000', '100000', 'prpr')

print(b.get_full_name())
print(b.get_total_income())
