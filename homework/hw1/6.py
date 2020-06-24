start = int(input("Сколько вы пробежали за 1 день?: "))
finish = int(input("Сколько хотите пробежать?: "))
day = 0
result = 0

while True:
    if result < finish:
        result = result + (start * 1.1)
        day += 1
    else:
        print(f'На {day} день, вы сможете пробежать не менее: {int(result)} киллометров')
        break




