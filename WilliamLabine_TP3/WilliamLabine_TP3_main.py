import os
import sys

# Print le path du dossier dans lequel se trouve ce même fichier
absolute_folder_path = os.path.dirname(os.path.abspath(__file__))

# On ajoute le path aux paths auxquels sys a accès
sys.path.append(absolute_folder_path)

# Dans mon fichier du UI, on importe la classe RandomAnimationUI
from WilliamLabine_TP3_ui import RandomAnimationUI

def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    random_animation_ui = RandomAnimationUI()
    random_animation_ui.show()

main()