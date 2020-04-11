# 3 Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

# coding: utf-8

with open('salary.txt') as f:
    workers = {}
    for line in f:
        key, value = line.split()
        workers[key] = value
        if float(value) < 20000:
            print(f'{key}: зарплата меньше 20000')

    s_tot = workers.values()
    result = [float(item) for item in s_tot]
#    print(result)
    print(f'Средний доход сотрудников: ', sum(result)/len(result))