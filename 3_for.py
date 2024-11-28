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
    sum_each_phone_sales = [{v['product']: sum(v['items_sold'])} for v in phones_sales]
    print(sum_each_phone_sales)
    
    avg_each_phone_sales = [{v['product']: float(round(np.mean(v['items_sold']), 2))} for v in phones_sales]
    print(avg_each_phone_sales)
    
    sum_all_phones_sales = sum([sum(v['items_sold']) for v in phones_sales])
    print(sum_all_phones_sales)
    
    avg_all_phones_sales = round(np.mean([v['items_sold'] for v in phones_sales]), 2)
    print(avg_all_phones_sales)
    
if __name__ == "__main__":
    main()
