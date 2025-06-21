label battle:
    show screen enemy_info
    show screen player_info

  
    menu: 
        "Аттака":
            return
        "Захист":
            return
        "Побіг":
            return
    

screen enemy_info():
    #Рамка з отступом та фоном
    frame:
        xalign 1.0  #позиція рамки
        yalign 0.0  
        
        background "#0008"
        #Горизонтально розміщення
        hbox:
            spacing 20

            #Вертикальне розміщення
            vbox:
                spacing 10
                text "Імя: Гоблін"
                text "HP: 100"
                text "Сила: 15"

            add "goblin_happy.png" size (200, 300)


screen player_info():
    #Рамка з отступом та фоном
    frame:
        xalign 0.0  #позиція рамки
        yalign 1.0  yoffset -50 #left corner -50 пікселей
        
        background "#0008"
        #Горизонтальне розміщення
        hbox:
            spacing 20

            #Вертикальне розміщення
            vbox:
                spacing 10
                text "Імя: Джо"
                text "HP: 100"
                text "Сила: 25"
