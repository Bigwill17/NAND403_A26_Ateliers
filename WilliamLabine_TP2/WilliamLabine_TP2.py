import sys
import json
from PySide6.QtWidgets import QMessageBox, QApplication, QTextEdit, QLabel, QWidget, QVBoxLayout, QPushButton, QCheckBox
import maya.cmds as cmds
from contextlib import contextmanager

#Tester le fichier JSON en le loadant, ou échouer lamentablement et afficher un message d'erreur digne
def test_json(file_path):

    #try et except permet de vérifier si le code est fonctionnel avant de runner le programme
    try:

        # Permet de loader le fichier JSON et le plug dans "data"
        # encoding="utf-8" permet d'afficher les accents sur les lettres
        with open(file_path, 'r', encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data

    #S'il y a un problème, le programme ne crash pas, il note l'erreur et affiche ce qui se passe
    except json.JSONDecodeError as e:
        print(f"Erreur JSON détectée : {e.msg}")
        print(f"Ligne : {e.lineno}, Col : {e.colno}")

        #Création d'un message d'erreur qui pop-up pour dire précisément l'erreur qui a lieu
        mon_message_derreur = QMessageBox()
        mon_message_derreur.setWindowTitle("Erreur JSON")
        mon_message_derreur.setInformativeText("Erreur JSON détectée")
        mon_message_derreur.setButtonText(1, "Fermer")
        mon_message_derreur.setDetailedText(f"{e.msg}\nLigne : {e.lineno}, Col : {e.colno}")
        mon_message_derreur.resize(300, 200)
        
        mon_message_derreur.show()
        sys.exit(app.exec())

    #Si le fichier JSON n'est pas au bon endroit, il est introuvable, et on détecte le problème ici
    except FileNotFoundError:
        print("Le fichier est introuvable.")

        #Création d'un message d'erreur qui pop-up pour dire que le fichier JSON est introuvable
        mon_message_derreur = QMessageBox()
        mon_message_derreur.setWindowTitle("Erreur JSON")
        mon_message_derreur.setInformativeText("Le fichier JSON est introuvable.")
        mon_message_derreur.setButtonText(1, "Fermer")
        mon_message_derreur.setDetailedText("Où est JSON? OÙ EST-IL!?")

        mon_message_derreur.resize(300, 200)
        
        mon_message_derreur.show()
        sys.exit(app.exec())

@contextmanager
def custom_undo_chunk():
    cmds.undoInfo(openChunk=True)
    try:
        yield
    finally:
        cmds.undoInfo(closeChunk=True)

class MessageBoard(QWidget):
    def __init__(self):
        #Initialisation du board avec toutes les options d'organisation
        super().__init__()
        self.setWindowTitle("Outliner Organizer")
        self.create_ui()

    def create_ui(self):
        
        #Fonction appelée lorsqu'on appuie sur le bouton du board pour organiser
        def on_click(self):
            #On met le chemin du JSON dans sa variable file_path
            file_path = text.toPlainText()

            #On teste le chargement du fichier JSON et on met celui-ci dans data
            data = test_json(file_path)

            with custom_undo_chunk():
                if selection_only_checkbox.isChecked():
                    objects = cmds.ls(selection = True)
                else:
                    objects = cmds.ls(transforms=True)

                if colors_checkbox.isChecked():
                    for keys in data:
                        for obj in objects:
                            if keys in obj:
                                cmds.setAttr(f"{obj}.useOutlinerColor", True)
                                cmds.setAttr(f"{obj}.outlinerColor", data[keys][0], data[keys][1], data[keys][2], type="double3")

                if reorder_checkbox.isChecked():
                    objects_sorted = sorted(objects, reverse=True)

                    for obj in objects_sorted:
                        cmds.reorder(obj, front=True)
        
        #Création du layout de mon board
        layout = QVBoxLayout(self)

        #Création du texte de base qui demande le chemin JSON
        label = QLabel("Please enter the JSON rule path")
        layout.addWidget(label)

        #Ajout de la zone d'entrée de chemin vers JSON
        text = QTextEdit()
        text.setFixedHeight(30)
        text.setPlaceholderText("JSON path...")
        layout.addWidget(text)

        #Ajout de la check box pour seulement la sélection active
        selection_only_checkbox = QCheckBox("Apply on selection only")
        layout.addWidget(selection_only_checkbox)

        #Ajout de la check box pour ajouter les couleurs
        colors_checkbox = QCheckBox("Apply colors")
        layout.addWidget(colors_checkbox)

        #Ajout de la check box pour réorganiser les items
        reorder_checkbox = QCheckBox("Apply reorder")
        layout.addWidget(reorder_checkbox)
        
        #Création du bouton de mon board pour organiser l'outliner
        button = QPushButton()
        button.setText("Organise Outliner")
        button.clicked.connect(on_click)
        layout.addWidget(button)

file_path = 0

def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()

main()