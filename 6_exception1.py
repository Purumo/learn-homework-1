"""

Домашнее задание №6

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    inp = ""
    msg = "Как дела?"

    try:
        while inp != "Хорошо":
            inp = input(f'{msg}\n')
    except KeyboardInterrupt:
        print("Пока!")
    except:
        print("Случилось что-то странное :(")
    
if __name__ == "__main__":
    hello_user()
