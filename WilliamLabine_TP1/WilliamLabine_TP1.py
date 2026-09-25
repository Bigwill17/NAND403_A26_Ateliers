import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QLabel, QVBoxLayout, QWidget, QMessageBox, QLineEdit
from PySide6.QtGui import QGuiApplication, Qt
from PySide6.QtCore import QFileInfo
import json


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

#Aller chercher les informations du fichier JSON utilisé (nom, taille et nombre d'objets)
def get_file_info(file_path):

    #Création de la variable file_infos qui pourra utiliser les fonctions de QFileInfo
    file_infos = QFileInfo(file_path)

    #On va chercher le nom et la taille avec file_infos, le nombre d'objets est obtenu grâce au fichier JSON lui-même (data)
    file_name = file_infos.fileName()
    file_size = file_infos.size()
    num_objects = len(data)

    return file_name, file_size, num_objects

#Aller chercher toutes les différentes keys et les conserver dans un array
def get_json_keys():
    #Je crée un array qui contiendra toutes les "keys" de mon JSON
    keys = []

    #Pour toutes les infos de mon JSON, je le mets dans mon array
    for object in data:
        for key in object:

            #Si la clé n'existe pas déjà dans mon array, je le rajoute
            if(key not in keys):
                keys.append(key)

            #Sinon, il existe déjà, donc j'ai fait le tour des "keys" nécessaires
            else:
                break
    return keys

#Faire le setup complet de ma window principale, puis du central widget, vertical box, tableau, etc
def set_window_and_stuff(window, tableau):

    window.setWindowTitle("William Labine TP1 - Visualisation de données")
    #Setup de la taille de la fenêtre en tenant compte de la taille de l'écran, pour le mettre full screen
    screen_size = QGuiApplication.primaryScreen().size()
    window.resize(screen_size.width(), screen_size.height())

    #Création d'un central widget pour gérer certains sous-widgets
    mon_central_widget = QWidget()
    #Setter mon central widget comme le central widget de ma fenêtre
    window.setCentralWidget(mon_central_widget)

    #Création de la vertical box pour aligner des sous-widgets de manière verticale
    layout = QVBoxLayout(mon_central_widget)

    #Ajouter les infos du fichier JSON (nom, taille et nombre d'éléments) dans un label pour l'afficher
    info_text = QLabel(f"Nom du fichier : {file_name}        Taille du fichier : {(file_size / 1024):.2f} Ko        Nombre total d'éléments : {num_objects}")
    info_text.setStyleSheet("font-size: 24px;")
    layout.addWidget(info_text)

    #Créer la barre de recherche avec le text "Rechercher", puis l'ajouter dans ma vertical box
    search_bar = QLineEdit()
    search_bar.setPlaceholderText("Rechercher")
    layout.addWidget(search_bar)

    #Connection de la fonction qui filtre les mots recherchés quand on écrit dans la barre de recherche
    search_bar.textChanged.connect(filter_research)

    #Ajout du tableau dans la vertical box
    layout.addWidget(tableau)

    #Je set les header labels avec les "keys" trouvées précédemment
    mon_tableau.setHorizontalHeaderLabels(keys)

#Remplir le tableau à l'aide des données du fichier JSON
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

#Afficher les éléments qui correspondent à la recherche, et cacher les autres
def filter_research(text):

    #Pour toutes mes données provenant du JSON, je compare les données avec le texte entré et je cache les rangées qui n'ont pas rapport
    for row_index in range(len(data)):
        #Je commence par cacher la rangée, toujours
        mon_tableau.setRowHidden(row_index, True)
        for column_index in range(len(keys)):
            #Puis je ramène la rangée si au moins un de ses éléments match avec le texte entré dans la barre de recherche
            if (text.lower() in str(data[row_index][keys[column_index]]).lower()):#Je regarde juste les lettre minuscules, pour faciliter la recherche
                mon_tableau.setRowHidden(row_index, False)

#On demande à l'utilisateur d'entrer le chemin pour se rendre au fichier JSON
file_path = input("Quel est le chemin du fichier JSON?")

#Je ne sais pas ce que c'est exactement, mais il nous faut ça à la fin pour afficher le tableau
app = QApplication(sys.argv)

#On commence en testant le chargement du fichier json et on met celui-ci dans "data"
data = test_json(file_path)

#On récupère les informations du fichier, soit le nom, la taille, et le nombre d'objets
file_name = get_file_info(file_path)[0]
file_size = get_file_info(file_path)[1]
num_objects = get_file_info(file_path)[2]

#On va chercher les clés du fichier JSON. On les utilisera pour setter les horizontal header labels et pour naviguer dans "data"
keys = get_json_keys()

#Création de mon tableau avec autant de rangées que d'objets dans mon JSON, et autant de colonnes que de "keys"
mon_tableau = QTableWidget(len(data), len(keys))

#Création de ma fenêtre principale dans laquelle il y aura tous mes autres widgets
ma_window = QMainWindow()

#On set la fenêtre principale avec son tableau (et tout le reste)
set_window_and_stuff(ma_window, mon_tableau)

#Remplissage du tableau
fill_tableau(mon_tableau)

#Afficher ma fenêtre avec tout
ma_window.show()

#Executer le tableau? Dans tous les cas ça empêche l'ordi d'exploser! :)
sys.exit(app.exec())