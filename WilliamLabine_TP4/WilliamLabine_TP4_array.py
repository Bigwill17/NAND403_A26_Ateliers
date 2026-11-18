import sys
import os
import maya.cmds as cmds
from contextlib import contextmanager

#On trouve le path du dossier dans lequel se trouve ce même fichier
absolute_folder_path = os.path.dirname(os.path.abspath(__file__))

#On ajoute le path aux paths auxquels sys a accès
sys.path.append(absolute_folder_path)

#On importe le fichier du ui
import WilliamLabine_TP4_ui as ui

# #On reload le fichier ui pour que Maya ne perde pas la tête
import importlib
importlib.reload(ui)

#Création de la fonction spéciale qui ouvre et ferme un "chunk" avec toutes les lignes de codes choisies
@contextmanager
def ctrlz_chunk():
    #On ouvre le chunk au début
    cmds.undoInfo(openChunk=True)
    try:
        yield
    finally:
        #On s'assure de refermer le chunk!
        cmds.undoInfo(closeChunk=True)

def make_array_in_a_line(line_x_count, line_y_count, line_z_count, line_x_offset, line_y_offset, line_z_offset, line_merge,
                         circle_r_count, circle_y_count, circle_r_offset, circle_y_offset, circle_merge, created_shapes, merged_result):

    #En utilisant le chunk de control Z, on active toutes nos fonctionnalités
    with ctrlz_chunk():

        #On set l'objet source (le premier objet sélectionné, normalement le seul)
        selection = cmds.ls(selection = True, transforms = True)
        source = selection[0]

        for current_shape in created_shapes:
            cmds.delete(current_shape)

        created_shapes.clear()

        for current_merge in merged_result:
            print("Hello")
            cmds.delete(current_merge)

        merged_result.clear()

        #Exécution des boucles pour le "centre"
        for zIdx in range(line_z_count - 1):
            for yIdx in range(line_y_count - 1):
                for xIdx in range(line_x_count - 1):
                    copy = cmds.duplicate(source)[0]
                    cmds.move(line_x_offset + (line_x_offset * xIdx), line_y_offset + (line_y_offset * yIdx), line_z_offset + (line_z_offset * zIdx), copy, relative = True)
                    created_shapes.append(copy)

        #Exécution des boucles pour les "edges"
        for xIdx in range(line_x_count - 1):
            copy = cmds.duplicate(source)[0]
            cmds.move(line_x_offset + (line_x_offset * xIdx), 0, 0, copy, relative = True)
            created_shapes.append(copy)

        for yIdx in range(line_y_count - 1):
            copy = cmds.duplicate(source)[0]
            cmds.move(0, line_y_offset + (line_y_offset * yIdx), 0, copy, relative = True)
            created_shapes.append(copy)

        for zIdx in range(line_z_count - 1):
            copy = cmds.duplicate(source)[0]
            cmds.move(0, 0, line_z_offset + (line_z_offset * zIdx), copy, relative = True)
            created_shapes.append(copy)

        #Exécution des boucles pour les "faces"
        for xIdx in range(line_x_count - 1):
            for yIdx in range(line_y_count - 1):
                copy = cmds.duplicate(source)[0]
                cmds.move(line_x_offset + (line_x_offset * xIdx), line_y_offset + (line_y_offset * yIdx), 0, copy, relative = True)
                created_shapes.append(copy)

        for yIdx in range(line_y_count - 1):
            for zIdx in range(line_z_count - 1):
                copy = cmds.duplicate(source)[0]
                cmds.move(0, line_y_offset + (line_y_offset * yIdx), line_z_offset + (line_z_offset * zIdx), copy, relative = True)
                created_shapes.append(copy)

        for zIdx in range(line_z_count - 1):
            for xIdx in range(line_x_count - 1):
                copy = cmds.duplicate(source)[0]
                cmds.move(line_x_offset + (line_x_offset * xIdx), 0, line_z_offset + (line_z_offset * zIdx), copy, relative = True)
                created_shapes.append(copy)

        #On merge si l'option de merge est cochée
        if line_merge == True:
            if len(created_shapes) >= 2:
                merged_result.extend(cmds.polyUnite(created_shapes, name = "Merged_Result", ch = False))
                created_shapes.clear()

        cmds.select(source)


def make_array_in_circle(line_x_count, line_y_count, line_z_count, line_x_offset, line_y_offset, line_z_offset, line_merge,
                         circle_r_count, circle_y_count, circle_r_offset, circle_y_offset, circle_merge):

    #En utilisant le chunk de control Z, on active toutes nos fonctionnalités
    with ctrlz_chunk():

        for i in range(circle_r_count):
            print("Array in a circle!")