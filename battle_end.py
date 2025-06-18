from gui import terminal_menu, menu
from characters import Enemy


def end_battle(state: bool, enemy: Enemy):
    # перемога True, поразка False
    if state:
        chosen_option = terminal_menu(["Продовжити"], f"Вітаю! Ти вбив {enemy.type}!")
        menu()
    else:
        chosen_option = terminal_menu(["Почати нову гру", "Вийти в меню"], f"Поразка!")
        if chosen_option == "Почати нову гру":
            pass
            #потрібні зміни в main для того щоб викликати нову гру
        else:
            menu()
            
end_battle(True,Enemy())