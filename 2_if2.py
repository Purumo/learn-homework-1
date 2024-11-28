"""

Домашнее задание №2

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def compare_strings(s1, s2):
    out_val = -1
    if not(type(s1) is str and type(s2) is str):
        out_val = 0
    elif s1 == s2:
        out_val = 1
    elif len(s1) > len(s2):
        out_val = 2
    elif s1 != s2 and s2 == 'learn':
        out_val = 3
    return out_val

def main():
    print(f'{compare_strings(3, 'hello world') = }')
    
    print(f'{compare_strings('I like chocolate', 'I like chocolate') = }')
    
    print(f'{compare_strings('I like chocolate so much', 'I like chocolate') = }')
    
    print(f'{compare_strings('small', 'learn') = }')
    
    print(f'{compare_strings('learn', 'learn') = }')
    

if __name__ == "__main__":
    main()
