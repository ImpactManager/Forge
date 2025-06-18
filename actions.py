""" Обробка дій в грі атака, захист, пропуск, розмови """

def attack(fighter1_obj, fighter2_obj) -> object:
    """ Функція логіки атаки. """
    fighter2_obj.hp = fighter2_obj.hp - fighter1_obj.attack
    return fighter2_obj.hp
    
    



