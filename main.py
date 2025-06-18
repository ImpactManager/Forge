""" Головний файл """
import gui
import sys
import characters
import actions
from random import choice
from os import system

def resize_windows_terminal(cols, lines):
    """Змінює розмір вікна терміналу для Windows."""
    command = f"mode con: cols={cols} lines={lines}"
    system(command)

resize_windows_terminal(220, 120)    

# Запускаємо перевірку пункта меню, який обрав юзер
def game_processor() -> None:
    """ Основний процессор гри """

    # Рендеримо меню
    menu_user_choice = gui.menu()

    if menu_user_choice == "Нова гра":

        # Тестово створємо героя та ворога
        player = characters.Player("Брудний Джо")
        enemy = characters.Enemy()

        # Запускаємо сцену. Передаємо імена учасників
        battle_members = [player, enemy]

        # Хто кого б'є першим
        current_fighter = choice(battle_members)

        # Якщо кимось з учасників був застосований блок
        player_defense_state = False
        enemy_defense_state = False

        while player.hp > 0 and enemy.hp > 0:

            # Якщо перший б'є плеер
            if current_fighter == player:
                scene_action = gui.scene(player, enemy, enemy)
                if scene_action == "Вдарити":
                    actions.attack(player, enemy, enemy_defense_state)
                    enemy_defense_state = False
                elif scene_action == "Захиститися": 
                    player_defense_state = True
                elif scene_action == "Побігти":  
                    print("Побіг ппц") 
                    break 
                # Передаємо хід ворогу
                current_fighter = enemy     

            # Якщо перший б'є ворог
            elif current_fighter == enemy:
                scene_action = gui.scene(player, enemy, player)
                if scene_action == "Вдарити":
                    actions.attack(enemy, player, player_defense_state)
                    player_defense_state = False
                elif scene_action == "Захиститися": 
                    enemy_defense_state = True    
                elif scene_action == "Побігти":  
                    print("Побіг ппц")        
                    break 
                # Передаємо хід гравцю
                current_fighter = player  

            if player.hp <= 0:
                gui.end_battle(False, enemy, game_processor)
            elif enemy.hp <= 0:
                gui.end_battle(True, enemy, game_processor)   


    elif menu_user_choice == "Вихід":    
        sys.exit(0) # Завершуємо програму

game_processor()