import pandas as pd

data = pd.read_csv('./uchebnaya_gruppa.csv', delimiter=";")
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
print(data)
print('---------------------------------------------------------------------------------------------------------------')

max_vozrast = list(map(int, data['Дата рождения'][0].split('.')))
for i in range(1, len(data)):
    a = list(map(int, data['Дата рождения'][i].split('.')))
    if a[2] < max_vozrast[2]:
        max_vozrast = a
    elif a[2] == max_vozrast[2]:
        if a[1] < max_vozrast[1]:
            max_vozrast = a
        elif a[1] == max_vozrast[1]:
            if a[0] < max_vozrast[0]:
                max_vozrast = a
            elif a[0] == max_vozrast[0]:
                print("Присутствуют люди с одинаковой датой рождения!")
                max_vozrast = a
max_vozrast = list(map(str, max_vozrast))
if len(max_vozrast[0]) < 2:
    max_vozrast[0] = '0' + max_vozrast[0]
if len(max_vozrast[1]) < 2:
    max_vozrast[1] = '0' + max_vozrast[1]
max_vozrast = '.'.join(max_vozrast)
print("Дата рождения самого старшего студента:", max_vozrast)
print("ФИО самого старшего студента:", data['ФИО студента'][data[data['Дата рождения'] == max_vozrast].index].tolist())
print('---------------------------------------------------------------------------------------------------------------')

max_vozrast = list(map(int, data['Дата рождения'][0].split('.')))
for i in range(1, len(data)):
    a = list(map(int, data['Дата рождения'][i].split('.')))
    if a[2] > max_vozrast[2]:
        max_vozrast = a
    elif a[2] == max_vozrast[2]:
        if a[1] > max_vozrast[1]:
            max_vozrast = a
        elif a[1] == max_vozrast[1]:
            if a[0] > max_vozrast[0]:
                max_vozrast = a
            elif a[0] == max_vozrast[0]:
                print("Присутствуют люди с одинаковой датой рождения!")
                max_vozrast = a
max_vozrast = list(map(str, max_vozrast))
if len(max_vozrast[0]) < 2:
    max_vozrast[0] = '0' + max_vozrast[0]
if len(max_vozrast[1]) < 2:
    max_vozrast[1] = '0' + max_vozrast[1]
max_vozrast = '.'.join(max_vozrast)
print("Дата рождения самого младшего студента:", max_vozrast)
print("ФИО самого младшего студента:", data['ФИО студента'][data[data['Дата рождения'] == max_vozrast].index].tolist())