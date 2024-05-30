from player import Player
from game import Game
import random

if __name__ == "__main__":

    player1, player2 = Player("Thomas"), Player("Ciara")

    game = Game(points_to_win=10, current_player_index=0, players=[player1, player2])
    
    game.play_game(points_to_win=10, current_player_index=random.randint(0,1))