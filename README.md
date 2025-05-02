# FastAPI Snakes and Ladders

## About

This project is a web-based implementation of the classic Snakes and Ladders board game, built with **Python** and **FastAPI**. It features a responsive web interface (using **TailwindCSS** for styling and **HTML/JavaScript** for interactivity) and uses **Jinja2** templates for rendering dynamic content. Players can take turns to roll a virtual dice and move their tokens on the game board, with automated handling of snakes (which send you backward) and ladders (which advance you forward). The FastAPI backend (served by **uvicorn**) powers the game logic and updates the board in real time, making it easy to run on a local server or deploy online.

## Features

- **Multiplayer gameplay:** Turn-based play for 2 or more players.
- **Dice rolling:** Click a button to roll a six-sided dice to determine movement.
- **Snakes and ladders mechanics:** Land on ladders to climb up, land on snakes to slide down.
- **Web UI:** Interactive game board rendered in the browser using Jinja2 templates.
- **Responsive styling:** Uses TailwindCSS for a clean, responsive design on any device.
- **Customizable:** Easily change player icons, board image, or snake/ladder positions.

## Tech Stack

- **Python 3.9+** – Core language and runtime for the backend.
- **FastAPI** – High-performance web framework to handle requests and game API.
- **Jinja2** – Templating engine to generate dynamic HTML pages.
- **TailwindCSS** – Utility-first CSS framework for styling the frontend.
- **HTML/JavaScript** – Frontend technologies for game rendering and interactivity.
- **uvicorn** – ASGI server to run the FastAPI application.

## Project Structure

- `main.py` – FastAPI application entry point and route handlers.
- `game.py` – Core game logic for Snakes and Ladders (board, dice, movements).
- `templates/` – Jinja2 HTML templates for the game pages (e.g., the board view).
- `static/` – Static assets (CSS, JavaScript, images, including the game board and icons).

## Local Setup

1. **Install Python:** Make sure you have Python 3.9 or newer installed on your system.
2. **Create and activate a virtual environment:**
   python3 -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
3. **Install dependencies:**
   pip install -r requirements.txt
   (Alternatively, if there is a `requirements.txt`, run `pip install -r requirements.txt`.)
4. **Run the server:**
   uvicorn main:app --reload
5. **Open in browser:** Navigate to `http://localhost:8000` to see the game interface.

## How to Play

On the game board page, each player takes turns clicking the **“Roll Dice”** button. The dice roll (a number between 1 and 6) moves the player's token forward by that many spaces on the board. If you land on the **bottom of a ladder**, your token automatically climbs up to the ladder’s top end. If you land on the **head of a snake**, your token slides down to its tail. Players alternate turns and the first player to reach the final square (usually #100) wins the game.

## Customization

You can personalize the game in several ways:

- **Player icons:** Replace the default token images in `static/images/` with your own icons to represent each player.
- **Board image:** Change the background image of the game board by updating the image file in `static/images/` or editing the template.
- **Snake/Ladder positions:** Modify the snakes and ladders data in `game.py` to change their positions on the board.
- **Number of players:** Adjust the game logic or UI to support more or fewer players as desired.

## Contributing

Contributions are welcome! Feel free to open an issue to report bugs or request features. You can also fork the repository and submit a pull request with improvements. Please ensure that your code follows the project’s style and standards.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
