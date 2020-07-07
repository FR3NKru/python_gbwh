en_ru = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре',}

with open('task4.txt', 'r', encoding='UTF-8') as my_file:
    with open('task4_new.txt', 'w', encoding='UTF-8') as my_file_new:
        for i in my_file:
            en = i.split(' ')
            ru = en_ru.get(en[0])
            my_file_new.write(f'{ru} {en[1]} {en[2]}')
