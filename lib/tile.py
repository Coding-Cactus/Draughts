from lib.piece import Piece

from PyQt5.Qt import QSize
from PyQt5.QtWidgets import QPushButton


class Tile(QPushButton):
    def __init__(self, coord, width, height):
        super(Tile, self).__init__()

        self.piece = None
        self.coord = coord
        self.playable = (coord.y + coord.x) % 2 == 0

        suffix = "-active" if self.playable else "-inactive"

        self.setObjectName(f"tile{suffix}")

        self.setMinimumSize(QSize(width, height))
        self.setMaximumSize(QSize(width, height))

        if self.playable and coord.y < 3:
            self.place_piece(1)
        elif self.playable and coord.y > 4:
            self.place_piece(2)

    def place_piece(self, player):
        self.setStyleSheet(f"background-image: url(imgs/player{player}.png)")
        self.piece = Piece(self, player)

    def remove_piece(self):
        self.setStyleSheet("")
        self.piece = None

    def on_click(self, tile_grid):
        if self.piece is not None and self.piece.player == tile_grid.current_turn:
            tile_grid.active_tile = self
        elif self.playable and self.piece is None and tile_grid.active_tile is not None:
            tile_grid.active_tile.piece.move_to(self)
            tile_grid.active_tile = None
            tile_grid.next_turn()
