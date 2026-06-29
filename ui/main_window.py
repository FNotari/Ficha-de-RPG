from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QWidget,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QVBoxLayout,
    QFormLayout,
    QMenuBar
)
from models.data_loader import load_classes, load_race


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ficha D&D 5e")
        self.resize(1200, 800)

       #Widget central(obrigatório o QMainWindow)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        #layout Principal
        layout = QVBoxLayout()
        
        #Menu
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Arquivo")
        edit_menu = menu_bar.addMenu("Editar")
        help_menu = menu_bar.addMenu("Ajuda")
        
        # Formulário
        form = QFormLayout()
        
        #Nome
        self.name_input = QLineEdit()
        form.addRow("Nome do Personagem", self.name_input)
        
        #Classe
        self.class_input = QComboBox()
        self.class_input.addItems(load_classes())
        form.addRow("Classe:", self.class_input)
        
        #Raça
        self.race_input = QComboBox()
        self.race_input.addItems(load_race())
        form.addRow("Raça:", self.race_input)
        
        #Nível
        self.level_input = QSpinBox()
        self.level_input.setRange(1, 20)
        self.level_input.setValue(1)
        form.addRow("Nível:", self.level_input)
        
        #Adiciona o formulário ao Layuot
        layout.addLayout(form)
        
        #Aplica layout no widget central
        central_widget.setLayout(layout)