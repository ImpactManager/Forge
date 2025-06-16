""" Відмалювання меню """
import readchar
import os
import sys

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
            sys.exit(0) # Завершуємо програму


def menu() -> None:
    menu_options = ["Нова гра", "Завантаження", "Налаштування", "Вихід"]

    chosen_option = terminal_menu(menu_options, "МЕНЮ:")

    if chosen_option == "Вихід":
        print("До побачення!")
    elif chosen_option == "Нова гра":
        print("Гра починається...")
    elif chosen_option == "Завантаження":
        print("Завнтаження гри")
    elif chosen_option == "Налаштування":    
        print("Переходимо до налаштувань...")