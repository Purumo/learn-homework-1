"""

Домашнее задание №5

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {
    "Как дела": "Хорошо!", 
    "Что делаешь?": "Программирую",
    "Когда спать?": "В планах в 12 ночи, как обычно",
    "Во сколько будешь вставать завтра?": "В 6:30, в понедельники oen-to-one-ы, нужно быть в офисе и ехать далеко",
    "Уходим?": "Уходим, уходим! Наступят времена почище 🧹",
}

def ask_user(answers_dict):
    out_answer = ''
    inp_question = input("Пожалуйста спросите: ")
    
    if inp_question in answers_dict.keys():
        out_answer = answers_dict[inp_question]
    else:
        out_answer = 'Я не знаю ответа на такой вопрос!'
        
    print(out_answer)
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
