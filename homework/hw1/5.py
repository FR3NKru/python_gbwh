proceeds = int(input('Введчите выручку предприятия: '))
outlay = int(input('Введчите расходы предприятия: '))
if proceeds > outlay:
    print('Ваша фирма работает в прибыль')
    profitability = (proceeds-outlay)/proceeds
    print('Рентабельность фирмы: ', profitability)
    employees = int(input('Введите численность сотрудников фирмы: '))
    profit = (proceeds - outlay) / employees
    print(f'Прибыль на одного сотрудника: {profit}')
elif proceeds < outlay:
    print('Ваша фирма работает в убыток')
else:
    print('Ваша фирма работает в НОЛЬ!')

