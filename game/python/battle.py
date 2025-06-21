import readchar
import os
from random import choice
from characters import Enemy, Player
from time import sleep

def clear_screen() -> None:
    """Очищує екран терміналу."""
    os.system("cls" if os.name == "nt" else "clear")

def controls(options, index):
        selected_index = index
        num_options = len(options)
        
        for i, option in enumerate(options):
            if i == selected_index:
                # Виділяємо обраний пункт
                print(f"> {option} <".center(32))
            else:
                print(f"  {option}".center(32))

        # Читаємо натискання клавіші
        key = readchar.readkey()

        if key == readchar.key.UP:
            selected_index = (selected_index - 1 + num_options) % num_options
        elif key == readchar.key.DOWN:
            selected_index = (selected_index + 1) % num_options
        elif key == readchar.key.ENTER:
            clear_screen()  # Очищаємо екран перед виходом
            return options[selected_index]
        elif key == readchar.key.ESC:  # Додаємо обробку клавіші ESC для виходу
            clear_screen()
        return selected_index
    
def battle(target, player, goblin, location="Свалка автохевен") -> None | int:

    options = ["Аттака", "Побіг"]
    #розміри
    width = 32
    height = 3
    #потрібен для керування
    index = 0
    
    while True:
        clear_screen()
        print("#" * width)
        print("#" + location.center(width - 2) + "#")
        print("#" * width)
        print("#" + " HP: " + f"{enemy.hp}")
        print(goblin.center(width))
        print("#\n" * height)
        
        index = controls(options, index)

        
enemy = Enemy()
player = Player(name="Джо")



goblin = """  
     XXXXX     
      X X      
       X       
X    XXXXX    X
XXXXXXXXXXXXXXX
       XX      
      X  X     
     X    X    
    X      X   """
    
battle(Enemy, player, goblin)