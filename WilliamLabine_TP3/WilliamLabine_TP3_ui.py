import os
import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSpinBox, QGroupBox, QGridLayout

#On trouve le path du dossier dans lequel se trouve ce même fichier
absolute_folder_path = os.path.dirname(os.path.abspath(__file__))

#On ajoute le path aux paths auxquels sys a accès
sys.path.append(absolute_folder_path)

#On importe le fichier du ui
import WilliamLabine_TP3_animator

#On reload le fichier ui pour que Maya ne perde pas la tête
import importlib
importlib.reload(WilliamLabine_TP3_animator)

class RandomAnimationUI(QWidget):
    def __init__(self):
        #Initialisation de mon message board avec le contructeur de base
        super().__init__()
        self.setWindowTitle("Random Animation Generator")
        self.setMinimumWidth(400)
        self.create_ui()

    def create_ui(self):

        #On génère une animation random selon les données entrées
        def generate_random_animation():
            WilliamLabine_TP3_animator.generate_random_animation()
        
        #Crée un QSpinBox et le place dans un QHBoxLayout
        def create_spinbox(gridlayout, row, column):
            self = QSpinBox()
            self.setMaximum(999999)
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

        #Création de la zone Animation Timing
        #====================================================================================================
        timing_grid = QGridLayout()
        duration_text = create_label("    Duration (Frames):", timing_grid, 0, 0)
        duration = create_spinbox(timing_grid, 0, 1)
        step_text = create_label("    Step (Frames):", timing_grid, 0, 2)
        step = create_spinbox(timing_grid, 0, 3)

        animation_groupbox = create_groupbox("Animation Timing", timing_grid)

        #Création de la zone Translation Parameters
        #====================================================================================================
        translation_grid = QGridLayout()
        trans_min_x_text = create_label("   Min X :", translation_grid, 0, 0)
        trans_min_x = create_spinbox(translation_grid, 0, 1)
        trans_min_y_text = create_label("   Min Y :", translation_grid, 0, 2)
        trans_min_y = create_spinbox(translation_grid, 0, 3)
        trans_min_z_text = create_label("   Min Z :", translation_grid, 0, 4)
        trans_min_z = create_spinbox(translation_grid, 0, 5)
        trans_max_x_text = create_label("   Max X :", translation_grid, 1, 0)
        trans_max_x = create_spinbox(translation_grid, 1, 1)
        trans_max_y_text = create_label("   Max Y :", translation_grid, 1, 2)
        trans_max_y = create_spinbox(translation_grid, 1, 3)
        trans_max_z_text = create_label("   Max Z :", translation_grid, 1, 4)
        trans_max_z = create_spinbox(translation_grid, 1, 5)

        translation_groupbox = create_groupbox("Translation Parameters", translation_grid)

        
        #Création de la zone Rotation Parameters
        #====================================================================================================
        rotation_grid = QGridLayout()
        rot_min_x_text = create_label("   Min X :", rotation_grid, 0, 0)
        rot_min_x = create_spinbox(rotation_grid, 0, 1)
        rot_min_y_text = create_label("   Min Y :", rotation_grid, 0, 2)
        rot_min_y = create_spinbox(rotation_grid, 0, 3)
        rot_min_z_text = create_label("   Min Z :", rotation_grid, 0, 4)
        rot_min_z = create_spinbox(rotation_grid, 0, 5)
        rot_max_x_text = create_label("   Max X :", rotation_grid, 1, 0)
        rot_max_x = create_spinbox(rotation_grid, 1, 1)
        rot_max_y_text = create_label("   Max Y :", rotation_grid, 1, 2)
        rot_max_y = create_spinbox(rotation_grid, 1, 3)
        rot_max_z_text = create_label("   Max Z :", rotation_grid, 1, 4)
        rot_max_z = create_spinbox(rotation_grid, 1, 5)

        rotation_groupbox = create_groupbox("Rotation Parameters", rotation_grid)


        #Création de la zone Scale Parameters
        #====================================================================================================
        scale_grid = QGridLayout()
        scale_min_x_text = create_label("   Min X :", scale_grid, 0, 0)
        scale_min_x = create_spinbox(scale_grid, 0, 1)
        scale_min_y_text = create_label("   Min Y :", scale_grid, 0, 2)
        scale_min_y = create_spinbox(scale_grid, 0, 3)
        scale_min_z_text = create_label("   Min Z :", scale_grid, 0, 4)
        scale_min_z = create_spinbox(scale_grid, 0, 5)
        scale_max_x_text = create_label("   Max X :", scale_grid, 1, 0)
        scale_max_x = create_spinbox(scale_grid, 1, 1)
        scale_max_y_text = create_label("   Max Y :", scale_grid, 1, 2)
        scale_max_y = create_spinbox(scale_grid, 1, 3)
        scale_max_z_text = create_label("   Max Z :", scale_grid, 1, 4)
        scale_max_z = create_spinbox(scale_grid, 1, 5)

        scale_groupbox = create_groupbox("Scale Parameters", scale_grid)


        #On ajoute le bouton pour générer les animations
        #====================================================================================================
        generate_button = QPushButton("Generate")
        generate_button.clicked.connect(generate_random_animation)


        #On ajoute tous les layout horizontaux dans le vertical
        #====================================================================================================
        for groupbox in groupbox_list:
            layout.addWidget(groupbox)

        layout.addWidget(generate_button)