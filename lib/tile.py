from lib.coord import Coord
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
            self.place_piece(Piece(self, 1))
        elif self.playable and coord.y > 4:
            self.place_piece(Piece(self, 2))

    def place_piece(self, piece, status=""):
        self.piece = piece
        self.__set_background(status)

    def remove_piece(self):
        self.setStyleSheet("")
        self.piece = None

    def __set_background(self, suffix=""):
        king = "_king" if self.piece.is_king else ""
        suffix = "_" + suffix if suffix != "" else ""

        self.setStyleSheet(f"background-image: url(imgs/player{self.piece.player}{king}{suffix}.png)")

    def on_click(self, tile_grid):
        if (
                self.piece is not None and self.piece.player == tile_grid.current_turn
                and tile_grid.turn_continuation in [None, self]
        ):
            if tile_grid.active_tile is not None:
                tile_grid.active_tile.__set_background()

            tile_grid.active_tile = self
            self.__set_background("active")

            return

        possible_captures = tile_grid.possible_captures()
        con = tile_grid.turn_continuation
        if con is not None:
            possible_captures = { (con.coord.x, con.coord.y): possible_captures[(con.coord.x, con.coord.y)] }

        if self.is_valid_move(tile_grid, possible_captures):
            for x, y in possible_captures:
                tile_grid.get_tile(Coord(x, y)).__set_background()

            captured = self.complete_capture(tile_grid)

            tile_grid.active_tile.piece.move_to(self)
            tile_grid.active_tile = None

            if not captured or (self.coord.x, self.coord.y) not in tile_grid.possible_captures():
                tile_grid.turn_continuation = None
                tile_grid.next_turn()
            else:
                tile_grid.active_tile = self
                tile_grid.turn_continuation = self
                self.__set_background("active")
        else:
            if tile_grid.active_tile is not None:
                tile_grid.active_tile.__set_background()
                tile_grid.active_tile = None

                for x, y in possible_captures:
                    tile_grid.get_tile(Coord(x, y)).__set_background("red")

    def is_valid_move(self, tile_grid, possible_captures):
        active = tile_grid.active_tile

        # null checks
        if not self.playable or self.piece is not None or active is None:
            return False

        # capture check
        if len(possible_captures) != 0:
            return (active.coord.x, active.coord.y) in possible_captures and \
                   self.coord in possible_captures[(active.coord.x, active.coord.y)]

        # movement check
        directions = [-1, 1]
        if not active.piece.is_king:
            directions.remove(-1 if tile_grid.current_turn == 1 else 1)

        return self.coord.y - active.coord.y in directions and abs(self.coord.x - active.coord.x) == 1

    def complete_capture(self, tile_grid):
        active_coord = tile_grid.active_tile.coord

        if abs(active_coord.x - self.coord.x) == 2:
            tile_grid.get_tile(
                Coord(int((active_coord.x + self.coord.x) / 2), int((active_coord.y + self.coord.y) / 2))
            ).remove_piece()

            return True

        return False

    def possible_captures(self, tile_grid):
        captures = []

        left_bound = self.coord.x if self.coord.x < 2 else self.coord.x - 2
        right_bound = self.coord.x if self.coord.x > len(tile_grid.tiles) - 3 else self.coord.x + 2

        bottom_bound = self.coord.y - 2 \
            if self.coord.y > 1 and (self.piece.is_king or tile_grid.current_turn == 2) \
            else self.coord.y
        top_bound = self.coord.y + 2 \
            if self.coord.y < len(tile_grid.tiles) - 2 and (self.piece.is_king or tile_grid.current_turn == 1) \
            else self.coord.y

        for x, y in [
            (left_bound, top_bound),
            (right_bound, top_bound),
            (right_bound, bottom_bound),
            (left_bound, bottom_bound)
        ]:
            if x == self.coord.x or y == self.coord.y or tile_grid.tiles[y][x].piece is not None:
                continue

            tile = tile_grid.get_tile(Coord(int((x + self.coord.x) / 2), int((y + self.coord.y) / 2)))

            if tile.piece is not None and tile.piece.player != tile_grid.current_turn:
                captures.append(Coord(x, y))

        return captures
