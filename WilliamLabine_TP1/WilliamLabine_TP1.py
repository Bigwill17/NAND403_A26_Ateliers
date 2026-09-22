import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PySide6.QtGui import QGuiApplication

import json
from pathlib import Path

#Je ne sais pas ce que c'est exactement, mais il nous faut ça à la fin pour afficher le tableau
app = QApplication(sys.argv)

#Ma variable pour switch de un à l'autre pour mon ordre croissant et décroissant avec mon bouton
flip_flop = True

#try et except permet de vérifier si le code est fonctionnel avant de runner le programme
try:

    # Permet de loader le fichier JSON et le plug dans "data"
    # encoding="utf-8" permet d'afficher les accents sur les lettres
    with open('data_small.json', 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)
    print("Le fichier JSON est valide.")

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

#Je crée un array qui contiendra toutes les "keys" de mon JSON
horizontal_header_labels = []

#Pour toutes les infos de mon JSON, je le mets dans mon array
for object in data:
    for key in object:

        #S'il n'existe pas déjà, je le rajoute
        if(key not in horizontal_header_labels):
            horizontal_header_labels.append(key)

        #Sinon, il existe déjà, donc j'ai fait le tour des "keys" nécessaires
        else:
            break

#Création de ma fenêtre principale dans laquelle il y aura tous mes autres widgets
ma_window = QMainWindow()
ma_window.setWindowTitle("Visualisation de données")

#Setup de la taille de la fenêtre en tenant compte de la taille de l'écran, pour le mettre full screen
screen_size = QGuiApplication.primaryScreen().size()
ma_window.resize(screen_size.width(), screen_size.height())

#Création d'un central widget pour gérer certains sous-widgets
mon_central_widget = QWidget()
#Setter mon central widget comme le central widget de ma fenêtre
ma_window.setCentralWidget(mon_central_widget)

#Création de la vertical box pour aligner des sous-widgets de manière verticale
layout = QVBoxLayout(mon_central_widget)

#Création de mon tableau avec autant de rangées que d'objets dans mon JSON, et autant de colonnes que de "keys"
mon_tableau = QTableWidget(len(data), len(horizontal_header_labels))


#Ajout du tableau dans la vertical box
layout.addWidget(mon_tableau)

#Je set les header labels avec les "keys" trouvées précédemment
mon_tableau.setHorizontalHeaderLabels(horizontal_header_labels)

#Je remplis mon tableau grâce a 2 for loop, une pour les rangées, l'autre pour les colonnes
for row_index in range(len(data)):
    for column_index in range(len(horizontal_header_labels)):
        #Je set l'item dans la bonne rangée (row_index) et dans la bonne colonne (column_index) 
        #Ce que je mets dans QTableWidgetItem() est énorme et incompréhensible, mais il équivaut à ça : (data[i]['key'])
        mon_tableau.setItem(row_index, column_index, QTableWidgetItem(str(data[row_index][horizontal_header_labels[column_index]])))

#Cette magnifique ligne de code permet de trier le tableau par colonne, tout simplement
mon_tableau.setSortingEnabled(True)

#Set la window en full screen automatiquement, mais le x pour fermer le fenêtre n'est plus visible
# ma_window.showFullScreen()

#Afficher ma fenêtre avec tout
ma_window.show()

#Executer le tableau?
sys.exit(app.exec())