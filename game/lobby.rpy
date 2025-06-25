label lobby:
    menu: 
        "Створити лоббі":
            jump create
        "Приэднатися":
            jump joinLobby

label create:
    $ lb = create_lobby()
    "Лоббі [lb], передайте цей номер вашому другові для того щоб він міг приєднатися"
    "чекаємо другого ігрока.."
    return

label joinLobby:
    #unique player id
    $ player_id = renpy.random.randint(10000, 99999)
    $ lb = renpy.input("Будь ласка введіть номер лоббі")
    $ lb = lb.strip() 

    #sending player id and lobby id to the server   
    $ result = renpy.fetch(f"{server_ulr}/join", json={"playerId": f"{player_id}", "lobbyId": f"{lb}"}, result="json")

    #if all guchi lets sent
    if result["live"] == "true":
        $ result = renpy.fetch(f"{server_ulr}/{lb}", json={"game": "ready"}, result="json")
        $ lobby_path = server_ulr + "/" + lb
        "Ви приєднались до лоббі успішно!"
    else:
        "Не вдалося приєднатись до лоббі. Спробуйте ще раз."

    return

init python:
    server_ulr = "http://localhost:3000"
    
    lobby_path = ""

    def create_lobby():
        player_id = renpy.random.randint(10000, 99999)
        lobby_id = renpy.random.randint(10000, 99999)
        result = renpy.fetch(f"{server_ulr}/create", json={"playerId": f"{player_id}", "lobbyId": f"{lobby_id}"}, result="json")
        return result["id"]
    
    def polling():
        result = renpy.fetch(f"{server_ulr}/{lb}", json={"":""}, result="json")
        