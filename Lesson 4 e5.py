#5 Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
#Подсказка: использовать функцию reduce().

from functools import reduce

even_numbers = [n for n in range(99, 1001) if n % 2 == 0]
print(even_numbers)

my_mult = reduce((lambda x, y: x * y), even_numbers)
print(my_mult)