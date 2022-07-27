#CODE IS NOT FINISHED
class Piece:

    def __init__(self,player):
        self.player = player
        self.is_king = False
        if self.player == 0:
            self.is_piece = False
        else:
            self.is_piece = True
        if self.player == 1:
            self.movement = -1
        else:
            self.movement = +1

    def promote(self):
        self.is_king = True
class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(Piece(0))
        for i in range(3):
            for j in range(i % 2, 8, 2):
                self.board[i][j] = Piece(1)

        for i in range(5,8):
            for j in range(i % 2 - 1, 8, 2):
                self.board[i][j] = Piece(2)
        self.play1_pieces = 12
        self.play2_pieces = 12

    def show(self):
        print(self.board)

    def move_adjacent(self, init, final,active_player):
        selected_piece = board[init[0]][init[1]]
        if not selected_piece.is_piece:
            return False
        if not selected_piece.player == active_player:
            return False
        if selected_piece.is_king:
            if abs(init[0] - final[0]) == 1 and abs(init[1] - final[1]) == 1:
                board[init[0]][init[1]] = Piece(0)
                board[final[0]][final[1]] = Piece(selected_piece.player)
                return True
        else:
            if abs(init[0] - final[0]) == 1 and final[1] - init[1] == selected_piece.movement:
                board[init[0]][init[1]] = Piece(0)
                board[final[0]][final[1]] = Piece(selected_piece.player)
                if active_player == 1 and final[1] == 7:
                    board[final[0]][final[1]].promote()
                elif active_player == 2 and final[1] == 0:
                    board[final[0]][final[1]].promote()
                return True
        return False

    def are_adjacent_moves(self,player):

        for i in range(8):
            for j in range(8):
                if board[i][j].player == player:
                    if board[i][j].is_king:
                        if i > 0:
                            if j > 0:
                                if not board[i - 1][j - 1].is_piece:
                                    return True
                            if j < 7:
                                if not board[i - 1][j + 1].is_piece:
                                    return True
                        if i < 7:
                            if j > 0:
                                if not board[i + 1][j - 1].is_piece:
                                    return True
                            if j < 7:
                                if not board[i + 1][j + 1].is_piece:
                                    return True
                    else:
                        if i > 0:
                            if board[i - 1][j - 1].movement == -1:
                                if j > 0:
                                    if not board[i - 1][j - 1].is_piece:
                                        return True
                            else:
                                if j < 7:
                                    if not board[i - 1][j + 1].is_piece:
                                        return True
                        if i < 7:
                            if board[i - 1][j - 1].movement == -1:
                                if j > 0:
                                    if not board[i + 1][j - 1].is_piece:
                                        return True
                            else:
                                if j < 7:
                                    if not board[i + 1][j + 1].is_piece:
                                        return True
        return False

    def captures(self,player):
        captures = []
        for i in range(8):
            for j in range(8):
                if board[i][j].player == player:
                    if board[i][j].is_king:
                        if i - 1 > 0:
                            if j - 1 > 0:
                                if board[i - 1][j - 1].is_piece and not board[i-2][j-2].is_piece:
                                    captures.append(((i,j),(i-2,j-2)))
                            if j + 1 < 7:
                                if board[i - 1][j + 1].is_piece and not board[i - 2][j + 2].is_piece:
                                    captures.append(((i, j), (i - 2, j + 2)))
                        if i + 1 < 7:
                            if j - 1 > 0:
                                if board[i + 1][j - 1].is_piece and not board[i + 2][j - 2].is_piece:
                                    captures.append(((i, j), (i - 2, j - 2)))
                            if j + 1 < 7:
                                if board[i - 1][j + 1].is_piece and not board[i - 2][j + 2].is_piece:
                                    captures.append(((i, j), (i - 2, j + 2)))
                    else:
                        if i - 1 > 0:
                            if board[i - 1][j - 1].movement == -1:
                                if j - 1 > 0:
                                    if board[i - 1][j - 1].is_piece and not board[i - 2][j - 2].is_piece:
                                        captures.append(((i, j), (i - 2, j - 2)))
                            else:
                                if j + 1 < 7:
                                    if board[i - 1][j + 1].is_piece and not board[i - 2][j + 2].is_piece:
                                        captures.append(((i, j), (i - 2, j + 2)))
                        if i + 1 < 7:
                            if board[i - 1][j - 1].movement == -1:
                                if j -1  > 0:
                                    if board[i + 1][j - 1].is_piece and not board[i + 2][j - 2].is_piece:
                                        captures.append(((i, j), (i - 2, j - 2)))
                            else:
                                if j + 1 < 7:
                                    if board[i - 1][j + 1].is_piece and not board[i - 2][j + 2].is_piece:
                                        captures.append(((i, j), (i - 2, j + 2)))
        return captures

board_class = Board()

selected_piece_location = (0,0)
move_to_location = (0,0)

game_over = False
is_valid = False
player_turn = 0
captures = []
while not game_over:
    board = board_class.board
    player_turn = player_turn % 2 + 1
    captures = board_class.captures(player_turn)
    if captures == []:
        if not board_class.are_adjacent_moves(player_turn):
            game_over = True
    else:
        if len(captures) >= 1:
             print(captures)

        while not is_valid:
            #get move_to_location and selected_piece_location from user via nathaniel
            is_valid = board_class.move(selected_piece_location,move_to_location)