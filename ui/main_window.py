from PySide6.QtWidgets import (
    QMainWindow,
    QLabel
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ficha D&D 5e")

        self.resize(1200, 800)

        texto = QLabel("Bem-vindo ao Gerador de Fichas D&D 5e", self)

        texto.move(20, 20)