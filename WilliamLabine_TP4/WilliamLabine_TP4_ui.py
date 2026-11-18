import os
import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSpinBox, QGroupBox, QGridLayout
import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance
from PySide6.QtCore import Qt

#Fonction pour mettre la fenêtre always on top
def maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(pointer), QWidget)

#On trouve le path du dossier dans lequel se trouve ce même fichier
absolute_folder_path = os.path.dirname(os.path.abspath(__file__))

#On ajoute le path aux paths auxquels sys a accès
sys.path.append(absolute_folder_path)

#On importe le fichier du ui
import WilliamLabine_TP4_array as array

# #On reload le fichier ui pour que Maya ne perde pas la tête
import importlib
importlib.reload(array)

class BlenderModifiersInMayaUi(QWidget):
    def __init__(self):
        #Initialisation de mon message board avec le contructeur de base
        super().__init__(maya_main_window())
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("Random Animation Generator")
        self.setMinimumWidth(400)
        self.create_ui()

    #On génère une animation random selon les données entrées
    def make_array_in_a_line(self):
        array.make_array_in_a_line()

    def make_array_in_circle(self):
        array.make_array_in_circle()

    def create_ui(self):
        
        #Crée un QSpinBox et le place dans un QHBoxLayout
        def create_spinbox(gridlayout, row, column):
            self = QSpinBox()
            self.setRange(-9999, 9999)
            gridlayout.addWidget(self, row, column)
            return self

        #Crée un QLabel qui servira de titre et le place dans un QHBoxLayout
        def create_label(text, gridlayout, row, column):
            self = QLabel(text)
            gridlayout.addWidget(self, row, column)
            return self

        #Crée un QGroupBox dans lequel on met le layout hbox, et on l'ajoute à la liste des groupbox
        def create_groupbox(title, gridlayout):
            self = QGroupBox(title)
            self.setLayout(gridlayout)
            groupbox_list.append(self)
            return self

        #Création du layout de mon board
        layout = QVBoxLayout(self)

        #Création du tableau de QGroupBox qui seront utilisés plus tard
        groupbox_list = []

        #On ajoute le bouton pour faire un array en ligne droite
        #====================================================================================================
        generate_button = QPushButton("Make Array In A Line")
        generate_button.clicked.connect(self.make_array_in_a_line)


        #On ajoute le bouton pour faire un array en cercle
        #====================================================================================================
        delete_keys_button = QPushButton("Make Array In Circle")
        delete_keys_button.clicked.connect(self.make_array_in_circle)


        #On ajoute tous les layout horizontaux dans le vertical
        #====================================================================================================
        for groupbox in groupbox_list:
            layout.addWidget(groupbox)

        layout.addWidget(generate_button)
        layout.addWidget(delete_keys_button)