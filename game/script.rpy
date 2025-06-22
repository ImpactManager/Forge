# You can place the game code here.

image bg bg_Junkyard_AutoHaven = "bg_Junkyard_AutoHaven.png" # Де "bg" - це тег, а "my_room" - назва для використання в коді

image goblin happy = "goblin_happy.png"
image goblin rage = "goblin_rage.png"


label start:
    $ player = Player(name="Джо", hp=100, attack=25, main_class="Воїн")
    $ enemy = Enemy(hp = 100, attack = 25, type = "Гоблін")

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


label battle:
    
    # show screen simple_stats_screen
    show screen enemy_info
    show screen player_info


    while (player.hp > 0) and (enemy.hp > 0):
        
        menu:
            "Влупити!":
                $ enemy.hp -= player.attack
                "Нанесено шкоди [player.attack]"
        
        $ player.hp -= enemy.attack
        "Ооооооой! {i}*Отримай*{/i} (наносить - [enemy.attack]шкоди)"
        
        
        
    hide screen simple_stats_screen
    
    if enemy.hp <= 0:
        if player.hp <= 0:
            "Ніііііііііііі, я ще повернуся!"
            
        else:
            "Єєєєєєє я виграв"
            
    else:
        "[enemy.type]Ну так шо)"