"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user_dict():
    
    asks_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую.", "Где ты находишься?": "На жестком диске."}
    while True:
        try:
            ask=input('Задайте вопрос: ')
            answer = asks_and_answers.get(ask,0)
            if not ask==0:
                print(answer)
            else:
                print('Я не знаю ответа.')
        except KeyboardInterrupt:
            print('Пока')
            break
    
ask_user_dict()