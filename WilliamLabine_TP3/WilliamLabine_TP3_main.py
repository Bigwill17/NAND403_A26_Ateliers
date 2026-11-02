import os
import sys

# Print le path du dossier dans lequel se trouve ce même fichier
absolute_folder_path = os.path.dirname(os.path.abspath(__file__))

# On ajoute le path aux paths auxquels sys a accès
sys.path.append(absolute_folder_path)

# Dans mon fichier du UI, on importe la classe RandomAnimationUI
import WilliamLabine_TP3_ui

# On reload le fichier ui pour que Maya ne perde pas la tête
import importlib
importlib.reload(WilliamLabine_TP3_ui)

# Fonction main ;)
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = WilliamLabine_TP3_ui.RandomAnimationUI()
    widget.show()

main()