import time

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
         start_time = time.time()
         position = 0
         while True:
            time.sleep(1)
            timer = time.time()
            print(self.__color[position])
            if timer > start_time + 7 and position==0:
               position = 1
               print(self.__color[position])
            if timer > start_time + 9 and position==1:
                position = 2
                print(self.__color[position])
            if timer > start_time + 16 and position==2:
               position = 0
               print(self.__color[position])
               start_time = time.time()
               continue

a = TrafficLight()
a.running()
