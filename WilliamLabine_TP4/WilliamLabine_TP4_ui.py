import os
import sys
from PySide6.QtWidgets import (QWidget,
                               QVBoxLayout,
                               QLabel,
                               QPushButton,
                               QSpinBox,
                               QDoubleSpinBox,
                               QSlider,
                               QGroupBox,
                               QGridLayout,
                               QTabWidget,
                               QCheckBox,
                               QComboBox,
                               QStackedWidget)
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
        self.setWindowTitle("Blender Modifiers In Maya")
        self.setMinimumWidth(400)
        self.created_shapes = []
        self.merged_result = []
        self.create_ui()

    def go_to_line_array_ui(self):
        self.array_stackedwidget.setCurrentIndex(0)
        self.circle_array_combobox.setCurrentIndex(1)

    def go_to_circle_array_ui(self):
        self.array_stackedwidget.setCurrentIndex(1)
        self.line_array_combobox.setCurrentIndex(0)

    def update_sliders(self, trans_slider, rot_slider, scale_slider, uniform_slider):
        trans_slider.setValue(uniform_slider.value())
        rot_slider.setValue(uniform_slider.value())
        scale_slider.setValue(uniform_slider.value())

    def create_label(self, text, gridlayout, row, column):
        this_label = QLabel(text)
        gridlayout.addWidget(this_label, row, column)
        return this_label

    def create_button(self, text, gridlayout, row, column):
        this_button = QPushButton(text)
        gridlayout.addWidget(this_button, row, column)
        return this_button

    def create_line_spinbox(self, min, max, gridlayout, row, column,):
        this_spinbox = QSpinBox()
        this_spinbox.setRange(min, max)
        gridlayout.addWidget(this_spinbox, row, column)
        this_spinbox.valueChanged.connect(lambda : array.make_array_in_a_line(self.line_x_count_spin.value(),
                                                                              self.line_y_count_spin.value(),
                                                                              self.line_z_count_spin.value(),
                                                                              self.line_x_offset_spin.value(),
                                                                              self.line_y_offset_spin.value(),
                                                                              self.line_z_offset_spin.value(),
                                                                              self.created_shapes))
        return this_spinbox

    def create_circle_spinbox(self, min, max, gridlayout, row, column,):
        this_spinbox = QSpinBox()
        this_spinbox.setRange(min, max)
        gridlayout.addWidget(this_spinbox, row, column)
        this_spinbox.valueChanged.connect(lambda : array.make_array_in_circle(self.circle_r_count_spin.value(),
                                                                              self.circle_y_count_spin.value(),
                                                                              self.circle_center_distance_spin.value(),
                                                                              self.circle_r_offset_spin.value(),
                                                                              self.circle_y_offset_spin.value(),
                                                                              self.created_shapes))
        return this_spinbox

    def create_line_doublespinbox(self, min, max, gridlayout, row, column):
        this_doublespinbox = QDoubleSpinBox()
        this_doublespinbox.setRange(min, max)
        gridlayout.addWidget(this_doublespinbox, row, column)
        this_doublespinbox.valueChanged.connect(lambda : array.make_array_in_a_line(self.line_x_count_spin.value(),
                                                                                    self.line_y_count_spin.value(),
                                                                                    self.line_z_count_spin.value(),
                                                                                    self.line_x_offset_spin.value(),
                                                                                    self.line_y_offset_spin.value(),
                                                                                    self.line_z_offset_spin.value(),
                                                                                    self.created_shapes))
        return this_doublespinbox

    def create_circle_doublespinbox(self, min, max, gridlayout, row, column):
        this_doublespinbox = QDoubleSpinBox()
        this_doublespinbox.setRange(min, max)
        gridlayout.addWidget(this_doublespinbox, row, column)
        this_doublespinbox.valueChanged.connect(lambda : array.make_array_in_circle(self.circle_r_count_spin.value(),
                                                                                    self.circle_y_count_spin.value(),
                                                                                    self.circle_center_distance_spin.value(),
                                                                                    self.circle_r_offset_spin.value(),
                                                                                    self.circle_y_offset_spin.value(),
                                                                                    self.created_shapes))
        return this_doublespinbox

    def create_line_slider(self, min, max, gridlayout, row, column):
        this_slider = QSlider()
        this_slider.setRange(min, max)
        this_slider.setOrientation(Qt.Horizontal)
        gridlayout.addWidget(this_slider, row, column)
        this_slider.valueChanged.connect(lambda : array.make_array_in_a_line(self.line_x_count_spin.value(),
                                                                             self.line_y_count_spin.value(),
                                                                             self.line_z_count_spin.value(),
                                                                             self.line_x_offset_spin.value(),
                                                                             self.line_y_offset_spin.value(),
                                                                             self.line_z_offset_spin.value(),
                                                                             self.created_shapes))
        return this_slider

    def create_circle_slider(self, min, max, gridlayout, row, column):
        this_slider = QSlider()
        this_slider.setRange(min, max)
        gridlayout.addWidget(this_slider, row, column)
        this_slider.setOrientation(Qt.Horizontal)
        this_slider.valueChanged.connect(lambda : array.make_array_in_circle(self.circle_r_count_spin.value(),
                                                                             self.circle_y_count_spin.value(),
                                                                             self.circle_center_distance_spin.value(),
                                                                             self.circle_r_offset_spin.value(),
                                                                             self.circle_y_offset_spin.value(),
                                                                             self.created_shapes))
        return this_slider

    def create_uniform_slider(self, min, max, gridlayout, row, column):
        this_slider = QSlider()
        this_slider.setRange(min, max)
        gridlayout.addWidget(this_slider, row, column)
        this_slider.setOrientation(Qt.Horizontal)
        return this_slider

    def create_checkbox(self, gridlayout, row, column):
        this_checkbox = QCheckBox()
        gridlayout.addWidget(this_checkbox, row, column)
        return this_checkbox

    def create_combobox(self, item01, item02, gridlayout, row, column):
        this_combobox = QComboBox()
        this_combobox.addItems([item01, item02])
        gridlayout.addWidget(this_combobox, row, column)
        return this_combobox

    def create_groupbox(self, title, gridlayout, groupbox_list):
        this_groupbox = QGroupBox(title)
        this_groupbox.setLayout(gridlayout)
        groupbox_list.append(this_groupbox)
        return this_groupbox

    def create_ui(self):

        #Création du layout de mon board
        self.layout = QVBoxLayout(self)

        #Ajout des tabs dans mon ui
        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)


        #Création et arrangement de la tab pour faire des arrays en ligne
        #====================================================================================================

        #On crée la tab pour les arrays
        self.tab_array = QWidget()
        self.layout_array = QVBoxLayout(self.tab_array)

        #Ajout de la tab array dans les tabs
        self.tabs.addTab(self.tab_array, "Array")

        #Ajout du stackedwidget pour les array en ligne ou en cercle
        self.array_stackedwidget = QStackedWidget()
        self.layout_array.addWidget(self.array_stackedwidget)

        #On crée la page d'array en ligne
        self.line_array = QWidget()
        self.line_array_layout = QVBoxLayout(self.line_array)

        #On crée la liste qui contiendra toutes les groupbox
        line_array_groupbox_list = []


        #Ajout du groupbox avec le dropdown menu
        #----------------------------------------------------------------------------------------------------

        #On crée le layout qui contiendra le groupbox du type d'array
        self.line_array_type_gridlayout = QGridLayout()

        #On crée le dropdown menu
        self.line_array_combobox = self.create_combobox("Array in a line", "Array in a circle", self.line_array_type_gridlayout, 0, 0)
        self.line_array_combobox.currentIndexChanged.connect(self.go_to_circle_array_ui)

        #On crée la box dans laquelle se trouve le dropdown menu
        self.line_array_type_groupbox = self.create_groupbox("Array Type", self.line_array_type_gridlayout, line_array_groupbox_list)


        #Ajout du groupbox avec le nombre d'itérations dans l'array
        #----------------------------------------------------------------------------------------------------
        
        #On crée le layout qui contiendra le groupbox des counts X, Y et Z
        self.line_count_gridlayout = QGridLayout()

        self.line_x_count_label = self.create_label("X Amount", self.line_count_gridlayout, 0, 0)
        self.line_x_count_spin = self.create_line_spinbox(1, 99, self.line_count_gridlayout, 0, 1)

        self.line_y_count_label = self.create_label("Y Amount", self.line_count_gridlayout, 1, 0)
        self.line_y_count_spin = self.create_line_spinbox(1, 99, self.line_count_gridlayout, 1, 1)

        self.line_z_count_label = self.create_label("Z Amount", self.line_count_gridlayout, 2, 0)
        self.line_z_count_spin = self.create_line_spinbox(1, 99, self.line_count_gridlayout, 2, 1)

        #On crée la box dans laquelle se trouve les counts
        self.line_count_groupbox = self.create_groupbox("Count", self.line_count_gridlayout, line_array_groupbox_list)


        #Ajout du groupbox avec les offset X, Y et Z
        #----------------------------------------------------------------------------------------------------

        #On crée le layout qui contiendra le groupbox des offsets X, Y et Z
        self.line_offsets_gridlayout = QGridLayout()

        self.line_x_offset_label = self.create_label("X Offset", self.line_offsets_gridlayout, 0, 0)
        self.line_x_offset_spin = self.create_line_doublespinbox(-9999, 9999, self.line_offsets_gridlayout, 0, 1)
        self.line_x_offset_spin.setValue(1.00)

        self.line_y_offset_label = self.create_label("Y Offset", self.line_offsets_gridlayout, 1, 0)
        self.line_y_offset_spin = self.create_line_doublespinbox(-9999, 9999, self.line_offsets_gridlayout, 1, 1)
        self.line_y_offset_spin.setValue(1.00)

        self.line_z_offset_label = self.create_label("Z Offset", self.line_offsets_gridlayout, 2, 0)
        self.line_z_offset_spin = self.create_line_doublespinbox(-9999, 9999, self.line_offsets_gridlayout, 2, 1)
        self.line_z_offset_spin.setValue(1.00)

        #On crée la box dans laquelle se trouve les offsets
        self.line_offsets_groupbox = self.create_groupbox("Offsets", self.line_offsets_gridlayout, line_array_groupbox_list)


        #Ajout du groupbox avec l'option merge
        #----------------------------------------------------------------------------------------------------
        
        #On crée le layout qui contiendra le groupbox du merge
        self.line_merge_gridlayout = QGridLayout()

        #On crée le checkbox et son label
        self.line_merge_label = self.create_label("Merge Geometry", self.line_merge_gridlayout, 0, 0)
        self.line_merge_checkbox = self.create_checkbox(self.line_merge_gridlayout, 0, 1)

        #On crée la box dans laquelle se trouve l'option merge
        self.line_merge_groupbox = self.create_groupbox("Merge", self.line_merge_gridlayout, line_array_groupbox_list)


        #Ajout du groupbox avec les options de randomness
        #----------------------------------------------------------------------------------------------------
        
        #On crée le layout qui contiendra le groupbox du randomness
        self.line_random_gridlayout = QGridLayout()

        #On crée le slider pour la randomness de translation
        self.line_trans_random_label = self.create_label("Random Translation", self.line_random_gridlayout, 0, 0)
        self.line_trans_random_slider = self.create_line_slider(0, 100, self.line_random_gridlayout, 0, 1)

        #On crée le slider pour la randomness de rotation
        self.line_rot_random_label = self.create_label("Random Rotation", self.line_random_gridlayout, 1, 0)
        self.line_rot_random_slider = self.create_line_slider(0, 100, self.line_random_gridlayout, 1, 1)

        #On crée le slider pour la randomness de translation
        self.line_scale_random_label = self.create_label("Random Scale", self.line_random_gridlayout, 2, 0)
        self.line_scale_random_slider = self.create_line_slider(0, 100, self.line_random_gridlayout, 2, 1)

        #On crée le slider pour la randomness de translation
        self.line_uniform_random_label = self.create_label("Uniform Random", self.line_random_gridlayout, 3, 0)
        self.line_uniform_random_slider = self.create_uniform_slider(0, 100, self.line_random_gridlayout, 3, 1)
        self.line_uniform_random_slider.valueChanged.connect(lambda : self.update_sliders(self.line_trans_random_slider,
                                                                                          self.line_rot_random_slider,
                                                                                          self.line_scale_random_slider,
                                                                                          self.line_uniform_random_slider))

        #On crée la box dans laquelle se trouve l'option merge
        self.line_random_groupbox = self.create_groupbox("Randomness", self.line_random_gridlayout, line_array_groupbox_list)


        #Ajout des boutons pour confirmer ou infirmer l'array
        #----------------------------------------------------------------------------------------------------

        #On crée le layout qui contiendra les deux boutons
        self.line_buttons_gridlayout = QGridLayout()

        #On crée le bouton de confirmation et d'infirmation
        self.line_cancel_button = self.create_button("Cancel", self.line_buttons_gridlayout, 0, 0)
        self.line_cancel_button.clicked.connect(lambda : array.cancel(self,
                                                                      self.created_shapes,
                                                                      self.merged_result))
        
        self.line_accept_button = self.create_button("Accept", self.line_buttons_gridlayout, 0, 1)
        self.line_accept_button.clicked.connect(lambda : array.confirm(self,
                                                                       self.line_merge_checkbox.isChecked(),
                                                                       self.created_shapes,
                                                                       self.merged_result))

        #On crée la box dans laquelle se trouve les boutons
        self.line_buttons_groupbox = self.create_groupbox("Confirmation", self.line_buttons_gridlayout, line_array_groupbox_list)


        #Ajout de tous les groupbox dans le layout d'array en ligne
        #----------------------------------------------------------------------------------------------------

        for groupbox in line_array_groupbox_list:
            # print(groupbox)
            self.line_array_layout.addWidget(groupbox)


        #Création et arrangement de la tab pour faire des arrays en cercle
        #====================================================================================================

        #On crée la page d'array en cercle
        self.circle_array = QWidget()
        self.circle_array_layout = QVBoxLayout(self.circle_array)

        #On crée la liste qui contiendra toutes les groupbox
        circle_array_groupbox_list = []


        #Ajout du groupbox avec le dropdown menu
        #----------------------------------------------------------------------------------------------------

        #On crée le layout qui contiendra le groupbox du type d'array
        self.circle_array_type_gridlayout = QGridLayout()

        #On crée le dropdown menu
        self.circle_array_combobox = self.create_combobox("Array in a line", "Array in a circle", self.circle_array_type_gridlayout, 0, 0)
        self.circle_array_combobox.setCurrentIndex(1)
        self.circle_array_combobox.currentIndexChanged.connect(self.go_to_line_array_ui)

        #On crée la box dans laquelle se trouve le dropdown menu
        self.circle_array_type_groupbox = self.create_groupbox("Array Type", self.circle_array_type_gridlayout, circle_array_groupbox_list)


        #Ajout du groupbox avec le nombre d'itérations dans l'array
        #----------------------------------------------------------------------------------------------------
        
        #On crée le layout qui contiendra le groupbox des counts X, Y et Z
        self.circle_count_gridlayout = QGridLayout()

        self.circle_r_count_label = self.create_label("Around Circle Amount", self.circle_count_gridlayout, 0, 0)
        self.circle_r_count_spin = self.create_circle_spinbox(1, 99,self.circle_count_gridlayout, 0, 1)

        self.circle_y_count_label = self.create_label("Y Amount", self.circle_count_gridlayout, 1, 0)
        self.circle_y_count_spin = self.create_circle_spinbox(1, 99, self.circle_count_gridlayout, 1, 1)

        #On crée la box dans laquelle se trouve les counts
        self.circle_count_groupbox = self.create_groupbox("Count", self.circle_count_gridlayout, circle_array_groupbox_list)


        #Ajout du groupbox avec les offsets de twist
        #----------------------------------------------------------------------------------------------------

        #On crée le layout qui contiendra le groupbox des offsets X, Y et Z
        self.circle_offset_gridlayout = QGridLayout()

        self.circle_center_distance_label = self.create_label("Distance to Center", self.circle_offset_gridlayout, 0, 0)
        self.circle_center_distance_spin = self.create_circle_doublespinbox(-9999, 9999, self.circle_offset_gridlayout, 0, 1)
        self.circle_center_distance_spin.setValue(1)

        self.circle_r_offset_label = self.create_label("Radius Offset", self.circle_offset_gridlayout, 1, 0)
        self.circle_r_offset_spin = self.create_circle_doublespinbox(-9999, 9999, self.circle_offset_gridlayout, 1, 1)
        
        self.circle_y_offset_label = self.create_label("Y Offset", self.circle_offset_gridlayout, 2, 0)
        self.circle_y_offset_spin = self.create_circle_doublespinbox(-9999, 9999, self.circle_offset_gridlayout, 2, 1)
        self.circle_y_offset_spin.setValue(1)

        #On crée la box dans laquelle se trouve les offsets
        self.circle_offset_groupbox = self.create_groupbox("Offsets", self.circle_offset_gridlayout, circle_array_groupbox_list)


        #Ajout du groupbox avec l'option merge
        #----------------------------------------------------------------------------------------------------
        
        #On crée le layout qui contiendra le groupbox du merge
        self.circle_merge_gridlayout = QGridLayout()

        #On crée le checkbox et son label
        self.circle_merge_label = self.create_label("Merge Geometry", self.circle_merge_gridlayout, 0, 0)
        self.circle_merge_checkbox = self.create_checkbox(self.circle_merge_gridlayout, 0, 1)

        #On crée la box dans laquelle se trouve l'option merge
        self.circle_merge_groupbox = self.create_groupbox("Merge", self.circle_merge_gridlayout, circle_array_groupbox_list)


        #Ajout du groupbox circle avec les options de randomness
        #----------------------------------------------------------------------------------------------------
        
        #On crée le layout qui contiendra le groupbox du randomness
        self.circle_random_gridlayout = QGridLayout()

        #On crée le slider pour la randomness de translation
        self.circle_trans_random_label = self.create_label("Random Translation", self.circle_random_gridlayout, 0, 0)
        self.circle_trans_random_slider = self.create_circle_slider(0, 100, self.circle_random_gridlayout, 0, 1)

        #On crée le slider pour la randomness de rotation
        self.circle_rot_random_label = self.create_label("Random Rotation", self.circle_random_gridlayout, 1, 0)
        self.circle_rot_random_slider = self.create_circle_slider(0, 100, self.circle_random_gridlayout, 1, 1)

        #On crée le slider pour la randomness de translation
        self.circle_scale_random_label = self.create_label("Random Scale", self.circle_random_gridlayout, 2, 0)
        self.circle_scale_random_slider = self.create_circle_slider(0, 100, self.circle_random_gridlayout, 2, 1)

        #On crée le slider pour la randomness de translation
        self.circle_uniform_random_label = self.create_label("Uniform Random", self.circle_random_gridlayout, 3, 0)
        self.circle_uniform_random_slider = self.create_uniform_slider(0, 100, self.circle_random_gridlayout, 3, 1)
        self.circle_uniform_random_slider.valueChanged.connect(lambda : self.update_sliders(self.circle_trans_random_slider,
                                                                                          self.circle_rot_random_slider,
                                                                                          self.circle_scale_random_slider,
                                                                                          self.circle_uniform_random_slider))

        #On crée la box dans laquelle se trouve l'option merge
        self.circle_random_groupbox = self.create_groupbox("Randomness", self.circle_random_gridlayout, circle_array_groupbox_list)


        #Ajout des boutons de confirmation du circle array
        #----------------------------------------------------------------------------------------------------

        #On crée le layout qui contiendra les deux boutons
        self.circle_buttons_gridlayout = QGridLayout()

        #On crée le bouton de confirmation et d'infirmation
        self.circle_cancel_button = self.create_button("Cancel", self.circle_buttons_gridlayout, 0, 0)
        self.circle_cancel_button.clicked.connect(lambda : array.cancel(self,
                                                                        self.created_shapes,
                                                                        self.merged_result))
        
        self.circle_accept_button = self.create_button("Accept", self.circle_buttons_gridlayout, 0, 1)
        self.circle_accept_button.clicked.connect(lambda : array.confirm(self,
                                                                         self.circle_merge_checkbox.isChecked(),
                                                                         self.created_shapes,
                                                                         self.merged_result))

        #On crée la box dans laquelle se trouve les boutons
        self.cine_buttons_groupbox = self.create_groupbox("Confirmation", self.circle_buttons_gridlayout, circle_array_groupbox_list)


        #Ajout de tous les groupbox dans le layout d'array en cercle
        #----------------------------------------------------------------------------------------------------

        for groupbox in circle_array_groupbox_list:
            # print(groupbox)
            self.circle_array_layout.addWidget(groupbox)


        #On applique nos deux "pages", nos deux layout, sur le stackedwidget
        #====================================================================================================

        self.array_stackedwidget.addWidget(self.line_array)
        self.array_stackedwidget.addWidget(self.circle_array)


        #Création et arrangement de la tab pour importer Suzanne
        #====================================================================================================

        #On crée la tab pour Suzanne
        self.tab_suzanne = QWidget()
        self.layout_suzanne = QVBoxLayout(self.tab_suzanne)

        #Ajout de la tab array dans les tabs
        self.tabs.addTab(self.tab_suzanne, "Suzanne")
        
        
        #Ajout du bouton pour importer Suzanne
        #----------------------------------------------------------------------------------------------------

        #On crée le bouton de confirmation et d'infirmation
        self.suzanne_button = QPushButton("Import Suzanne")
        self.suzanne_button.clicked.connect(array.import_suzanne)


        #Ajout de tous les groupbox dans le layout de Suzanne
        #----------------------------------------------------------------------------------------------------

        self.layout_suzanne.addWidget(self.suzanne_button)