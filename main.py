from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from game import Game

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

game = None

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    global game
    if game is None or not game.players:
        return templates.TemplateResponse("choose_players.html", {"request": request})

    board = generate_board(game.players, game.current_turn)
    last_move = getattr(game, "last_move", None)  # (player_name, old_pos, new_pos, icon)
    return templates.TemplateResponse("board.html", {
        "request": request,
        "players": game.players,
        "messages": game.messages[-8:],
        "winner": game.get_winner(),
        "current_player": game.players[game.current_turn].name,
        "current_player_obj": game.players[game.current_turn],
        "board": board,
        "last_move": last_move,
        "is_animating": False,
        "ladders": Game.LADDERS,
        "snakes": Game.SNAKES,
    })

@app.post("/start", response_class=RedirectResponse)
async def start_game(request: Request):
    form = await request.form()
    num_players = int(form.get("num_players", 2))
    global game
    game = Game(num_players)
    return RedirectResponse("/", status_code=303)

@app.post("/roll", response_class=RedirectResponse)
async def roll_dice(request: Request):
    global game
    if game and not game.is_finished():
        game.next_turn()
    return RedirectResponse("/", status_code=303)

@app.post("/restart", response_class=RedirectResponse)
async def restart_game(request: Request):
    global game
    game = None
    return RedirectResponse("/", status_code=303)

def generate_board(players, current_turn):
    board = []
    current_player = players[current_turn]

    last_move_to = game.last_move[2] if game and game.last_move else None

    for row in range(10, 0, -1):
        start = (row - 1) * 10 + 1
        end = row * 10 + 1
        row_cells = list(range(start, end))
        if row % 2 == 0:
            row_cells.reverse()

        row_with_players = []
        for cell in row_cells:
            if cell == 1 and current_player.position == 1:
                cell_players = [current_player.icon]
            else:
                # ✨ Avoid showing icon in the destination cell during animation
                cell_players = [
                    p.icon for p in players
                    if p.position == cell and (cell != last_move_to or p.name != current_player.name)
                ]
            row_with_players.append({
                "number": cell,
                "players": cell_players,
            })
        board.append(row_with_players)
    return board

