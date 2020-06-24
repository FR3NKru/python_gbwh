while True:
    try:
        a = int(input('Введите целое число: '))
        b = int(input('Введите целое число: '))
        c = int(input('Введите целое число: '))
        break
    except ValueError:
        print('Ошибка! Повторно введите целые числа!')

def max2_number(a: int, b: int ,c: int):
    result = (a + b + c) - min(a, b , c)
    return result

print(max2_number(a, b, c))
