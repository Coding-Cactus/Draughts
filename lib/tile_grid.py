class TileGrid:
    def __init__(self, app):
        self.draughts_app = app

        self.tiles = [[None for _ in range(8)] for _ in range(8)]
        self.active_tile = None  # Currently selected tile (for use in movement)
        self.current_turn = 1
        self.turn_continuation = None

    def get_tile(self, coord):
        return self.tiles[coord.y][coord.x]

    def set_tile(self, tile, coord):
        self.tiles[coord.y][coord.x] = tile

        tile.clicked.connect(lambda: tile.on_click(self))

    def resize_tiles(self, size):
        for row in self.tiles:
            for tile in row:
                if tile is not None:
                    tile.resize(size)

    def next_turn(self):
        self.current_turn = self.current_turn % 2 + 1

        game_over = True
        for row in self.tiles:
            for tile in row:
                if (
                        tile.piece is not None and tile.piece.player == self.current_turn
                        and len(tile.possible_moves(self)) != 0
                ):
                    game_over = False
                    break

            if not game_over:
                break

        if game_over:
            self.draughts_app.game_over(self.current_turn % 2 + 1)

        return self.current_turn

    def possible_captures(self):
        captures = {}

        for row in self.tiles:
            for tile in row:
                if not tile.playable or tile.piece is None or tile.piece.player != self.current_turn:
                    continue

                possibles = tile.possible_captures(self)

                if len(possibles) != 0:
                    captures[(tile.coord.x, tile.coord.y)] = possibles

        return captures
