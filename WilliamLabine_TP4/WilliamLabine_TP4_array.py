import random
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
    cmds.undoInfo(openChunk = True)
    try:
        yield
    finally:
        #On s'assure de refermer le chunk!
        cmds.undoInfo(closeChunk = True)

def make_array_in_a_line(x_count, y_count, z_count,
                         x_offset, y_offset, z_offset,
                         trans_random, rot_random, scale_random, seed,
                         created_shapes):

    #En utilisant le chunk de control Z, on active toutes nos fonctionnalités
    with ctrlz_chunk():

        #On set l'objet source (le premier objet sélectionné, normalement le seul)
        selection = cmds.ls(selection = True, transforms = True)
        source = selection[0]

        #On supprime toutes les formes créées au cycle d'avant
        for current_shape in created_shapes:
            cmds.delete(current_shape)
        created_shapes.clear()

        #On set la seed selon la valeur du spinbox
        random.seed(seed)

        #Exécution des boucles pour le line array
        for zIdx in range(z_count):
            for yIdx in range(y_count):
                for xIdx in range(x_count):
                    copy = cmds.duplicate(source)[0]
                    cmds.move(x_offset * xIdx + (random.uniform(-0.5, 0.5) * trans_random / 100),
                              y_offset * yIdx + (random.uniform(-0.5, 0.5) * trans_random / 100),
                              z_offset * zIdx + (random.uniform(-0.5, 0.5) * trans_random / 100),
                              copy, relative = True)
                    cmds.rotate((random.uniform(-180, 180) * rot_random / 100),
                                (random.uniform(-180, 180) * rot_random / 100),
                                (random.uniform(-180, 180) * rot_random / 100),
                                copy, relative = True)
                    random_scale = (random.uniform(-0.5, 0.5) * scale_random / 100) + 1
                    cmds.scale(random_scale,
                               random_scale,
                               random_scale,
                               copy, relative = True)
                    created_shapes.append(copy)

        #On s'assure de toujours avoir l'objet source sélectionné à la fin d'un cycle
        cmds.select(source)


def make_array_in_circle(r_count, y_count,
                         center_distance, r_offset, y_offset,
                         trans_random, rot_random, scale_random, seed,
                         created_shapes):

    #En utilisant le chunk de control Z, on active toutes nos fonctionnalités
    with ctrlz_chunk():

        #On set l'objet source (le premier objet sélectionné, normalement le seul)
        selection = cmds.ls(selection = True, transforms = True)
        source = selection[0]

        #On supprime toutes les formes créées au cycle d'avant
        for current_shape in created_shapes:
            cmds.delete(current_shape)
        created_shapes.clear()

        #On va chercher le pivot de notre objet source autour duquel on va tourner
        circle_pivot = cmds.xform(source, query = True, worldSpace = True, rotatePivot = True)

        #On set la seed selon la valeur du spinbox
        random.seed(seed)

        #Exécution de la boucle du circle array
        for yIdx in range(y_count):
            for rIdx in range(r_count):
                copy = cmds.duplicate(source)[0]
                cmds.move(center_distance + (random.uniform(-0.5, 0.5) * trans_random / 100),
                          y_offset * yIdx + (random.uniform(-0.5, 0.5) * trans_random / 100),
                          (random.uniform(-0.5, 0.5) * trans_random / 100),
                          copy, relative = True)
                cmds.rotate((random.uniform(-180, 180) * rot_random / 100),
                            (random.uniform(-180, 180) * rot_random / 100),
                            (random.uniform(-180, 180) * rot_random / 100),
                            copy, relative = True)
                cmds.rotate(0, (360 * rIdx / r_count) + (r_offset * yIdx), 0, copy, pivot = circle_pivot, relative = True)
                random_scale = (random.uniform(-0.5, 0.5) * scale_random / 100) + 1
                cmds.scale(random_scale,
                            random_scale,
                            random_scale,
                            copy, relative = True)
                created_shapes.append(copy)

        #On s'assure de toujours avoir l'objet source sélectionné à la fin d'un cycle
        cmds.select(source)

def confirm(self, merge, created_shapes, merged_result):

    #En utilisant le chunk de control Z, on active toutes nos fonctionnalités
    with ctrlz_chunk():

        #On set l'objet source, on le supprimera après
        selection = cmds.ls(selection = True, transforms = True)

        #On merge si l'option de merge est cochée
        if merge == True:
            if len(created_shapes) >= 2:
                merged_result.extend(cmds.polyUnite(created_shapes, name = "Merged_Result", ch = False))
                created_shapes.clear()

            else:
                print("You need at least an array of 2 to merge")

        #On supprime l'objet source
        cmds.delete(selection[0])

        #On ferme le widget
        self.close()


def cancel(self, created_shapes, merged_result):

    #En utilisant le chunk de control Z, on active toutes nos fonctionnalités
    with ctrlz_chunk():

        for current_shape in created_shapes:
            cmds.delete(current_shape)

        created_shapes.clear()

        for current_merge in merged_result:
            cmds.delete(current_merge)

        merged_result.clear()

        #On ferme le widget
        self.close()

def import_suzanne():

    #On trouve le path du dossier dans lequel se trouve ce même fichier
    absolute_folder_path = os.path.dirname(os.path.abspath(__file__))

    #On greffe le fichier de Suzanne au path
    suzanne_path = absolute_folder_path + "\SM_Suzanne.fbx"

    #On importe Suzanne
    cmds.file(suzanne_path, i = True)