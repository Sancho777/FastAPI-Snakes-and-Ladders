import random

class Player:
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon
        self.position = 1  # Start at cell 1 (zigzag numbering)

class Game:
    ICONS = ["🎩", "🐱", "🧙‍♂️", "🐶", "🦊", "🐼", "🐸", "🐵", "🐧", "🦄"]

    LADDERS = {
        2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84,
        36: 44, 51: 67, 78: 98, 71: 91, 87: 94,
    }
    SNAKES = {
        16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53,
        89: 68, 92: 88, 95: 75, 99: 80,
    }

    def __init__(self, num_players):
        self.players = [Player(f"Player {i+1}", self.ICONS[i]) for i in range(num_players)]
        self.current_turn = 0
        self.messages = []
        self.last_move = None

    def roll_dice(self):
        return random.randint(1, 6)

    def next_turn(self):
        player = self.players[self.current_turn]
        dice = self.roll_dice()
        old_position = player.position
        new_position = old_position + dice

        if new_position > 100:
            new_position = old_position  # Can't move beyond 100

        move_msg = f"{player.icon} rolled a 🎲 {dice} and moved from {old_position} to {new_position}"

        # Check ladders
        if new_position in self.LADDERS:
            destination = self.LADDERS[new_position]
            move_msg += f" 🚀 Climbed a ladder to {destination}"
            new_position = destination

        # Check snakes
        elif new_position in self.SNAKES:
            destination = self.SNAKES[new_position]
            move_msg += f" 🐍 Bitten by a snake down to {destination}"
            new_position = destination

        player.position = new_position
        self.messages.append(move_msg)
        self.last_move = (player.name, old_position, new_position, player.icon)

        self.current_turn = (self.current_turn + 1) % len(self.players)

    def get_winner(self):
        for player in self.players:
            if player.position == 100:
                return player.icon
        return None

    def is_finished(self):
        return self.get_winner() is not None
