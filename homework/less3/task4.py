usr_num1, usr_num2 = 0, 0
while True:
    try:
        usr_num1 = int(input('Введите целое, положительное число: '))
    except ValueError:
        continue
    try:
        usr_num2 = int(input('Введите целое, отрицательное число: '))
        if usr_num2 >= 0:
            print('Прочитайте условия, повторите ввод!')
            continue
        break
    except ValueError:
        continue


def my_pow(a: int, b: int):
    return a ** b

def my_pow2(a: int, b: int):
    result = 0
    for itm in range(b * -1):
        sum = a * a
        result = result + sum
    return 1 / result

print(my_pow(usr_num1, usr_num2))
print(my_pow2(usr_num1, usr_num2))


