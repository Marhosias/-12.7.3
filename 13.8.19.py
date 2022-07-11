S = int(input('Введите количество билетов: '))
Sum_Cost = 0
i = 1
while i < S + 1:
    V = int(input('Введите возраст: '))
    if V < 18:
        Cost = 0
        print('Цена билета: ', Cost)
    elif 18 <= V < 25:
        Cost = 990
        print('Цена билета: ', Cost)
    else:
        Cost = 1390
        print('Цена билета: ', Cost)
    i += 1
    Sum_Cost += Cost
if S > 3:
    Sum_Cost = Sum_Cost - Sum_Cost * 0.1
print('Стоимость заказа: ', Sum_Cost)
