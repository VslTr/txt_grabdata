import logging
import os


os . chdir ( os . path . dirname ( __file__ ))


def log(l):
    logging.basicConfig(level=logging.INFO, filename='script.log', filemode='a', 
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.info(l)


def to_list(file):
    log('run def tp_list')
    with open(file, 'r') as f:
        tmp_list = []
        for i in f:
            # print(len(i))
            if len(i) == 19:  # выбираем строку (по длинне) с обьемом заявки
                j = i.replace('\n', '')
                tmp_list.append(j.split())
        return tmp_list       


def to_sort(tmp_list):
    log('run def to_sort')
    return [sorted(i) for i in tmp_list if len(i) == 6]


def to_int(x):
    log('run def to_int')
    for i in x:
            for j in range (len(i)): i[j] = int(i[j])
    return x

def to_dublicate(tmp_list):
    log('run def to_dublicate')
    return [sorted(set(tmp_list[i])) for i in range(len(tmp_list))] # set() множество, удалит дубликаты.


# print(f'{data_list[0:3]= })
# print(len(data_list[0])) 
  
data_list = to_list('data.txt')
sorted_list = to_sort(data_list) # Новый с-ок с доваблением в него отсортировонных ел-в из с-ка "data_list"
sorted_list = to_int(sorted_list) # Переводим из строк в числа
log(sorted_list[0:5])

for i in sorted_list[0:10]: print(f'index: {sorted_list.index(i)} -> {i}')
print()

# dublicate = to_dublicate(sorted_list) # вызов ф-ии удаляющей дубликаты
