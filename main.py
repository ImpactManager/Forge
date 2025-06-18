""" Головний файл """
import gui
import sys
import characters
import actions
from random import choice

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
        
        while player.hp > 0 and enemy.hp > 0:

            # Якщо перший б'є плеер
            if current_fighter == player:
                scene_action = gui.scene(player, enemy, enemy)
                if scene_action == "Вдарити":
                    actions.attack(player, enemy)
                elif scene_action == "Побігти":  
                    print("Побіг ппц") 
                    break 
                # Передаємо хід ворогу
                current_fighter = enemy     

            # Якщо перший б'є ворог
            elif current_fighter == enemy:
                scene_action = gui.scene(player, enemy, player)
                if scene_action == "Вдарити":
                    actions.attack(enemy, player)
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