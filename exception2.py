"""
Домашнее задание №1
Исключения: приведение типов
* Напишите функцию get_summ(num_one, num_two), которая принимает 
  на вход два целых числа (int), складывает их и возвращает результат 
  сложения
* Оба аргумента нужно приводить к целому числу при помощи int() и 
  перехватывать исключение ValueError если приведение типов не сработало
    
"""

def get_summ(num_one, num_two):
    try:
        num1 = int(num_one)
        num2 = int(num_two)
        return num1+num2
    except ValueError:
        print('Ошибка')
        
    
if __name__ == "__main__":
    print(get_summ(3, 4))
    print(get_summ(3, "5"))
    print(get_summ("10", "43"))
    print(get_summ("четыре", 6))
    print(get_summ("двенадцать", "Сто"))