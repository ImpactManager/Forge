# label battle:
#     show screen enemy_info
#     show screen player_info

  
#     menu: 
#         "Аттака":
#             return
#         "Захист":
#             return
#         "Побіг":
#             return

label battle:
    
    # show screen simple_stats_screen
    show screen enemy_info
    show screen player_info


    while (player.hp > 0) and (enemy.hp > 0):

        # Якщо обрано "Захист"    
        $ player_is_defence = False
        $ enemy_is_defence = False

        menu:
            "Влупити!":
                $ enemy.hp -= player.attack
                "Нанесено шкоди [player.attack]"

            "Захиститися":
                "[player.name] стає в захист"    
                $ player_is_defence = True

        # Перевіряємо, чи обрано "Захист" 
        if player_is_defence is True:
            $ player.hp -= enemy.attack*0
            $ player_is_defence = False
        else:
            $ player.hp -= enemy.attack
            "[enemy.say_something()] (наносить - [enemy.attack]шкоди)"
        
    hide screen simple_stats_screen
    
    if enemy.hp <= 0:
        if player.hp <= 0:
            "Ніііііііііііі, я ще повернуся!"
            
        else:
            "Єєєєєєє я виграв"
            
    else:
        "[enemy.type]Ну так шо)"
    

screen enemy_info():
    #Рамка з отступом та фоном
    frame:
        xalign 1.0  #позиція рамки
        yalign 0.0  

        xsize 400
        ysize 220
        
        background "#0008"
        #Горизонтально розміщення
        hbox:
            spacing 20
            #Вертикальне розміщення
            vbox:
                spacing 10
                text "[enemy.type]"
                text "[enemy.hp]"
                text "[enemy.attack]"
            add "goblin.png" size (200, 200)    


screen player_info():
    #Рамка з отступом та фоном
    frame:
        xalign 0.0  #позиція рамки
        yalign 1.0  yoffset -50 #left corner -50 пікселей
        
        xsize 400
        ysize 220

        background "#0008"
        #Горизонтальне розміщення
        hbox:
            spacing 20
            add "player.png" size (200, 200)
            #Вертикальне розміщення
            vbox:
                spacing 10
                text "Імя: [player.name]"
                text "HP: [player.hp]"
                text "Сила: [player.attack]"      