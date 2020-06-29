with open('text.txt', 'w', encoding='UTF-8') as my_file:
    while True:
        my_text = input('Введите текст')
        if my_text == '':
            break
        else:
            my_file.write(f'{my_text} \n')