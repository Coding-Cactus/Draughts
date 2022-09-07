from lib.tile import Tile
from lib.pages import Pages
from lib.coord import Coord
from lib.tile_grid import TileGrid
from lib.scroll_label import ScrollLabel

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
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

        self.labels = []

        self.setWindowTitle(self.title)

        self.layout = QGridLayout(self.centralWidget)
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignCenter)

        self.__set_page(Pages.HOME)

        self.showMaximized()

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        self.resize_content()        
    
    def resize_content(self):
        dims = self.centralWidget.size()
        width, height = dims.width(), dims.height()

        self.tile_grid.resize_tiles((min(width, height) - 200) / 8)

        for label in self.labels:
            label["label"].setFont(QFont("", label["vh"] / 100 * height))
            label["label"].adjustSize()

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

        self.labels.append({
            "label": title,
            "vh": 7
        })

        pvp_button = QPushButton("USER VS USER")
        pvp_button.setObjectName("home")
        pvp_button.clicked.connect(lambda: self.__set_page(Pages.PLAYING))

        self.labels.append({
            "label": pvp_button,
            "vh": 3
        })

        how_button = QPushButton("HOW TO PLAY")
        how_button.setObjectName("home")
        how_button.clicked.connect(lambda: self.__set_page(Pages.HOW_TO_PLAY))

        self.labels.append({
            "label": how_button,
            "vh": 3
        })

        self.layout.addWidget(title, 0, 0)
        self.layout.addWidget(pvp_button, 1, 0)
        self.layout.addWidget(how_button, 2, 0)

        self.setLayout(self.layout)        
        self.resize_content()

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
        self.resize_content()

    def game_over(self, winner):
        self.__set_page([Pages.PLAYER1_WIN, Pages.PLAYER2_WIN][winner - 1])

    def __show_win_page(self, winner):
        title = QLabel(f"PLAYER {winner}\nWINS!")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignHCenter)

        self.labels.append({
            "label": title,
            "vh": 7
        })

        play_button = QPushButton("PLAY AGAIN")
        play_button.setObjectName("home")
        play_button.clicked.connect(lambda: self.__set_page(Pages.PLAYING))

        self.labels.append({
            "label": play_button,
            "vh": 3
        })

        home_button = QPushButton("HOME")
        home_button.setObjectName("home")
        home_button.clicked.connect(lambda: self.__set_page(Pages.HOME))

        self.labels.append({
            "label": home_button,
            "vh": 3
        })

        self.layout.addWidget(title, 0, 0)
        self.layout.addWidget(play_button, 1, 0)
        self.layout.addWidget(home_button, 2, 0)

        self.setLayout(self.layout)        
        self.resize_content()

    def __show_how_page(self):
        title = QLabel("HOW TO PLAY")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignHCenter)

        self.labels.append({
            "label": title,
            "vh": 7
        })

        content = ScrollLabel()
        content.set_text("""
• Each player takes turn playing a move

• To move, click on a piece and then click on its destination tile

• For a move to be valid, you must either capture a piece, or travel to an adjacent diagonal square. Down the board if you are player 1 or up the board if you are player 2

• If during your turn you are able to capture, you must capture

• To capture an enemy piece, they must be diagonally adjacent to your piece with an empty square diagonally behind them in a straight line in the correct direction (up or down the board)

• When a piece is captured, it is removed from the board

• If directly after a capture, you can capture another enemy piece with the newly positioned piece, then you must capture again with that piece

• When your piece reaches the other end of the board, it becomes a king piece. This means that it can then move in any diagonal direction from now on.

• To win the game, you must capture all of the enemy's pieces or block all of the enemy's pieces from moving
"""[1:-1])
        content.set_object_name("content")

        self.labels.append({
            "label": content,
            "vh": 2.5
        })

        home_button = QPushButton("HOME")
        home_button.setObjectName("how")
        home_button.clicked.connect(lambda: self.__set_page(Pages.HOME))

        self.labels.append({
            "label": home_button,
            "vh": 3
        })

        self.layout.addWidget(title, 0, 0)
        self.layout.addWidget(content, 1, 0)
        self.layout.addWidget(home_button, 2, 0)

        self.setLayout(self.layout)        
        self.resize_content()

    def __clear_page(self):
        for i in reversed(range(self.layout.count())):
            w = self.layout.itemAt(i).widget()
            self.layout.removeWidget(w)
            w.setParent(None)

        self.labels = []
