#Importer toutes les dépendances avant de pleurer
import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow

#Demander au dude son nom et sa ville avec des inputs
son_nom = input("Quel est ton nom?\n")
sa_ville_dorigine = input("D'où viens-tu?\n")

#Afficher les réponses directement dans la console
#print("Son nom est : ", son_nom)
#print("Il vient de : ", sa_ville_dorigine)

#Je ne sais pas ce que c'est exactement, mais il nous faut ça à la fin pour afficher le tableau
app = QApplication(sys.argv)

#Création de mon tableau qui affichera le nom et la ville
mon_tableau = QTableWidget(1, 2)

#Setter le nom des colonnes du tableau
mon_tableau.setHorizontalHeaderLabels(["Nom", "Ville"])

#Setter les deux valeurs du tableau avec le nom et la ville
mon_tableau.setItem(0, 0, QTableWidgetItem(son_nom))
mon_tableau.setItem(0, 1, QTableWidgetItem(sa_ville_dorigine))

#Afficher le tableau (je pense)
mon_tableau.show()

#Executer le tableau?
sys.exit(app.exec())