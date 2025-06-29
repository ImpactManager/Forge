﻿# You can place the game code here.

image bg bg_Junkyard_AutoHaven = "bg_Junkyard_AutoHaven.png" # Де "bg" - це тег, а "my_room" - назва для використання в коді

image goblin happy = "goblin_happy.png"
image goblin rage = "goblin_rage.png"


label start:
    $ player = Player(name="Джо", hp=100, attack=25, main_class="Воїн")
    $ enemy = Enemy(hp = 100, attack = 25, type = "Гоблін")

    $ player_speaker = Character(player.name)
    $ enemy_speaker = Character(enemy.type)

    # Музика
    play audio "dead-melodies-the-sacred-scroll.mp3"
    scene bg bg_Junkyard_AutoHaven # Змінимо фон на кімнату, що є в прикладі
    with fade # Зробимо плавний перехід
    jump battle

    "Привіт, світе! Це моя перша візуальна новела." # Простий рядок тексту від оповідача
    show goblin rage at truecenter

    enemy_speaker "Чого прийшов?!" # Діалог від персонажа "Ейлін"

    hide goblin rage
    show player at truecenter

    player_speaker "Та от сам думаю." # Діалог від головного героя

    hide player at center
    show goblin rage at truecenter

    enemy_speaker "Що ти хочеш зробити далі?"
    hide goblin rage
    menu: # Створимо простий вибір
        "Напасти на тебе.":
            #NOTE:трошки попрацював над экраном батлу -fen
            jump battle

        "Вже йду.":
            scene bg bg_Junkyard_AutoHaven
            show goblin happy at truecenter
            enemy_speaker "Бувай! І не повертайся."
            jump end_game # Перейдемо до кінця гри

    scene bg bg_Junkyard_AutoHaven
    show goblin happy at truecenter
    enemy_speaker "Ось так от"

    hide goblin # Приховати персонажа

label end_game: # Мітка для кінця гри
    "Дякую за гру!"
    return # Завершує гру і повертає до головного меню