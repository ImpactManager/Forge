""" Головний файл """
import gui

gui.menu()


# """
# game_state - стан гри. Значення:
# menu - в меню
# idle - в нейтральній локації
# battle - в стані битви 
# """

# new_map = actions.leave_location()
#     # Який викликає load_map(map_list, current_map)

# def load_map(map_list: list, current_map: str) -> dict:
#     """Завантажуємо мапу. Повертаємо назву мапи та стан"""

#     # Тут ми повертаємо наступне {map_name: city, map_state: battle, enemy_class: str}
#     pass


# game_state = new_map.get("map_state")

# # І після цього запускаємо батву
# if game_state == "battle":
#     menu.battle_gui() # Малюємо GUI битви(ХП, тощо)
#     # В свою чергу battle_gui має кнопки атакувати/захиститися тощо
#     # який буде посилатися на actions.attack(player, enemy)

# elif game_state == "idle":   
#     menu.idle_gui() # Малюємо GUI дій на локаці

# elif game_state == "menu":
#     menu.menu() # Малюємо меню    