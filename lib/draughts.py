from lib.pages import Pages
from lib.coord import Coord
from lib.tile_grid import TileGrid
from lib.tile import Tile

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout


class Draughts(QMainWindow):
    def __init__(self, width, height):
        super().__init__()

        self.WIDTH  = width
        self.HEIGHT = height

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.top   = 0
        self.left  = 0
        self.title = "Draughts"

        self.tile_grid = TileGrid(self)

        self.setWindowTitle(self.title)

        self.layout = QGridLayout(self.centralWidget)
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignCenter)

        self.__set_page(Pages.HOME)

        self.showMaximized()

    def __set_page(self, page):
        self.__clear_page()

        if page == Pages.HOME:
            self.__show_home_page()
        elif page == Pages.PLAYING:
            self.__show_play_page()
        elif page == Pages.PLAYER1_WIN:
            self.__show_win_page(1)
        elif page == Pages.PLAYER2_WIN:
            self.__show_win_page(2)
        elif page == Pages.HOW_TO_PLAY:
            self.__show_how_page()

    def __show_home_page(self):
        title = QLabel("DRAUGHTS")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignHCenter)

        pvp_button = QPushButton("USER VS USER")
        pvp_button.setObjectName("home")
        pvp_button.clicked.connect(lambda: self.__set_page(Pages.PLAYING))

        how_button = QPushButton("HOW TO PLAY")
        how_button.setObjectName("home")
        how_button.clicked.connect(lambda: self.__set_page(Pages.HOW_TO_PLAY))

        self.layout.addWidget(title, 0, 0)
        self.layout.addWidget(pvp_button, 1, 0)
        self.layout.addWidget(how_button, 2, 0)

        self.setLayout(self.layout)

    def __show_play_page(self):
        self.tile_grid.current_turn = 1

        dims = self.centralWidget.size()
        width, height = dims.width(), dims.height()

        size = (min(width, height) - 200) // 8

        for y in range(8):
            for x in range(8):
                tile = Tile(Coord(x, y), size)
                self.tile_grid.set_tile(tile, Coord(x, y))
                self.layout.addWidget(tile, y, x)

        self.setLayout(self.layout)

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)

        dims = self.centralWidget.size()
        width, height = dims.width(), dims.height()

        self.tile_grid.resize_tiles((min(width, height) - 200) / 8)

    def game_over(self, winner):
        self.__set_page([Pages.PLAYER1_WIN, Pages.PLAYER2_WIN][winner - 1])

    def __show_win_page(self, winner):
        title = QLabel(f"PLAYER {winner}\nWINS!")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignHCenter)

        play_button = QPushButton("PLAY AGAIN")
        play_button.setObjectName("home")
        play_button.clicked.connect(lambda: self.__set_page(Pages.PLAYING))

        home_button = QPushButton("HOME")
        home_button.setObjectName("home")
        home_button.clicked.connect(lambda: self.__set_page(Pages.HOME))

        self.layout.addWidget(title, 0, 0)
        self.layout.addWidget(play_button, 1, 0)
        self.layout.addWidget(home_button, 2, 0)

        self.setLayout(self.layout)

    def __show_how_page(self):
        title = QLabel("HOW TO PLAY")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignHCenter)

        content = QLabel("""
- Each player takes turn playing a move
- On your move, if no other piece is in a piece’s path and the path lies on the board, you can move a Piece diagonally one square
- You can never move a friendly piece over a friendly piece, and likewise for the opponent
- If a blocking enemy piece, on your turn, has an empty space directly behind the piece and inline with the path, then you can capture it, and move your piece behind the captured enemy piece
- If directly after a capture, you can capture another enemy piece, then you must capture again
- If at any point you can capture, you must capture, however you can choose what to capture in a turn.
""")
        content.setWordWrap(True)

        home_button = QPushButton("HOME")
        home_button.setObjectName("how")
        home_button.clicked.connect(lambda: self.__set_page(Pages.HOME))

        self.layout.addWidget(title, 0, 0)
        self.layout.addWidget(content, 1, 0)
        self.layout.addWidget(home_button, 2, 0)

        self.setLayout(self.layout)

    def __clear_page(self):
        for i in reversed(range(self.layout.count())):
            w = self.layout.itemAt(i).widget()
            self.layout.removeWidget(w)
            w.setParent(None)

