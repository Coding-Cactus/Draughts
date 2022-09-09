import os
import sys

from lib import Draughts
from lib import stylesheet

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = u'qtpys.draughts.pvp.1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

BASE_DIR = os.path.dirname(__file__)

# a = lambda: abc
if __name__ == "__main__":
    # sys.excepthook = a
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    app.setWindowIcon(QtGui.QIcon(os.path.join(BASE_DIR, "imgs/favicon.ico").replace("\\", "/")))
    ex = Draughts(600, 600)
    sys.exit(app.exec_())
