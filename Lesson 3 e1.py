#1 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_division(x,y):
    try:
        return x/y
    except ZeroDivisionError as e:
        print(f'Не стоит делить на ноль!')
print(my_division(int(input('Введите делимое: ')), int(input('Введите делитель: '))))

