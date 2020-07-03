import time

class TrafficLight:
    __color = ['Зеленый', 'Желтый', 'Красный']
    def running(self, position, toogle):
        self.position = position
        self.toogle = toogle
        start_time = time.time()
        while True:
            time.sleep(0.5)
            timer = time.time()
            if timer > start_time + 7:
                print("Прошло 7 сек")
                break


a = time.time()
b = a + 3
while True:
    time.sleep(0.5)
    a = time.time()
    if a > b:
        print('прошло 3 сек')
        break

print(a)
b = a + 2



    

