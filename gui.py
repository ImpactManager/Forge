""" Відмалювання меню """
import readchar
import os

def clear_screen() -> None:
    """Очищує екран терміналу."""
    os.system('cls' if os.name == 'nt' else 'clear')

def terminal_menu(options, title="Оберіть опцію:") -> None|int:
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
            clear_screen() # Очищаємо екран перед виходом
            return options[selected_index]
        elif key == readchar.key.ESC: # Додаємо обробку клавіші ESC для виходу
            clear_screen()

def menu() -> str:
    """ Відмальовуємо меню """
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

def scene(player_name: str, enemy_name: str) -> str:
    """ Відмальовуємо сцену гри. Приймаємо: 
        player_name як ім'я гравця
        enemy_name як ім'я ворога

        Відмальовуємо пункти керування
    """

    scene_discription = f"Ну шо {player_name}, каже {enemy_name}, настав і твій час. Діставай зброю пес."

    scene_actions = ["Вдарити", "Побігти"]
    chosen_option = terminal_menu(scene_actions, f"Сцена перша. {scene_discription}")

    if chosen_option == "Вдарити":
        return chosen_option
    elif chosen_option == "Побігти":
        return chosen_option






