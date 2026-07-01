import sys

from PySide6.QtWidgets import QApplication

from interface.ficha_personagem import FichaPersonagem

app = QApplication(sys.argv)

janela = FichaPersonagem()
janela.show()

app.exec()