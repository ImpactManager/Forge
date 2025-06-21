"""Обробка дій в грі атака, захист, пропуск, розмови"""


def attack(fighter1_obj, fighter2_obj, defense_state: bool) -> object:
    """Функція логіки атаки."""

    if defense_state:
       fighter2_obj.hp = fighter2_obj.hp - 0
    else:
        fighter2_obj.hp = fighter2_obj.hp - fighter1_obj.attack
    return fighter2_obj
