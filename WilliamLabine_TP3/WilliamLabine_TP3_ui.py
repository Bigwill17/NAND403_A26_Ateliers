from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSpinBox, QGroupBox

class RandomAnimationUI(QWidget):
    def __init__(self):
        #Initialisation de mon message board avec le contructeur de base
        super().__init__()
        self.setWindowTitle("Random Animation Generator")
        self.setMinimumWidth(400)
        self.create_ui()

    def create_ui(self):

        def generate_random_animation():
            print("yes")

        #Crée un QHBoxLayout et le met dans la liste de tous les hbox
        def create_hbox():
            self = QHBoxLayout()
            return self
        
        #Crée un QSpinBox et le place dans un QHBoxLayout
        def create_spinbox(hbox):
            self = QSpinBox()
            self.setMaximum(999999)
            hbox.addWidget(self)
            return self

        #Crée un QLabel qui servira de titre et le place dans un QHBoxLayout
        def create_label(text, hbox):
            self = QLabel(text)
            hbox.addWidget(self)
            return self

        #Crée un QGroupBox dans lequel on met le layout hbox, et on l'ajoute à la liste des groupbox
        def create_groupbox(title, hbox):
            self = QGroupBox(title)
            self.setLayout(hbox)
            groupbox_list.append(self)
            return self

        #Création du layout de mon board
        layout = QVBoxLayout(self)

        #Création du tableau de QGroupBox qui seront utilisés plus tard
        groupbox_list = []

        #Création de la zone Animation Timing
        #====================================================================================================

        timing_hbox = create_hbox()
        duration_text = create_label("    Duration (Frames):", timing_hbox)
        duration = create_spinbox(timing_hbox)
        step_text = create_label("    Step (Frames):", timing_hbox)
        step = create_spinbox(timing_hbox)

        animation = create_groupbox("Animation Timing", timing_hbox)

        #Création de la zone Translation Parameters
        #====================================================================================================

        trans_title_hbox = create_hbox()
        trans_title = create_label("Translation Parameters", trans_title_hbox)

        trans_min_hbox = create_hbox()
        trans_min_x_text = create_label("   Min X :", trans_min_hbox)
        trans_min_x = create_spinbox(trans_min_hbox)
        trans_min_y_text = create_label("   Min Y :", trans_min_hbox)
        trans_min_y = create_spinbox(trans_min_hbox)
        trans_min_z_text = create_label("   Min Z :", trans_min_hbox)
        trans_min_z = create_spinbox(trans_min_hbox)

        trans_max_hbox = create_hbox()
        trans_max_x_text = create_label("   Max X :", trans_max_hbox)
        trans_max_x = create_spinbox(trans_max_hbox)
        trans_max_y_text = create_label("   Max Y :", trans_max_hbox)
        trans_max_y = create_spinbox(trans_max_hbox)
        trans_max_z_text = create_label("   Max Z :", trans_max_hbox)
        trans_max_z = create_spinbox(trans_max_hbox)

        
        #Création de la zone Rotation Parameters
        #====================================================================================================
        rot_title_hbox = create_hbox()
        rot_title = create_label("Rotation Parameters", rot_title_hbox)

        rot_min_hbox = create_hbox()
        rot_min_x_text = create_label("   Min X :", rot_min_hbox)
        rot_min_x = create_spinbox(rot_min_hbox)
        rot_min_y_text = create_label("   Min Y :", rot_min_hbox)
        rot_min_y = create_spinbox(rot_min_hbox)
        rot_min_z_text = create_label("   Min Z :", rot_min_hbox)
        rot_min_z = create_spinbox(rot_min_hbox)

        rot_max_hbox = create_hbox()
        rot_max_x_text = create_label("   Max X :", rot_max_hbox)
        rot_max_x = create_spinbox(rot_max_hbox)
        rot_max_y_text = create_label("   Max Y :", rot_max_hbox)
        rot_max_y = create_spinbox(rot_max_hbox)
        rot_max_z_text = create_label("   Max Z :", rot_max_hbox)
        rot_max_z = create_spinbox(rot_max_hbox)


        #Création de la zone Scale Parameters
        #====================================================================================================
        scale_title_hbox = create_hbox()
        scale_title = create_label("Scale Parameters", scale_title_hbox)

        scale_min_hbox = create_hbox()
        scale_min_x_text = create_label("   Min X :", scale_min_hbox)
        scale_min_x = create_spinbox(scale_min_hbox)
        scale_min_y_text = create_label("   Min Y :", scale_min_hbox)
        scale_min_y = create_spinbox(scale_min_hbox)
        scale_min_z_text = create_label("   Min Z :", scale_min_hbox)
        scale_min_z = create_spinbox(scale_min_hbox)

        scale_max_hbox = create_hbox()
        scale_max_x_text = create_label("   Max X :", scale_max_hbox)
        scale_max_x = create_spinbox(scale_max_hbox)
        scale_max_y_text = create_label("   Max Y :", scale_max_hbox)
        scale_max_y = create_spinbox(scale_max_hbox)
        scale_max_z_text = create_label("   Max Z :", scale_max_hbox)
        scale_max_z = create_spinbox(scale_max_hbox)


        #On ajoute le bouton pour générer les animations
        #====================================================================================================
        generate_button = QPushButton("Generate")
        generate_button.clicked.connect(generate_random_animation)


        #On ajoute tous les layout horizontaux dans le vertical
        #====================================================================================================
        # for groupbox in groupbox_list:
        #     layout.addLayout(groupbox)
        
        layout.addWidget(animation)
        layout.addWidget(generate_button)