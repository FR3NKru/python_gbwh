def int_func(text):
    char = text[0].upper()
    return f'{char}{text[1:]}'

data = input('Введите слово латиницей, маленькими буквами: ')
data_list = 'hello how are you'
a = data_list.split(' ')

print(int_func(data))

for itm in a:
    print(int_func(itm), end=' ')
