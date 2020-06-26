from sys import argv


_, hour, range_in_hour, bonus = argv
hour = int(hour)
range_in_hour = int(range_in_hour)
bonus = int(bonus)

result = (hour * range_in_hour) + bonus
print(f'Ваша зп (включая премию): {result}')

