"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def average_school(school_classes):
    all_school = []
    for marks in school_classes:
        all_school += marks['scores']
    return sum(all_school)/len(all_school)
def average_class(school_classes):
    for class_number in school_classes:
        print('Средняя оценка класса', class_number['school_class'], '-' )
        print(sum(class_number['scores'])/len(class_number['scores']))


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    school_classes = [{'school_class': '1а', 'scores': [5, 4, 3, 4, 4]}]
    school_classes.append ({'school_class': '1б', 'scores': [4, 4, 4, 3, 3]})
    school_classes.append ({'school_class': '1б', 'scores': [4, 4, 4, 3, 3]})  
    school_classes.append ({'school_class': '2а', 'scores': [2, 2, 3, 4, 4]}) 
    school_classes.append ({'school_class': '2б', 'scores': [4, 4, 4, 3, 5]})  
    
    print('Средняя оценка школы - ', average_school(school_classes) )
    average_class(school_classes)

if __name__ == "__main__":
    main()
