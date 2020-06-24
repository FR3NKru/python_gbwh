def my_division (a, b):
        result = a / b
        return result

u_num1 = int(input('Введите делимое: '))
u_num2 = 0
while u_num2 == 0:
    u_num2 = int(input('Введите делитель: '))

print(my_division(u_num1, u_num2))


