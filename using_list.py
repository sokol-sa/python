#!/usr/bin/env python3
shoplist=['яблоки', 'манго', 'морковь', 'бананы']

print('Мне нужно ', len(shoplist), 'покупок')

print('Покупки', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nЕще риса')
shoplist.append('рис')
print('Теперь список такой', shoplist)

print('Сортировка:')
shoplist.sort()
print('Отсортированный список', shoplist)

print('Первая покупка', shoplist[0])
olditem=shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь список такой', shoplist)
