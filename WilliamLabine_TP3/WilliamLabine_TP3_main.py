import os
import sys

#On trouve le path du dossier dans lequel se trouve ce même fichier
absolute_folder_path = os.path.dirname(os.path.abspath(__file__))

#On ajoute le path aux paths auxquels sys a accès
sys.path.append(absolute_folder_path)

#On importe le fichier du ui
import WilliamLabine_TP3_ui as ui

#On reload le fichier ui pour que Maya ne perde pas la tête
import importlib
importlib.reload(ui)

# Fonction main ;)
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = ui.RandomAnimationUI()
    widget.show()

main()