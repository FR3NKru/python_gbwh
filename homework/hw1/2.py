
user_time_sec = input('Введите время в секундах: ')
user_time_sec = int(user_time_sec)
time_hour = user_time_sec / 60 // 60
time_hour = int(time_hour)
user_time_sec = user_time_sec - (time_hour *60*60)
time_min = user_time_sec // 60
time_min = int(time_min)
user_time_sec = user_time_sec - (time_min * 60)
time_sec = int(user_time_sec)
print(f'{time_hour}:{time_min}:{time_sec}')