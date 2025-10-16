import random
print('Камень бьёт ножницы, ножницы - бумагу, бумага - камень')
a=input('Сделай свой выбор: ')
a=a.lower()
print(a)
ch=['камень', 'ножницы', 'бумага']
comp=random.choice(ch)
print(comp)
if a=='камень' and comp=='камень' or a=='ножницы' and comp=='ножницы' or a=='бумага' and comp=='бумага':
    print('Ничья')
elif a=='камень' and comp=='ножницы' or a=='ножницы' and comp=='бумага' or a=='бумага' and comp=='камень':
    print('Вы победили')
elif a=='ножницы' and comp=='камень' or a=='бумага' and comp=='ножницы' or a=='камень' and comp=='бумага':
    print('Вы проиграли')