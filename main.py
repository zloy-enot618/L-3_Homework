from time import sleep as xdwd
from missions import *

"""
    План разрабтки приложения для меня ориентеровка:
    [...] 1. Вывести полный список миссий.
    [?] 2. Спросить направление для поиска.
         |                                \
         |                                 \
        \|/                                 \ 
[!] 3. Вывести миссии выбранного направления \
                                              |
                                             \|/
                       [:(] 3. Сообщить если миссии не найдены.      

"""




def Main(missions_list):
    print("===Каталог Космических миссий!===")
    xdwd(0.3)
    print("==Текущие миссии==")
    xdwd(0.33)
    for always_int, moved_missions_list in enumerate(missions_list, start=1):
        print(f"{always_int}._________________________________\n   |- Название: {moved_missions_list['name']} -|\n   |- Год: {moved_missions_list['year']} -|\n   |- Направление: {moved_missions_list['direction']} -|\n   |_______________________________\n")
        xdwd(0.3)
    print(f"\nВведите направление для поиска: ", end='')
    dire = input()

    is_any_find = 0

    risults = []
    for poisk in missions_list:
        if poisk["direction"].lower() == dire.lower():
            risults.append(poisk)
            is_any_find += 1
    if is_any_find == 0:
        print("Не найдено ни одной миссии ;(! Сожалеем!")
    elif is_any_find != 0:
        print(f"По вашему запросу найдено {is_any_find} результатов.\nВот эти миссии:\n")
        for always_int1, moved_risults in enumerate(risults, start=1):
            print(f"{always_int1}._________________________________\n   |- Название: {moved_risults['name']} -|\n   |- Год: {moved_risults['year']} -|\n   |- Направление: {moved_risults['direction']} -|\n   |_______________________________")
    

if __name__ == "__main__":
    Main(missions_list)
elif __name__ != "__main__":
    print("Запустите файл на прямую!")