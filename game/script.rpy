# You can place the game code here.

image bg bg_Junkyard_AutoHaven = "bg_Junkyard_AutoHaven.png" # Де "bg" - це тег, а "my_room" - назва для використання в коді

image goblin happy = "goblin_happy.png"
image goblin rage = "goblin_rage.png"

define e = Character("Гоблін") # Приклад визначення персонажа (можеш змінити або додати своїх)
define mc = Character("Ви") # Визначимо головного героя

label start:
    play audio "dead-melodies-the-sacred-scroll.mp3"
    scene bg bg_Junkyard_AutoHaven # Змінимо фон на кімнату, що є в прикладі
    with fade # Зробимо плавний перехід

    #NOTE:трошки попрацював над экраном батлу -fen
    jump battle

    "Привіт, світе! Це моя перша візуальна новела." # Простий рядок тексту від оповідача
    show goblin rage at truecenter

    e "Чого прийшов?!" # Діалог від персонажа "Ейлін"

    hide goblin rage
    show player at truecenter

    mc "Та от сам думаю." # Діалог від головного героя

    hide player at center
    show goblin rage at truecenter

    e "Що ти хочеш зробити далі?"
    hide goblin rage
    menu: # Створимо простий вибір
        "Розповісти про себе.":
            hide goblin rage
            show player at truecenter
            mc "Я лише вчуся."
            show goblin rage at truecenter
            hide player at truecenter
            e "Ну-ну."

        "Вже йду.":
            scene bg bg_Junkyard_AutoHaven
            show goblin happy at truecenter
            e "Бувай! І не повертайся."
            jump end_game # Перейдемо до кінця гри

    scene bg bg_Junkyard_AutoHaven
    show goblin happy at truecenter
    e "Ось так ти можеш взаємодіяти з грою."

    hide goblin # Приховати персонажа

    "Кінець демонстрації."

label end_game: # Мітка для кінця гри
    "Дякую за гру!"
    return # Завершує гру і повертає до головного меню