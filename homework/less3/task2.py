template_dict = {
        'name': 'имя',
        'surname': 'фамилия',
        'year': 'год рождения',
        'city': 'город',
        'email': 'email',
        'phone': 'номер телефона',
}
user_dict = {}
for key, value in template_dict.items():
    user_dict.update({key: input(f'Введите {value}: ')})

def my_info (name='', surname='',year='', city='', email='', phone=''):
    result = f'Привет, тебя зовут {surname} {name}, ты {year} года рождения, \n' \
             f' живешь в городе {city}, твои контакты: {phone}, {email}'
    return result
print(my_info(**user_dict))