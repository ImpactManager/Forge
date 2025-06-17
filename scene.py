###########################
###простий приклад сцени###
#####python scene.py#######

import readchar
import os
import sys
from characters import Enemy

def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def terminal_menu(options, location, enemy) -> None|int:
    selected_index = 0
    num_options = len(options)

    while True:
        clear_screen()
        print(location)
        
        ####ці прінти можно перенести в класс enemy у метод __str__ 
        ####та викликати один print(enemy) 
       
        print("-" * len(location))
        print("Перед вами:")
        print(enemy)
        print(f"🗣️  {enemy.say}")
        print("-" * len(location))

        for i, option in enumerate(options):
            if i == selected_index:
                # Виділяємо обраний пункт
                print(f"> {option} <")
            else:
                print(f"  {option}")

        # Читаємо натискання клавіші
        key = readchar.readkey()

        if key == readchar.key.UP:
            selected_index = (selected_index - 1 + num_options) % num_options
        elif key == readchar.key.DOWN:
            selected_index = (selected_index + 1) % num_options
        elif key == readchar.key.ENTER:
            clear_screen() # Очищаємо екран перед виходом
            return options[selected_index]
        elif key == readchar.key.ESC: # Додаємо обробку клавіші ESC для виходу
            clear_screen()
            sys.exit(0) # Завершуємо програму


def scene(location: str, enemy: Enemy) -> None:
    menu_options = ["Вдарити", "Захиститися", "Побіг"]
    
    
    chosen_option = terminal_menu(menu_options, location, enemy)

    if chosen_option == "Вдарити":
       print("actions.py")
    elif chosen_option == "Захиститися":
        print("функція захисту")
    elif chosen_option == "Побіг":
         print("функція побігу") 

scene("Свалка Автохевен", Enemy().random_enemy())