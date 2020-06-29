def our_summ():
    with open('task3.txt', 'r', encoding='UTF-8') as my_file:
        my_summ = 0
        i = 0
        for itm in my_file:
            a = itm.split(' ')
            my_summ += int(a[1])
            i +=1
        return my_summ / i

with open('task3.txt', 'r', encoding='UTF-8') as my_file:
    for itm in my_file:
        a = itm.split(' ')
        if int(a[1]) < 20000:
            print(a[0])

print(f'Средня зп: {round(our_summ(), 2)} руб.')



