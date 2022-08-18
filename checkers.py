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

    def move(self, piece_to_move, row, col):
        self.board[row][col] = self.board[piece_to_move.row][piece_to_move.col]
        self.board[piece_to_move.row][piece_to_move.col] = self.board[row][col]
        if abs(piece_to_move.row - row) > 1 and abs(piece_to_move.col - col) > 1:
            piece = self.board[(row+piece_to_move.row)/2][(col+piece_to_move.col)/2]
            if piece.player == 1:
                self.play1_pieces -= 1
            elif piece.player == 2
                self.play2_pieces -= 1
            self.board[(row+piece.row)/2][(col+piece.col)/2] = 0
            return self.board[row][col]
        return None

    def create_board(self):
        for row in range(8):
            self.board.append([])
            for col in range(8):
                if col % 2 == (row+1) % 2:
                    if row < 3:
                        self.board[row].append(Piece(row, col, 1))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, 2))
                    else:
                        self.board[row].append(None)
                else:
                    self.board[row].append(None)

class Game:
    def __init__(self):
        self.board_class = Board()
        self.board = self.board_class.board
        self.current_player = 1
        self.saved_piece = None
        self.done = False
        self.won = None

    def play_game(self):

        while not self.done
            if not self.are_pieces:
                self.done = True
            else:
                self.saved_piece = None
                captures = self.all_captures()
                if not captures == []:
                    #make player choose
                    #self.saved_piece = user input
                    #move piece
                    while self.saved_piece is not None:
                        #if can_promote(saved_piece) saved_piece.promote
                        captures = self.captures_by_piece(self.saved_piece)
                        if not captures == []:
                            # make player choose
                            # self.saved_piece = user input
                            # move piece
                        else:
                            self.saved_piece = None
                else:
                    if self.are_adjacent_moves():
                        # make player enter some stuff
                        # self.saved_piece = user input
                        # move piece
                    else:
                        self.done = True
            self.change_turn()
        self.end_message()

    def can_promote(self, piece):
        if piece.row == 7 or piece.row == 0:
            return True
        return False
    def end_message(self):
        print(f"Player {self.current_player} has won!")


    def move_piece(self, piece, row, col):
        self.saved_piece = self.board_class(piece, row, col)


    def are_pieces(self):
        if self.current_player == 1 and self.board.play1_pieces == 0:
            return False
        if self.current_player == 2 and self.board.play2_pieces == 0:
            return False
        return True

    def change_turn(self):
        self.current_player = 3 - self.current_player

    def all_captures(self):
        captures = []
        for r in range(8):
            for c in range(8):
                if self.board[r][c] != 0:
                    if self.board[r][c].player == self.current_player:
                        captures += self.captures_by_piece(self.board[r][c])
        return captures

    def captures_for_piece(self, piece):
        row = piece.row
        col = piece.col
        captures = []
        if piece.player == 1 or piece.is_king:
            if row + 2 < 8 and col + 2 < 8:
                captures += [self.captures_in_a_direction(row, col, 1, 1)]
            if row + 2 < 8 and col - 2 > 0:
                captures += [self.captures_in_a_direction(row, col, 1, -1)]
        if piece.player == 2 or piece.is_king:
            if row - 2 > 0 and col + 2 < 8:
                captures += [self.captures_in_a_direction(row, col, -1, 1)]
            if row - 2 > 0 and col - 2 > 0:
                captures += [self.captures_in_a_direction(row, col, -1, -1)]
        return captures

    def captures_in_a_direction(self, start_row, start_col, step_row, step_col):
        if self.board[start_row+step_row][start_col +step_col] == 3 - self.current_player:
            if self.board[start_row+2*step_row][start_col +2*step_col] is None:
                return [(start_row, start_col),(start_row+2*step_row, start_col +2*step_col)]
        return []

    def are_adjacent_moves(self):
        for r in range(8):
            for c in range(8):
                if self.board[r][c] is not None:
                    piece = self.board[r][c]
                    if piece.player == 1 or piece.is_king:
                        if r + 1 < 8 and c + 1 < 8:
                            if self.board[r+1][c+1] == 0:
                                return True
                        if r + 1 < 8 and c - 1 > 0:
                            if self.board[r + 1][c - 1] == 0:
                                return True
                    if piece.player == 2 or piece.is_king:
                        if r - 1 > 0 and c + 1 < 8:
                            if self.board[r - 1][c + 1] == 0:
                                return True
                        if r - 1 > 0 and c - 1 > 0:
                            if self.board[r - 1][c - 1] == 0:
                                return True
        return False

game = Game()
game.play_game()