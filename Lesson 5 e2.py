#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

#with open('234.txt','a') as my_file
my_file = open('234.txt','w')
while True:
    stroke = input('Введите данные : ')
    if stroke == '': break
    my_file.write(stroke+'\n')
my_file.close()

with open("234.txt", "r") as f:
 i=0
 for line in f:
    i
    i+=1
 print(i)

