""" Головний файл """
import gui
import sys
import characters
import actions
from random import choice

# Рендеримо меню
menu_user_choice = gui.menu()

# Тестово створємо героя та ворога
player = characters.Player("Брудний Джо")
enemy = characters.Enemy()

# Керування боєм

# Запускаємо перевірку пункта меню, який обрав юзер
if menu_user_choice == "Нова гра":
    # Запускаємо сцену. Передаємо імена учасників

    battle_members = [player, enemy]

    while player.hp > 0 and enemy.hp > 0:
        # Хто кого б'є першим
        who_first_attack = choice(battle_members)
        # Якщо перший б'є плеер
        if who_first_attack == player:
            scene_action = gui.scene(player, enemy, enemy)
            if scene_action == "Вдарити":
                result_attack = actions.attack(player, enemy)
                print(f"Вдарили на {player.attack}. {enemy.type} має {result_attack}")
            elif scene_action == "Побігти":  
                print("Побіг ппц") 
                break 

        # Якщо перший б'є ворог
        elif who_first_attack == enemy:
            scene_action = gui.scene(player, enemy, player)
            if scene_action == "Вдарити":
                result_attack = actions.attack(enemy, player)
                print(f"{enemy.type} пробив тебе на {enemy.attack}. Маєш  HP: {result_attack}")
            elif scene_action == "Побігти":  
                print("Побіг ппц")        
                break 

        if player.hp <= 0:
            print("Ти програв")
        elif enemy.hp <= 0:
            print(f"Ти вбив {enemy.type}! Когретілешонс!")    


elif menu_user_choice == "Вихід":    
    sys.exit(0) # Завершуємо програму
