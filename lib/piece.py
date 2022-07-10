class Piece:
    def __init__(self, tile, player):
        self.tile = tile
        self.player = player

    def move_to(self, tile):
        self.tile.remove_piece()

        self.tile = tile
        tile.place_piece(self.player)
