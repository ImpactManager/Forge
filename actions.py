""" Обробка дій в грі атака, захист, пропуск, розмови """

def attack(player_obj, enemy_obj, target: str) -> int:
    """ Функція логіки атаки. target - хто кого б'є.
    """
    if target == "enemy":
        result_hp = enemy_obj.hp - player_obj.attack

        return result_hp
    



