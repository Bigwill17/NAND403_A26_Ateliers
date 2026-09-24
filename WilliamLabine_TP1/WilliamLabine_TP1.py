import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QListWidget, QLineEdit
from PySide6.QtGui import QGuiApplication, Qt
import json

#Je ne sais pas ce que c'est exactement, mais il nous faut ça à la fin pour afficher le tableau
app = QApplication(sys.argv)

def test_json(the_json):
    #try et except permet de vérifier si le code est fonctionnel avant de runner le programme
    try:

        # Permet de loader le fichier JSON et le plug dans "data"
        # encoding="utf-8" permet d'afficher les accents sur les lettres
        with open(the_json, 'r', encoding="utf-8") as json_file:
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

def get_json_keys():
    #Je crée un array qui contiendra toutes les "keys" de mon JSON
    keys = []

    #Pour toutes les infos de mon JSON, je le mets dans mon array
    for object in data:
        for key in object:

            #S'il n'existe pas déjà, je le rajoute
            if(key not in keys):
                keys.append(key)

            #Sinon, il existe déjà, donc j'ai fait le tour des "keys" nécessaires
            else:
                break
    return keys

def set_window_and_stuff(window, tableau):

    window.setWindowTitle("Visualisation de données")
    #Setup de la taille de la fenêtre en tenant compte de la taille de l'écran, pour le mettre full screen
    screen_size = QGuiApplication.primaryScreen().size()
    window.resize(screen_size.width(), screen_size.height())

    #Création d'un central widget pour gérer certains sous-widgets
    mon_central_widget = QWidget()
    #Setter mon central widget comme le central widget de ma fenêtre
    window.setCentralWidget(mon_central_widget)

    #Création de la vertical box pour aligner des sous-widgets de manière verticale
    layout = QVBoxLayout(mon_central_widget)

    #Créer la barre de recherche avec le text "Rechercher", puis l'ajouter dans ma vertical box
    search_bar = QLineEdit()
    search_bar.setPlaceholderText("Rechercher")
    layout.addWidget(search_bar)

    #Ajout du tableau dans la vertical box
    layout.addWidget(tableau)

    #Je set les header labels avec les "keys" trouvées précédemment
    mon_tableau.setHorizontalHeaderLabels(keys)

def fill_tableau(tableau):
    
    #Je remplis mon tableau grâce a 2 for loop, une pour les rangées, l'autre pour les colonnes
    for row_index in range(len(data)):
        for column_index in range(len(keys)):
            #Je set l'item dans la bonne rangée (row_index) et dans la bonne colonne (column_index) 
            #Ce que je mets dans QTableWidgetItem() est énorme et incompréhensible, mais il équivaut à ça : (data[i]['key'])
            tableau.setItem(row_index, column_index, QTableWidgetItem(str(data[row_index][keys[column_index]])))

    #Cette magnifique ligne de code permet de trier le tableau par colonne, tout simplement
    tableau.setSortingEnabled(True)
    #Le setSortingEnabled(True) de base organise ma première colonne en ordre décroissant, alors je la remets en ordre croissant tout de suite après
    tableau.sortByColumn(0, Qt.SortOrder.AscendingOrder)

#On commence en testant le chargement du fichier json et on met celui-ci dans "data"
data = test_json('data_small.json')

#=====================================================================================================================================
#                     ^^^^^
#        ENTREZ LE NOM DU FICHIER JSON ICI
#=====================================================================================================================================

#On va chercher les clés du fichier json. On les utilisera pour setter les horizontal header labels et pour naviguer dans "data"
keys = get_json_keys()

#Création de mon tableau avec autant de rangées que d'objets dans mon JSON, et autant de colonnes que de "keys"
mon_tableau = QTableWidget(len(data), len(keys))

#Création de ma fenêtre principale dans laquelle il y aura tous mes autres widgets
ma_window = QMainWindow()

set_window_and_stuff(ma_window, mon_tableau)

fill_tableau(mon_tableau)

#Afficher ma fenêtre avec tout
ma_window.show()

#Executer le tableau?
sys.exit(app.exec())