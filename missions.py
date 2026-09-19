missions_list = [
    {
        "name": "Покорение Марса",
        "year": 2021,
        "direction": "Марс"
    },
    {
        "name": "Отблеск солнца",
        "year": 2020,
        "direction": "Луна"
    },
    {
        "name": "Забытая восьмая",
        "year": 2050,
        "direction": "Плутон"
    },
    {
        "name": "Жар",
        "year": 2040,
        "direction": "Меркурий"
    }
]

def poisk1(dire):
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




