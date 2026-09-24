import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PySide6.QtGui import QGuiApplication
from pathlib import Path

import json

#Je ne sais pas ce que c'est exactement, mais il nous faut ça à la fin pour afficher le tableau
app = QApplication(sys.argv)

try:
    # Permet de loader le fichier JSON et le plug dans "data"
    # encoding="utf-8" permet d'afficher les accents sur les lettres
    with open('drinks.json', 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)
    print("We got the booze!")

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

#Créer mon header_labels pour y mettre les clés, puis l'utiliser pour setter les header labels du tableau
header_labels = []

#Get les keys et les mettre dans mon array header_labels
for object in data:
    for key in object:
        if(key not in header_labels):
            header_labels.append(key)

#Print les keys pour tester si tout va bien
for i in range(len(header_labels)):
    print(header_labels[i])

#Création de mon tableau avec autant de rangées que d'objets dans mon JSON, et autant de colonnes que de "keys"
mon_tableau = QTableWidget(len(data), len(header_labels))

#Setter les horizontal header labels avec mon array créé précédemment
mon_tableau.setHorizontalHeaderLabels(header_labels)
mon_tableau.setWindowTitle("Drinks du vieux neuf Saloon")

#Setter tous les items du tableau dans celui-ci pour qu'ils soient affichés
for row_index in range(len(data)):
    for column_index in range(len(header_labels)):
        mon_tableau.setItem(row_index, column_index, QTableWidgetItem(str(data[row_index][header_labels[column_index]])))

#Resize de mon tableau pour voir quelque chose
mon_tableau.resize(320, 120)

#Ajouter le tri en ordre croissant parce que pourquoi pas! :)
mon_tableau.setSortingEnabled(True)

#Afficher mon magnifique tableau
mon_tableau.show()

#Fonction à la fin pour éviter que tout explose!
sys.exit(app.exec())
