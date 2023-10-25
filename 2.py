'''
Создать текстовый файл (не программно).
Построчно записать названия детских товаров и их
стоимость (не менее 10 строк). Вывести на экран все товары,
стоимость которых ниже 10 рублей. Вывести на экран все товары
с минимальной стоимостью.
Пример файла:
Машинка  50
Кукла  40
'''
with open("tovar.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
less_than_10 = []
min_price = float("inf")
min_price_items = []
for line in lines:
    name, price = line.split()
    price = float(price)
    if price < 10:
        less_than_10.append(name)
        if price < min_price:
            min_price = price
            min_price_items = [name]
        elif price == min_price:
            min_price_items.append(name)
print("Товары с ценой ниже 10 рублей:")
for item in less_than_10:
    print(item)
print("Товары с минимальной стоимостью:")
for item in min_price_items:
    print(item)