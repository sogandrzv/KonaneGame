from Tile import Tile

class Agent:
    MIN_VALUE = -1000000
    MAX_VALUE = 1000000

    def __init__(self, game, color, max_depth):
        self.game = game
        self.color = color
        self.max_depth = max_depth

    def do_min_max(self, current_board):
        move, value = self.max(current_board, self.color, 0, self.MIN_VALUE, self.MAX_VALUE)

        return move

    def max(self, current_board, current_color, depth, alpha, beta):
        if self.game.check_terminal(current_board, current_color):
            return None, self.game.evaluate(current_board, current_color, -1000)

        if depth == self.max_depth:
            return None, self.game.evaluate(current_board, current_color)

        all_moves = self.game.generate_all_possible_moves(current_board, current_color)
        best = None
        best_value = self.MIN_VALUE
        # for move in all_moves:
        #     temp_move=self.min(current_board.next_board(current_color, move))
        #     temp_value =self.game.opponent((current_color), depth+1)
        #     if temp_value > best_value:
        #         best_value = temp_value
        #         best = temp_move
        # return best, best_value
        for move in all_moves:
            next_one = current_board.next_board(current_color, move)
            opponent_color = self.game.opponent(current_color)
            temp_move, min_value = self.min(next_one, opponent_color, depth+1, alpha, beta)

            if min_value > best_value:
                best_value = min_value
                best = move


            if best_value >= beta:
                return best, best_value

            maximumm=max(alpha, best_value)
            alpha = maximumm

        return best, best_value

    def min(self, current_board, current_color, depth,alpha, beta):
        if self.game.check_terminal(current_board, current_color):
            return None, self.game.evaluate(current_board, current_color, 1000)
        if depth == self.max_depth:
            return None, self.game.evaluate(current_board, current_color)
        all_moves = self.game.generate_all_possible_moves(current_board, current_color)
        best = None
        best_value = self.MAX_VALUE
        for move in all_moves:
            next_one = current_board.next_board(current_color, move)
            opponent_color = self.game.opponent(current_color)
            temp_move, max_value = self.max(next_one, opponent_color, depth + 1, alpha, beta)

            if max_value < best_value:
                best_value = max_value
                best = move

            if best_value <= alpha:
                return best, best_value

            minimumm= min(alpha, best_value)
            alpha = minimumm

        return best, best_value
        #     temp_move, temp_value = self.max(current_board.next_board(current_color, move),
        #                                      self.game.opponent(current_color), depth+1)
        #     if temp_value < best_value:
        #         best_value = temp_value
        #         best = temp_move
        # return best, best_value