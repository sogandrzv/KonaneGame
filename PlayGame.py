from KonaneGame2 import KonaneGame2
from PlayKonane import PlayKonane
from Tile import Tile
from Agent import Agent
from Board import Board
from KonaneGame import KonaneGame

class PlayGame:

    def __init__(self):
        NotImplemented

    def play(self):
        size = 6
        game = KonaneGame()
        game2 = KonaneGame2()
        initial_board = Board(size, game.initialize_board(size))
        agent1 = Agent(game2, color=Tile.P_Black, max_depth=4)
        agent2 = Agent(game, color=Tile.P_White, max_depth=2)
        # bot vs bot
        play = PlayKonane(initial_board, game, agent1=agent1, agent2=agent2)

        # player vs bot
        # play = PlayKonane(initial_board, game, agent1=agent2)


if __name__ == '__main__':
    PlayGame().play()
