from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
import maya.cmds as cmds

class MessageBoard(QWidget):
    def __init__(self):
        #Initialisation de mon board avec le contructeur de base
        super().__init__()
        self.setWindowTitle("Center Pivot To Selection")
        self.setMinimumWidth(400)
        self.create_ui()

    def create_ui(self):

        #Création du layout de mon board
        layout = QHBoxLayout(self)

        #Ajout de mes variables qui enregistrent les coordonnées moyennes
        self.x_moyen = 0
        self.y_moyen = 0
        self.z_moyen = 0

        #Création du bouton Apply de mon message board
        apply_button = QPushButton()
        apply_button.setText("Apply Selection")
        apply_button.clicked.connect(self.Apply)
        layout.addWidget(apply_button)

        #Création du bouton Center de mon message board
        center_button = QPushButton()
        center_button.setText("Center Pivot")
        center_button.clicked.connect(self.Center)
        layout.addWidget(center_button)

    #Fonction pour identifier le type d'objet dans ma sélection
    def identify_selection(self):

        if cmds.filterExpand(selectionMask = 31):
            return "Vertex"
            
        elif cmds.filterExpand(selectionMask = 32):
            return "Edge"

        elif cmds.filterExpand(selectionMask = 34): 
            return "Face"

        else:
            return "Object"

    #Fonction qui enregistre les coordonnées moyennes des éléments sélectionnés
    def Apply(self):

        #On set les valeurs moyennes à 0
        self.x_moyen = 0
        self.y_moyen = 0
        self.z_moyen = 0

        #On rentre les objets sélectionnés dans la variable selection
        selection = cmds.ls(selection=True, flatten=True)

        #On enregistre le type d'objets sélecitonnés dans la variable type_selection
        type_selection = self.identify_selection()

        #Pour les vertex et les objets, on fait la même commande
        if type_selection == "Vertex" or type_selection == "Object":
            objects = cmds.ls(selection = True, flatten = True)

        #Pour les edges et les faces, on convertit d'abord ces edges ou faces en vertex, puis on fait la même commande
        elif type_selection == "Edge" or type_selection == "Face":
            vertices = cmds.polyListComponentConversion(selection, toVertex=True)
            objects = cmds.ls(vertices, flatten=True)

        #Pour tous les objets sélectionnés, on incrémente x, y et z
        for comp in objects:
            coordo = cmds.xform(comp, query = True, translation = True, worldSpace = True)

            self.x_moyen += coordo[0]
            self.y_moyen += coordo[1]
            self.z_moyen += coordo[2]

        #Puis on divise x, y et z par le nombre d'éléments pour faire la moyenne
        self.x_moyen /= len(objects)
        self.y_moyen /= len(objects)
        self.z_moyen /= len(objects)

        #On print les coordonnées moyennes, juste pour avoir un peu de feedback ;)
        print(self.x_moyen)
        print(self.y_moyen)
        print(self.z_moyen)

    def Center(self):
        #L'objet sélectionné va dans la variable object
        object = cmds.ls(selection = True)

        #On initialise la viriable new_position aux valeurs x, y et z moyennes
        new_position = [self.x_moyen, self.y_moyen, self.z_moyen]

        #On déplace le pivot de rotation et d'échelle de l'objet sélectionné en même temps, aux mêmes coordos
        cmds.xform(object, rotatePivot = new_position, worldSpace = True)
        cmds.xform(object, scalePivot = new_position, worldSpace = True)
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()

main()