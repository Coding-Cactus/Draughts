class TileGrid:
    def __init__(self):
        self.tiles = [[None for _ in range(8)] for _ in range(8)]
        self.active_tile = None  # Currently selected tile (for use in movement)
        self.current_turn = 1

    def get_tile(self, coord):
        return self.tiles[coord.y][coord.x]

    def set_tile(self, tile, coord):
        self.tiles[coord.y][coord.x] = tile

        tile.clicked.connect(lambda: tile.on_click(self))

    def next_turn(self):
        self.current_turn = self.current_turn % 2 + 1
        return self.current_turn
