import express, { Request, Response } from 'express'
const app = express()
const port = 3000
app.use(express.json());

let lobbies: lobby[] = []

interface lobby {
    id: string,
    players: string[]
    ready?: string
}
//шлях створення лоббі
app.post('/create', async (req: Request, res: Response) => {
  const data = req.body;
  //const dataArray = await JSON.parse(data)
  const lobbyId = await createLobby(data.lobbyId, data.playerId)
  res.json({
    id: lobbyId,
  });
});

//шлях приєднная до лоббі
app.post('/join', (req: Request, res: Response) => {
  const data = req.body;
  const lobbyId = data.lobbyId
  const playerId = data.playerId

  //якщо лоббі існує доддаємо player id до листа
  lobbies.forEach((lobbie) => {
    if (lobbie.id === lobbyId) {
        lobbie.players.push(playerId)
    }})

    //створюємо унікальний шлях до нашого лоббі
    app.post(`/${lobbyId}`, (req: Request, res: Response) => {
      const currentLobbie = lobbies.find(lobbie => lobbie.id === lobbyId)
      const data = req.body;

      // якщо лоббі не знайденно відправляємо нот фаунд
      if (!currentLobbie) res.json({id: "not found"})

      if (data.game === "ready" && currentLobbie){
          currentLobbie.ready = "true"
          res.json(currentLobbie)
      }


      });



  res.json({
    live: "true",
  });
});

const createLobby = async(id: string, player: string)=>{
    const lobby: lobby = {
        id: id,
        players: [player]
    }

    console.log(lobby)
    lobbies.push(lobby)

    return lobby.id
}

app.listen(port, () => {
  console.log(`Listening on port ${port}`)
})