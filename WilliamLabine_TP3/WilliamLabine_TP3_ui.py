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
import WilliamLabine_TP3_animator as animator

# #On reload le fichier ui pour que Maya ne perde pas la tête
import importlib
importlib.reload(animator)

class RandomAnimationUI(QWidget):
    def __init__(self):
        #Initialisation de mon message board avec le contructeur de base
        super().__init__(maya_main_window())
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("Random Animation Generator")
        self.setMinimumWidth(400)
        self.create_ui()
        
    #Crée un QSpinBox et le place dans un QHBoxLayout
    def create_spinbox(self, gridlayout, row, column):
        this_spinbox = QSpinBox()
        this_spinbox.setRange(-9999, 9999)
        gridlayout.addWidget(this_spinbox, row, column)
        return this_spinbox

    #Crée un QLabel qui servira de titre et le place dans un QHBoxLayout
    def create_label(self, text, gridlayout, row, column):
        this_label = QLabel(text)
        gridlayout.addWidget(this_label, row, column)
        return this_label

    #Crée un QGroupBox dans lequel on met le layout hbox, et on l'ajoute à la liste des groupbox
    def create_groupbox(self, title, gridlayout):
        this_groupbox = QGroupBox(title)
        this_groupbox.setLayout(gridlayout)
        self.groupbox_list.append(this_groupbox)
        return this_groupbox
    
    def create_ui(self):

        #Création du layout de mon board
        self.layout = QVBoxLayout(self)

        #Création du tableau de QGroupBox qui seront utilisés plus tard
        self.groupbox_list = []

        #Création de la zone Animation Timing
        #====================================================================================================
        self.timing_grid = QGridLayout()
        self.duration_text = self.create_label("    Duration (Frames):", self.timing_grid, 0, 0)
        self.duration = self.create_spinbox(self.timing_grid, 0, 1)
        self.step_text = self.create_label("    Step (Frames):", self.timing_grid, 0, 2)
        self.step = self.create_spinbox(self.timing_grid, 0, 3)

        #On set la valeur minimum de duration et step à 1, car elles sont les deux seules spinbox qui ne doivent pas aller en dessous de cette valeur
        self.duration.setMinimum(1)
        self.step.setMinimum(1)

        self.animation_groupbox = self.create_groupbox("Animation Timing", self.timing_grid)

        #Création de la zone Translation Parameters
        #====================================================================================================
        self.translation_grid = QGridLayout()
        self.trans_min_x_text = self.create_label("   Min X :", self.translation_grid, 0, 0)
        self.trans_min_x = self.create_spinbox(self.translation_grid, 0, 1)
        self.trans_min_y_text = self.create_label("   Min Y :", self.translation_grid, 0, 2)
        self.trans_min_y = self.create_spinbox(self.translation_grid, 0, 3)
        self.trans_min_z_text = self.create_label("   Min Z :", self.translation_grid, 0, 4)
        self.trans_min_z = self.create_spinbox(self.translation_grid, 0, 5)
        self.trans_max_x_text = self.create_label("   Max X :", self.translation_grid, 1, 0)
        self.trans_max_x = self.create_spinbox(self.translation_grid, 1, 1)
        self.trans_max_y_text = self.create_label("   Max Y :", self.translation_grid, 1, 2)
        self.trans_max_y = self.create_spinbox(self.translation_grid, 1, 3)
        self.trans_max_z_text = self.create_label("   Max Z :", self.translation_grid, 1, 4)
        self.trans_max_z = self.create_spinbox(self.translation_grid, 1, 5)

        self.translation_groupbox = self.create_groupbox("Translation Parameters", self.translation_grid)

        
        #Création de la zone Rotation Parameters
        #====================================================================================================
        self.rotation_grid = QGridLayout()
        self.rot_min_x_text = self.create_label("   Min X :", self.rotation_grid, 0, 0)
        self.rot_min_x = self.create_spinbox(self.rotation_grid, 0, 1)
        self.rot_min_y_text = self.create_label("   Min Y :", self.rotation_grid, 0, 2)
        self.rot_min_y = self.create_spinbox(self.rotation_grid, 0, 3)
        self.rot_min_z_text = self.create_label("   Min Z :", self.rotation_grid, 0, 4)
        self.rot_min_z = self.create_spinbox(self.rotation_grid, 0, 5)
        self.rot_max_x_text = self.create_label("   Max X :", self.rotation_grid, 1, 0)
        self.rot_max_x = self.create_spinbox(self.rotation_grid, 1, 1)
        self.rot_max_y_text = self.create_label("   Max Y :", self.rotation_grid, 1, 2)
        self.rot_max_y = self.create_spinbox(self.rotation_grid, 1, 3)
        self.rot_max_z_text = self.create_label("   Max Z :", self.rotation_grid, 1, 4)
        self.rot_max_z = self.create_spinbox(self.rotation_grid, 1, 5)

        self.rotation_groupbox = self.create_groupbox("Rotation Parameters", self.rotation_grid)


        #Création de la zone Scale Parameters
        #====================================================================================================
        self.scale_grid = QGridLayout()
        self.scale_min_x_text = self.create_label("   Min X :", self.scale_grid, 0, 0)
        self.scale_min_x = self.create_spinbox(self.scale_grid, 0, 1)
        self.scale_min_y_text = self.create_label("   Min Y :", self.scale_grid, 0, 2)
        self.scale_min_y = self.create_spinbox(self.scale_grid, 0, 3)
        self.scale_min_z_text = self.create_label("   Min Z :", self.scale_grid, 0, 4)
        self.scale_min_z = self.create_spinbox(self.scale_grid, 0, 5)
        self.scale_max_x_text = self.create_label("   Max X :", self.scale_grid, 1, 0)
        self.scale_max_x = self.create_spinbox(self.scale_grid, 1, 1)
        self.scale_max_y_text = self.create_label("   Max Y :", self.scale_grid, 1, 2)
        self.scale_max_y = self.create_spinbox(self.scale_grid, 1, 3)
        self.scale_max_z_text = self.create_label("   Max Z :", self.scale_grid, 1, 4)
        self.scale_max_z = self.create_spinbox(self.scale_grid, 1, 5)

        self.scale_groupbox = self.create_groupbox("Scale Parameters", self.scale_grid)


        #On ajoute le bouton pour générer les animations
        #====================================================================================================
        generate_button = QPushButton("Generate Animation")
        generate_button.clicked.connect(lambda : animator.generate_random_animation(self.duration.value(), self.step.value(),
                                                                                    self.trans_min_x.value(), self.trans_max_x.value(),
                                                                                    self.trans_min_y.value(), self.trans_max_y.value(),
                                                                                    self.trans_min_z.value(), self.trans_max_z.value(),
                                                                                    self.rot_min_x.value(), self.rot_max_x.value(),
                                                                                    self.rot_min_y.value(), self.rot_max_y.value(),
                                                                                    self.rot_min_z.value(), self.rot_max_z.value(),
                                                                                    self.scale_min_x.value(), self.scale_max_x.value(),
                                                                                    self.scale_min_y.value(), self.scale_max_y.value(),
                                                                                    self.scale_min_z.value(), self.scale_max_z.value()))


        #On ajoute le bouton pour générer les animations
        #====================================================================================================
        delete_keys_button = QPushButton("Delete Animation Keys")
        delete_keys_button.clicked.connect(animator.delete_animation_keys)


        #On ajoute tous les layout horizontaux dans le vertical
        #====================================================================================================
        for groupbox in self.groupbox_list:
            self.layout.addWidget(groupbox)

        self.layout.addWidget(generate_button)
        self.layout.addWidget(delete_keys_button)