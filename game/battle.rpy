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
            

# screen simple_stats_screen:
#     frame:
#         xalign 0.01 yalign 0.05
#         vbox:
#             text "[player.name]" size 22 xalign 0.5
#             null height 5
#             hbox:
#                 bar:
#                     xmaximum 130
#                     value red_hood_hp
#                     range red_hood_max_hp
#                     left_gutter 0
#                     right_gutter 0
#                     thumb None
#                     thumb_shadow None
                    
#                 null width 5
                
#                 text "[red_hood_hp] / [red_hood_max_hp]" size 16
                
                
#     frame:
#         xalign 0.99 yalign 0.05
#         vbox:
#             text "[enemy.type]" size 22 xalign 0.5
#             null height 5
#             hbox:
#                 bar:
#                     xmaximum 130
#                     value wolf_hp
#                     range wolf_max_hp
#                     left_gutter 0
#                     right_gutter 0
#                     thumb None
#                     thumb_shadow None
                    
#                 null width 5
                
#                 text "[wolf_hp] / [wolf_max_hp]" size 16
                