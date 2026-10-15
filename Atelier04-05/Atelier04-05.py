import random
from maya import cmds
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTextEdit, QLabel, QHBoxLayout

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(330)
        self.build_ui()
    
    def build_ui(self):

        def create_object(self):

            #Initialisation de mes variables provenant des textedit, si rien n'est écrit dans les textedit, on met une valeur par défaut
            if (number_objects_textedit.toPlainText() == ""):
                number_of_objects = 1
            else:
                number_of_objects = int(number_objects_textedit.toPlainText())

            if (min_x_textedit.toPlainText() == ""):
                min_x = 0
            else:
                min_x = float(min_x_textedit.toPlainText())

            if (max_x_textedit.toPlainText() == ""):
                max_x = 0
            else:
                max_x = float(max_x_textedit.toPlainText())

            if (min_y_textedit.toPlainText() == ""):
                min_y = 0
            else:
                min_y = float(min_y_textedit.toPlainText())

            if (max_y_textedit.toPlainText() == ""):
                max_y = 0
            else:
                max_y = float(max_y_textedit.toPlainText())

            if (min_z_textedit.toPlainText() == ""):
                min_z = 0
            else:
                min_z = float(min_z_textedit.toPlainText())

            if (max_z_textedit.toPlainText() == ""):
                max_z = 0
            else:
                max_z = float(max_z_textedit.toPlainText())

            if (min_scale_textedit.toPlainText() == ""):
                min_scale = 1
            else:
                min_scale = float(min_scale_textedit.toPlainText())

            if (max_scale_textedit.toPlainText() == ""):
                max_scale = 1
            else:
                max_scale = float(max_scale_textedit.toPlainText())

            #On fait une boucle égal au number of objects
            for i in range(number_of_objects):
                forme = random.choice(["cube", "cylindre", "sphere"])
                if forme == "cube":
                    objet = cmds.polyCube()[0]
                elif forme == "cylindre":
                    objet = cmds.polyCylinder()[0]
                else:
                    objet = cmds.polySphere()[0]

                #On met une valeur aléatoire dans les positions x, y et z et le scale selon le min et max donnés
                random_x = random.uniform(min_x, max_x)
                random_y = random.uniform(min_y, max_y)
                random_z = random.uniform(min_z, max_z)
                random_scale = random.uniform(min_scale, max_scale)

                #On déplace les formes et on les scale en conséquence
                cmds.move(random_x, random_y, random_z, objet)
                cmds.scale(random_scale, random_scale, random_scale, objet)

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
        self.create_button.clicked.connect(create_object)
        v_layout.addWidget(self.create_button)

def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()