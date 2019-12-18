data_list = []

with open('data.txt', 'r') as f:
    for i in f:
        # print(len(i))
        if len(i) == 19:  # выбираем строку (по длинне) с обьемом заявки
            j = i.replace('\n', '')
            data_list.append(j.split())

print(f'{data_list[0:3]= }')  # Смотрим результат в срезе от 0-го до 3-го ел-та
sorted_list = [sorted(i) for i in data_list]  # Новый с-ок с доваблением в него отсортировонных ел-в из с-ка "data_list"
print(f'{sorted_list[0:3]= }')  # Смотрим результат в срезе

