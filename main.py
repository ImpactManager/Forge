""" Головний файл """
import gui
import sys
import characters
import actions

# Рендеримо меню
menu_user_choice = gui.menu()

# Тестово створємо героя та ворога
player = characters.Player("Брудний Джо")
enemy = characters.Enemy()

# Керування боєм

# Запускаємо перевірку пункта меню, який обрав юзер
if menu_user_choice == "Нова гра":
    # Запускаємо сцену. Передаємо імена учасників
    scene_action = gui.scene(player.name, enemy.type)
    if scene_action == "Вдарити":
        result_attack = actions.attack(player.attack, enemy.hp, target="enemy")
        print(f"Вдарили на {result_attack['damage_taken']}. {enemy.type} має {result_attack['enemy_hp']}")
    elif scene_action == "Побігти":  
        print("Побіг ппц") 


elif menu_user_choice == "Вихід":    
    sys.exit(0) # Завершуємо програму
