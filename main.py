import sys

from lib import Draughts
from lib import stylesheet

from PyQt5.QtWidgets import QApplication


a = lambda: abc
if __name__ == "__main__":
    sys.excepthook = a
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    ex = Draughts(600, 600)
    sys.exit(app.exec_())