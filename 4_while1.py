"""

Домашнее задание №4

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    inp = ""
    msg = "Как дела?"
    
    while inp != "Хорошо":
        inp = input(f'{msg}\n')
    
if __name__ == "__main__":
    hello_user()
