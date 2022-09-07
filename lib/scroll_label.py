from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QScrollArea


class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        self.setWidgetResizable(True)

        self.content = QWidget(self)
        self.setWidget(self.content)

        layout = QVBoxLayout(self.content)

        self.label = QLabel(self.content)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)

        layout.addWidget(self.label)

    def set_text(self, text):
        self.label.setText(text)

    def set_object_name(self, name):
        self.setObjectName(name)
        self.content.setObjectName(f"{name}-text")
        self.label.setObjectName(name)

    def setFont(self, font):
        self.label.setFont(font)
