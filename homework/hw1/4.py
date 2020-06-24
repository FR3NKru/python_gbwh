user_number = (input('Введите целое, положительно число: '))
i = 0
max_number = 0
while i < len(user_number):
    a = int(user_number[i])
    if max_number < a:
        max_number = a
    i = i + 1
print(max_number)



