data_list = []

with open('Text.txt', 'r') as f:
    for i in f:
        if len(i) == 11:  # выбираем строку (по длинне) с обьемом заявки
            j = i.replace('\n', '')
            data_list.append(j.split())

print(data_list)
