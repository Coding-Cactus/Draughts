class Piece:
    def __init__(self, tile, player):
        self.tile = tile
        self.player = player
        self.is_king = False

    def move_to(self, tile):
        self.tile.remove_piece()

        if (tile.coord.y == 7 and self.player == 1) or (tile.coord.y == 0 and self.player == 2):
            self.is_king = True

        self.tile = tile
        tile.place_piece(self)
