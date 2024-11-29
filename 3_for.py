"""

Домашнее задание №3

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

import numpy as np

def main():
    phones_sales = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    sum_each_phone_sales_onelinter = [{v['product']: sum(v['items_sold'])} for v in phones_sales]
    
    sum_each_phone_sales = []
    sum_val = 0
    for v in phones_sales:
        for s in v['items_sold']:
            sum_val += s
        sum_each_phone_sales.append({v['product']: sum_val})
        sum_val = 0
    
    print(f"{sum_each_phone_sales_onelinter=}")
    print(f"{sum_each_phone_sales=}")
    print()
    
    avg_each_phone_sales_onelinter = [{v['product']: float(round(np.mean(v['items_sold']), 2))} for v in phones_sales]

    avg_each_phone_sales = []
    for v in phones_sales:
        avg_each_phone_sales.append({v['product']: float(round(np.mean(v['items_sold']), 2))})
    
    print(f"{avg_each_phone_sales_onelinter=}")
    print(f"{avg_each_phone_sales=}")
    print()
    
    sum_all_phones_sales_onelinter = sum([sum(v['items_sold']) for v in phones_sales])

    sum_all_phones_sales = 0
    for phones_sale in phones_sales:
        for v in phones_sale['items_sold']:
            sum_all_phones_sales += v
    
    print(f"{sum_all_phones_sales_onelinter=}")
    print(f"{sum_all_phones_sales=}")
    print()
    
    avg_all_phones_sales_onelinter = round(np.mean([v['items_sold'] for v in phones_sales]), 2)

    all_phones_sales = []
    for v in phones_sales:
        all_phones_sales.append(v['items_sold'])
    avg_all_phones_sales = round(np.mean(all_phones_sales), 2)
    
    print(f"{avg_all_phones_sales_onelinter=}")
    print(f"{avg_all_phones_sales=}")
    print()
    
if __name__ == "__main__":
    main()






