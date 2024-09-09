#6.	Создать множество из 5 разных чисел, затем добавить в него новое число и вывести на экран
spis = []
for i in range(5):
    print('Vvedite ', i+1, ' element')
    spis.append(input())
print(spis)