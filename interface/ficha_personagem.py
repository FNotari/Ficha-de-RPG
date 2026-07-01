from pathlib import Path
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPixmap


class FichaPersonagem(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
    #Titulo da janela
        self.setWindowTitle("Ficha de Persoangem")
        
        #Caminho da imagem
        caminho_imagem = (Path(__file__).parent/"imagens"/"pagina1.png")
        
        #Carregar imagem
        imagem = QPixmap(str(caminho_imagem))
        
        # Redimensiona a imagem para uma largura de 900 pixels,
        # mantendo a proporção.
        imagem = imagem.scaledToWidth(900)
        
        #Criar um componente para mostrar a imagem
        self.ficha = QLabel(self)
        
        self.ficha.setPixmap(imagem)
        
        #Ajustar o tamnho da janela a imagem
        self.resize(imagem.width(), imagem.height())    