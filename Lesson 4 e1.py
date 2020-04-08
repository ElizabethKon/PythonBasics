#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
#платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
#час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
#скрипт с параметрами.

from sys import argv

output, rate_hour, bonus = argv
print("Выработка в часах: ", output)
print("Ставка в час: ", rate_hour)
print("Премия: ", bonus)

output = int(output)
rate_hour = int(rate_hour)
bonus = int(bonus)

print(output * rate_hour + bonus)

# у меня ничего не получилось
# я через командную строку вызывала, например
# python Lesson4e1 7 2 5
# и всегда была ошибка ValueError: too many values to unpack: (expected 3)
# в общем я понимаю, что не понимаю.


