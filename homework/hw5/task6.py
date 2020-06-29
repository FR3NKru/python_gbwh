my_dict = {}
with open('task6.txt', 'r', encoding='UTF-8') as my_file:
    for txt in my_file:
        f = txt.split(' ')
        my_dict.update({f[0] : '1'})
        print(my_dict)

"""" Нет понимания как красиво все распаковать """