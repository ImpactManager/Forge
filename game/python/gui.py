"""Відмалювання меню"""

import readchar
import os
from random import choice
from characters import Enemy
from time import sleep

def clear_screen() -> None:
    """Очищує екран терміналу."""
    os.system("cls" if os.name == "nt" else "clear")


def terminal_menu(options, title="Оберіть опцію:") -> None | int:
    """
    Створює меню.

    Args:
        options (list): Список рядків, що представляють пункти меню.
        title (str): Заголовок меню.

    Returns:
        str: Обраний пункт меню.
    """
    selected_index = 0
    num_options = len(options)

    while True:
        clear_screen()
        print(title)
        print("-" * len(title))

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
            clear_screen()  # Очищаємо екран перед виходом
            return options[selected_index]
        elif key == readchar.key.ESC:  # Додаємо обробку клавіші ESC для виходу
            clear_screen()


def menu() -> str:
    """Відмальовуємо меню"""
    menu_options = ["Нова гра", "Завантаження", "Налаштування", "Вихід"]

    chosen_option = terminal_menu(menu_options, "МЕНЮ:")

    if chosen_option == "Вихід":
        return chosen_option
    elif chosen_option == "Нова гра":
        return chosen_option
    elif chosen_option == "Завантаження":
        print("Завнтаження гри")
    elif chosen_option == "Налаштування":
        print("Переходимо до налаштувань...")


def scene(player_obj, enemy_obj, target) -> str:
    """Відмальовуємо сцену гри. Приймаємо:
    player_name як ім'я гравця
    enemy_name як ім'я ворога

    Відмальовуємо пункти керування
    """

    scene_actions = ["Вдарити", "Захиститися", "Побігти"]

    # Якщо першим ходить ворог, він не може втекти
    if target == player_obj:
        # Залишаємо тільки "Вдарити"
        scene_actions = scene_actions[0]
    else:
        scene_actions = scene_actions

    enemy_action_choice = choice(scene_actions)
    
    if target == player_obj:
        turn = f"Хід: ворога.\n"
        hp = f"\nВаше HP: {player_obj.hp}\n"
        scene_discription = f"Ну шо {player_obj.name}, каже {enemy_obj.type}, настав і твій час. Отримай."
        enemy_display = f"Перед вами: \n{enemy_obj}"
        scene_discription = turn + enemy_display + hp + scene_discription
        chosen_option = terminal_menu(["Ану давай!"], f"{scene_discription}")
        return("Вдарити")

    elif target == enemy_obj:
        turn = f"Хід: ваш.\n"
        hp = f"\nВаше HP: {player_obj.hp}\n"
        scene_discription = f"Йди сюди вонючий {enemy_obj.type}."
        enemy_display = f"Перед вами: \n{enemy_obj}"
        scene_discription = turn + enemy_display + hp + scene_discription
        chosen_option = terminal_menu(scene_actions, f"{scene_discription}")

    if chosen_option == "Вдарити":
        return chosen_option
    elif chosen_option == "Захиститися":
        return chosen_option
    elif chosen_option == "Побігти":
        return chosen_option

def end_battle(state: bool, enemy: Enemy, run_new_game):
    # перемога True, поразка False
    if state:
        chosen_option = terminal_menu(["Продовжити"], f"Вітаю! Ти вбив {enemy.type}!")
        menu()
    else:
        chosen_option = terminal_menu(["Почати нову гру", "Вийти в меню"], f"Поразка!")
        if chosen_option == "Почати нову гру":
            run_new_game()
        else:
            menu()