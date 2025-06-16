""" Обробка дій в грі атака, захист, пропуск, розмови """
import gui
import readchar

# Флаг, що хто ходить, гравець чи ворог
player_turn = True

def turn(player, enemy):
    """
    Прораховуємо хто ходить. За замовчуванням перший - гравець.
    """

    print("Натисни ENTER, щоб продовжити...")

    while True:
        key = readchar.readkey()
        if key == readchar.key.ENTER:
            # Ходить гравець
            if player_turn is True:
                attack(player, enemy, "enemy")
                player_turn = False
            # Ходить ворог    
            else:
                attack(player, enemy, "player")   
                player_turn = True  

def attack(player, enemy, target: str) -> None:
    """ Функція логіки атаки. target це ціль кого б'є """

    key = readchar.readkey()

    while enemy.hp > 0 and player.hp > 0:
        gui.clear_screen()
        if target == "player":
            print("Біє ", player.name)
            enemy.hp = enemy.hp - player.attack
            if key == readchar.key.ENTER:
                turn(player, enemy)
                if enemy.hp == 0:
                    print(enemy.name, " був вбитий.")
                    return False
                
        elif target == "enemy":
            print("Біє ", enemy.name)
            player.hp = player.hp - enemy.attack
            if key == readchar.key.ENTER:
                turn(player, enemy) 
                if player.hp == 0:
                   print(player.name, " був вбитий.") 
                   return False 

