#CODE IS NOT FINISHED
class Piece:

    def __init__(self,player,row,col):
        self.player = player
        self.is_king = False
        self.row = row
        self.col = col

    def promote(self):
        self.is_king = True

class Board:
    def __init__(self):
        self.board = []
        self.play1_pieces = 12
        self.play2_pieces = 12
        self.create_board()

    def show(self):
        print(self.board)

    def move(self, piece, row, col):
        self.board[row][col] = self.board[piece.row][piece.col]
        if abs(piece.row - row) == 1 and abs(piece.col - col) == 1:
            piece = self.board[(row+piece.row)/2][(col+piece.col)/2]
            if piece != 0:
                if piece.player == 1:
                    self.play1_pieces -= 1
                elif piece.player == 2:
                    self.play2_pieces -= 1

            self.board[(row+piece.row)/2][(col+piece.col)/2] = 0
        self.board[piece.row][piece.col] = self.board[row][col]

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(8):
            self.board.append(row)
            for col in range(8):
                if col % 2 == (row+1) % 2:
                    if row < 3:
                        self.board[row].append(Piece(row, col, 1))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, 2))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

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

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 1
        self.saved_piece = None

    def are_pieces(self):
        if self.turn == 1 and self.board.play1_pieces == 0:
            return False
        if self.turn == 2 and self.board.play2_pieces == 0:
            return False
        return True

    def change_turn(self):
        self.turn = 3 - self.turn

    def captures(self, piece):
        if self.board[piece.row][piece.col] != 0:
            if self.board[piece.row+1][piece.col-1].player == 3 - self.turn:
                if piece.player == 1 or piece.is_king:
                    pass
                if piece.player == 2 or piece.is_king:
                    if i - 1 > 0:
                        if j - 1 > 0:
                            if board[i - 1][j - 1].is_piece and not board[i - 2][j - 2].is_piece:
                                captures.append(((i, j), (i - 2, j - 2)))
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

class Tree:
    pass



# need to check for all captures
# if there are none, check if there are any available moves
# if there are available moves, let the user select a piece and a destination
# and see if the piece is in the list of available moves


"""
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
"""