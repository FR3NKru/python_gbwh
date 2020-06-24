user_number = ''
my_stop = False
my_res = []
total = 0
while my_stop == False:
    user_number = input('Введите числа через пробел: ')
    my_res += user_number.split(' ')
    for i in my_res:
        if i == 'q':
            my_stop = True
        else:
            total += int(i)
            my_res = []
    print(total)
user_number = ''
my_res = []
while True:
    user_number = input('Введите числа через пробел')
    if user_number == 'q':
        break
    my_res.append(user_number)

print(sum(my_res))




