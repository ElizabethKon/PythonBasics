#2  Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_adress_book(name='Name', surname='Surname', year_of_birth='Year', city='City', e_mail='Mail', phone_number='Number'):
     return print(f'Имя: {name} Фамилия: {surname} Год рождения: {year_of_birth}' f'Город проживания: {city} '
                  f'E-mail: {e_mail} Телефон: {phone_number}')
#   return print(name, surname, year_of_birth, city, e_mail, phone_number)
my_adress_book(
    name=input('Имя: '),
    surname=input('Фамилия: '),
    year_of_birth=input('Год Рождения: '),
    city=input('Город проживания: '),
    e_mail=input('e-mail: '),
    phone_number=input('Телефон: '),
)

