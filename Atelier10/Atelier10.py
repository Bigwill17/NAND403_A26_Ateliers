import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QSpinBox,
    QDoubleSpinBox,
    QMessageBox
)
import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance
from PySide6.QtCore import Qt

#Fonction pour mettre la fenêtre always on top
def maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(pointer), QWidget)


class Scatter(QWidget):

    #Constructeur de base de notre widget scatter
    def __init__(self):
        super().__init__(maya_main_window())
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("Scatter")
        self.setMinimumWidth(250)
        self.build_ui()

    #On ajoute tous les composants du ui
    def build_ui(self):

        #Ajout du form
        layout = QVBoxLayout(self)
        form = QFormLayout()
        layout.addLayout(form)

        #Ajout du spinbox du nombre d'éléments dupliqués
        self.count_spin = QSpinBox()
        self.count_spin.setRange(1, 100)
        self.count_spin.setValue(10)
        form.addRow("Copies", self.count_spin)

        #Ajout du spinbox de rayon
        self.radius_spin = QDoubleSpinBox()
        self.radius_spin.setRange(1.0, 50.0)
        self.radius_spin.setValue(10.0)
        form.addRow("Radius", self.radius_spin)

        #Ajout du spinbox de la seed
        self.seed_spin = QSpinBox()
        self.seed_spin.setRange(0, 9999)
        form.addRow("Seed", self.seed_spin)

        #On connecte le changement d'une quelconque valeur à la fonction scatter pour permettre le live edit
        self.count_spin.valueChanged.connect(self.scatter)
        self.radius_spin.valueChanged.connect(self.scatter)
        self.seed_spin.valueChanged.connect(self.scatter)

    #Fonction principale pour dupliquer et disperser les objets
    def scatter(self):

        #On set l'objet source (le premier objet sélectionné, normalement le seul)
        selection = cmds.ls(selection = True, transforms = True)
        source = selection[0]

        #On set tous les autres objets (ils seront supprimés au début de la fonction scatter)
        everything_else = cmds.ls(dag = True, transforms = True)

        #On retire les 4 caméras de base qu'on ne peut même pas supprimer
        everything_else.remove("top")
        everything_else.remove("persp")
        everything_else.remove("side")
        everything_else.remove("front")

        #On delete tous les autres objets
        for selected_object in everything_else:
            if selected_object != source:
                cmds.delete(selected_object)

        #On affiche un message d'erreur si rien n'est sélectionné
        if not selection:
            QMessageBox.warning(self, "Scatter", "Select an object first.")
            return

        #On set la seed et le rayon selon les valeurs des spinbox
        random.seed(self.seed_spin.value())
        radius = self.radius_spin.value()

        #On duplique notre objet sélecitonné et on les déplace dans notre rayon
        for i in range(self.count_spin.value()):
            copy = cmds.duplicate(source)[0]
            x = random.uniform(-radius, radius)
            z = random.uniform(-radius, radius)
            cmds.move(x, 0, z, copy, relative=True)

        #On remet la sélection sur notre objet source, pour pouvoir modifier les valeurs des spinbox sans avoir à sélectionner l'objet de nouveau
        cmds.select(source)

#On affiche notre outil de scatter
def show_tool():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = Scatter()
    tool_window.show()


show_tool()
