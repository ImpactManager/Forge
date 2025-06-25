"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const app = (0, express_1.default)();
const port = 3000;
app.use(express_1.default.json());
let lobbies = [];
app.post('/create', (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const data = req.body;
    //const dataArray = await JSON.parse(data)
    const lobbyId = yield createLobby(data.lobbyId, data.playerId);
    res.json({
        id: lobbyId,
    });
}));
app.post('/join', (req, res) => {
    const data = req.body;
    const lobbyId = data.lobbyId;
    const playerId = data.playerId;
    lobbies.forEach((lobbie) => {
        if (lobbie.id === lobbyId) {
            lobbie.players.push(playerId);
        }
        app.post(`/${lobbyId}`, (req, res) => {
            console.log("Dynamic path");
        });
        console.log(lobbies);
    });
    res.json({
        live: "true",
        received: data,
    });
});
const createLobby = (id, player) => __awaiter(void 0, void 0, void 0, function* () {
    const lobby = {
        id: id,
        players: [player]
    };
    console.log(lobby);
    lobbies.push(lobby);
    return lobby.id;
});
app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});
