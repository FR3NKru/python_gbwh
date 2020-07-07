from random import randint
numbers = randint(3, 10)
my_sum = 0

with open('task5.txt', 'w', encoding='UTF-8') as my_file:
    for i in range(numbers):
        i = randint(1, 100)
        my_file.write(f'{i} ')

with open('task5.txt', 'r', encoding='UTF-8') as my_file_sum:
    for itm in my_file_sum:
        my_list = itm.split(' ')
        for i in my_list:
            if i.isdigit() == True:
                x = int(i)
                my_sum += x

print(my_sum)


