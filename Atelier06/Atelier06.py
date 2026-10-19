import random
from maya import cmds
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTextEdit, QLabel, QHBoxLayout
from contextlib import contextmanager

#Création de la fonction spéciale qui ouvre et ferme un "chunk" avec toutes les lignes de codes choisies
@contextmanager
def ctrlz_chunk():
    #On ouvre le chunk au début
    cmds.undoInfo(openChunk=True)
    try:
        yield
    finally:
        #On s'assure de refermer le chunk!
        cmds.undoInfo(closeChunk=True)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 6")
        self.setMinimumWidth(220)
        self.build_ui()
    
    def build_ui(self):

        def create_fence(self):

            #En utilisant le chunk de control Z, on active toutes nos fonctionnalités
            with ctrlz_chunk():
            
                #Initialisation de mes variables provenant des textedit, si rien n'est écrit dans les textedit, on met une valeur par défaut
                if (number_v_poles_textedit.toPlainText() == ""):
                    number_v_poles = 1
                else:
                    number_v_poles = int(number_v_poles_textedit.toPlainText())

                if (hauteur_v_poles_textedit.toPlainText() == ""):
                    hauteur_v_poles = 100
                else:
                    hauteur_v_poles = float(hauteur_v_poles_textedit.toPlainText())

                if (largeur_v_poles_textedit.toPlainText() == ""):
                    largeur_v_poles = 5
                else:
                    largeur_v_poles = float(largeur_v_poles_textedit.toPlainText())

                if (number_h_poles_textedit.toPlainText() == ""):
                    number_h_poles = 2
                else:
                    number_h_poles = int(number_h_poles_textedit.toPlainText())

                if (longueur_h_poles_textedit.toPlainText() == ""):
                    longueur_h_poles = 100
                else:
                    longueur_h_poles = float(longueur_h_poles_textedit.toPlainText())

                if (largeur_h_poles_textedit.toPlainText() == ""):
                    largeur_h_poles = 3
                else:
                    largeur_h_poles = float(largeur_h_poles_textedit.toPlainText())

                #On fait apparaitre le premier pole
                pole01 = cmds.polyCube()[0]
                cmds.scale(largeur_v_poles, hauteur_v_poles, largeur_v_poles, pole01)

                #On fait une boucle pour les poles verticales
                for i in range(number_v_poles - 1):
                    v_pole = cmds.polyCube()[0]

                    #On déplace les formes et on les scale en conséquence
                    cmds.move((i + 1) * longueur_h_poles, 0, 0, v_pole)
                    cmds.scale(largeur_v_poles, hauteur_v_poles, largeur_v_poles, v_pole)

                    #On fait une boucle pour les poles horizontales
                    for j in range(number_h_poles):
                        h_pole = cmds.polyCube()[0]

                        #On déplace les formes et on les scale en conséquence
                        cmds.move((longueur_h_poles * i) + longueur_h_poles / 2, ((hauteur_v_poles / 2) / (number_h_poles)) * j - largeur_h_poles, 0, h_pole)
                        cmds.scale(longueur_h_poles, largeur_h_poles, largeur_h_poles, h_pole)

        v_layout = QVBoxLayout(self)

        #Ajout de la zone où l'utilisateur inquera le nombre de poles verticales à créer
        number_v_poles_layout = QHBoxLayout()

        number_v_poles_text = QLabel()
        number_v_poles_text.setText("Nombre de poles verticales")
        number_v_poles_layout.addWidget(number_v_poles_text)

        number_v_poles_textedit = QTextEdit()
        number_v_poles_textedit.setFixedHeight(30)
        number_v_poles_textedit.setFixedWidth(100)
        number_v_poles_layout.addWidget(number_v_poles_textedit)

        #Ajout des TextEdit pour la hauteur des poles verticales
        hauteur_v_poles_layout = QHBoxLayout()

        hauteur_v_poles_text = QLabel()
        hauteur_v_poles_text.setText("Hauteur des poles verticales")
        hauteur_v_poles_layout.addWidget(hauteur_v_poles_text)

        hauteur_v_poles_textedit = QTextEdit()
        hauteur_v_poles_textedit.setFixedHeight(30)
        hauteur_v_poles_textedit.setFixedWidth(100)
        hauteur_v_poles_layout.addWidget(hauteur_v_poles_textedit)

        #Ajout des TextEdit pour la largeur des poles verticales
        largeur_v_poles_layout = QHBoxLayout()

        largeur_v_poles_text = QLabel()
        largeur_v_poles_text.setText("Largeur des poles verticales")
        largeur_v_poles_layout.addWidget(largeur_v_poles_text)

        largeur_v_poles_textedit = QTextEdit()
        largeur_v_poles_textedit.setFixedHeight(30)
        largeur_v_poles_textedit.setFixedWidth(100)
        largeur_v_poles_layout.addWidget(largeur_v_poles_textedit)

        #Ajout d'un layout blank pour bien organiser le board
        blank_layout = QHBoxLayout()

        blank_text = QLabel()
        blank_text.setText("")
        blank_layout.addWidget(blank_text)

        #Ajout de la zone où l'utilisateur inquera le nombre de poles horizontales à créer
        number_h_poles_layout = QHBoxLayout()

        number_h_poles_text = QLabel()
        number_h_poles_text.setText("Nombre de poles horizontales")
        number_h_poles_layout.addWidget(number_h_poles_text)

        number_h_poles_textedit = QTextEdit()
        number_h_poles_textedit.setFixedHeight(30)
        number_h_poles_textedit.setFixedWidth(100)
        number_h_poles_layout.addWidget(number_h_poles_textedit)

        #Ajout des TextEdit pour la hauteur des poles
        longueur_h_poles_layout = QHBoxLayout()

        longueur_h_poles_text = QLabel()
        longueur_h_poles_text.setText("Longueur des poles horizontales")
        longueur_h_poles_layout.addWidget(longueur_h_poles_text)

        longueur_h_poles_textedit = QTextEdit()
        longueur_h_poles_textedit.setFixedHeight(30)
        longueur_h_poles_textedit.setFixedWidth(100)
        longueur_h_poles_layout.addWidget(longueur_h_poles_textedit)

        #Ajout des TextEdit pour la largeur des poles horizontales
        largeur_h_poles_layout = QHBoxLayout()

        largeur_h_poles_text = QLabel()
        largeur_h_poles_text.setText("Largeur des poles horizontales")
        largeur_h_poles_layout.addWidget(largeur_h_poles_text)

        largeur_h_poles_textedit = QTextEdit()
        largeur_h_poles_textedit.setFixedHeight(30)
        largeur_h_poles_textedit.setFixedWidth(100)
        largeur_h_poles_layout.addWidget(largeur_h_poles_textedit)

        #Ajout de tous les layout horizontaux dans le principal layout vertical
        v_layout.addLayout(number_v_poles_layout)
        v_layout.addLayout(hauteur_v_poles_layout)
        v_layout.addLayout(largeur_v_poles_layout)
        v_layout.addLayout(blank_layout)
        v_layout.addLayout(number_h_poles_layout)
        v_layout.addLayout(longueur_h_poles_layout)
        v_layout.addLayout(largeur_h_poles_layout)

        #Ajout du bouton pour créer les objets
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(create_fence)
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