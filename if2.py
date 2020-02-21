"""
Домашнее задание №1
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
def compare_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0
    if str1==str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif 'learn'==str2:
        return 3
    else:
        return "Повторите снова."


print(compare_strings(str1 = 'petya', str2 = 'learn'))
print(compare_strings(str1 = 'learn', str2 = 'learn'))
print(compare_strings(str1 = 'learn', str2 = 'it'))
print(compare_strings(str1 = 2, str2 = 4))

