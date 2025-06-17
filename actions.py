""" Обробка дій в грі атака, захист, пропуск, розмови """

def attack(player: int, enemy: int, target: str) -> dict:
    """ Функція логіки атаки. target - хто кого б'є.
        Повертаємо dict з залишком ХП там скільки дамагу нанесли
    """

    # NOTE Можна повернути і int, але якщо буде прорахунок дефа, чи 
    # випадкове ухиляння(рандом якийсь на це), то ми маємо частково порізати дамаг
    # і відпарвити інформацію про це в рендер


    if target == "enemy":
        result_hp = enemy - player
        result_dict = {"enemy_hp": result_hp, "damage_taken": player}
    
        return result_dict
    



