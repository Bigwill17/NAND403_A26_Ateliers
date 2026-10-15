import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QTextEdit,
    QLabel,
    QHBoxLayout
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(330)
        self.build_ui()
    
    def build_ui(self):
        v_layout = QVBoxLayout(self)

        #Ajout de la zone où l'utilisateur inquera le nombre d'objets à créer
        number_objects_layout = QHBoxLayout()

        number_objects_text = QLabel()
        number_objects_text.setText("Number of objects")
        number_objects_layout.addWidget(number_objects_text)

        number_objects_textedit = QTextEdit()
        number_objects_textedit.setFixedHeight(30)
        number_objects_textedit.setFixedWidth(100)
        number_objects_layout.addWidget(number_objects_textedit)

        blank_text = QLabel()
        blank_text.setText("")
        number_objects_layout.addWidget(blank_text)

        #Ajout des textes "Min" et "Max"
        min_max_layout = QHBoxLayout()

        min_max_layout.addWidget(blank_text)

        min_text = QLabel()
        min_text.setText("Min")
        min_max_layout.addWidget(min_text)

        max_text = QLabel()
        max_text.setText("Max")
        min_max_layout.addWidget(max_text)

        #Ajout des TextEdit pour le min et max de la position X
        position_x_layout = QHBoxLayout()

        position_x_text = QLabel()
        position_x_text.setText("Position X")
        position_x_layout.addWidget(position_x_text)

        min_x_textedit = QTextEdit()
        min_x_textedit.setFixedHeight(30)
        min_x_textedit.setFixedWidth(100)
        position_x_layout.addWidget(min_x_textedit)

        max_x_textedit = QTextEdit()
        max_x_textedit.setFixedHeight(30)
        max_x_textedit.setFixedWidth(100)
        position_x_layout.addWidget(max_x_textedit)

        #Ajout des TextEdit pour le min et max de la position Y
        position_y_layout = QHBoxLayout()

        position_y_text = QLabel()
        position_y_text.setText("Position Y")
        position_y_layout.addWidget(position_y_text)

        min_y_textedit = QTextEdit()
        min_y_textedit.setFixedHeight(30)
        min_y_textedit.setFixedWidth(100)
        position_y_layout.addWidget(min_y_textedit)

        max_y_textedit = QTextEdit()
        max_y_textedit.setFixedHeight(30)
        max_y_textedit.setFixedWidth(100)
        position_y_layout.addWidget(max_y_textedit)

        #Ajout des TextEdit pour le min et max de la position Z
        position_z_layout = QHBoxLayout()

        position_z_text = QLabel()
        position_z_text.setText("Position Z")
        position_z_layout.addWidget(position_z_text)

        min_z_textedit = QTextEdit()
        min_z_textedit.setFixedHeight(30)
        min_z_textedit.setFixedWidth(100)
        position_z_layout.addWidget(min_z_textedit)

        max_z_textedit = QTextEdit()
        max_z_textedit.setFixedHeight(30)
        max_z_textedit.setFixedWidth(100)
        position_z_layout.addWidget(max_z_textedit)

        #Ajout des TextEdit pour le scale des objets
        scale_layout = QHBoxLayout()

        scale_text = QLabel()
        scale_text.setText("Scale")
        scale_layout.addWidget(scale_text)

        min_scale_textedit = QTextEdit()
        min_scale_textedit.setFixedHeight(30)
        min_scale_textedit.setFixedWidth(100)
        scale_layout.addWidget(min_scale_textedit)

        max_scale_textedit = QTextEdit()
        max_scale_textedit.setFixedHeight(30)
        max_scale_textedit.setFixedWidth(100)
        scale_layout.addWidget(max_scale_textedit)

        #Ajout de tous les layout horizontaux dans le principal layout vertical
        v_layout.addLayout(number_objects_layout)
        v_layout.addLayout(min_max_layout)
        v_layout.addLayout(position_x_layout)
        v_layout.addLayout(position_y_layout)
        v_layout.addLayout(position_z_layout)
        v_layout.addLayout(scale_layout)

        #Ajout du bouton pour créer les objets
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        v_layout.addWidget(self.create_button)

    def create_object(self):
        forme = random.choice(["cube", "cylindre", "sphere"])

        if forme == "cube":
            objet = cmds.polyCube()[0]
        elif forme == "cylindre":
            objet = cmds.polyCylinder()[0]
        else:
            objet = cmds.polySphere()[0]

        random_value = random.uniform(-10, 10)
        cmds.move(random_value, random_value, random_value, objet)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()