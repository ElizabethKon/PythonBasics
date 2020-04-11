#1 Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

file_name = input('Название файла: ')
my_file = open(file_name,'w')
while True:
    stroke = input('Введите данные : ')
    if stroke == '': break
    my_file.write(stroke+'\n')
my_file.close()