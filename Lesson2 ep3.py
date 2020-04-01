#3 Пользователь вводит месяц в виде целого числа от 1 до 1 2. Сообщить к какому времени года
#относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

# через list
m = int(input('Введите целое число от 1 до 12 включительно '))
the_answer = []
if m in [1,2,12]:
    the_answer.append('Зима')
if m in [3,4,5]:
    the_answer.append('Весна')
if m in [6,7,8]:
    the_answer.append('Лето')
if m in [9,10,11]:
    the_answer.append('Осень')
print('Этот сезон - ', the_answer)

# через Dict
number_month = int(input('Введите целое число от 1 до 12 включительно '))
seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

for key in seasons.keys():
    if number_month in seasons[key]:
        print('Этот сезон: ', key)

