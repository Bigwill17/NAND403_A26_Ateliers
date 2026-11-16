import random
import os
import sys
import maya.cmds as cmds
from contextlib import contextmanager

#On trouve le path du dossier dans lequel se trouve ce même fichier
absolute_folder_path = os.path.dirname(os.path.abspath(__file__))

#On ajoute le path aux paths auxquels sys a accès
sys.path.append(absolute_folder_path)

#On importe le fichier du ui
import WilliamLabine_TP3_ui

#On reload le fichier ui pour que Maya ne perde pas la tête
import importlib
importlib.reload(WilliamLabine_TP3_ui)

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

def generate_random_animation(duration, step,
                              trans_min_x, trans_max_x, trans_min_y, trans_max_y, trans_min_z, trans_max_z,
                              rot_min_x, rot_max_x, rot_min_y, rot_max_y, rot_min_z, rot_max_z,
                              scale_min_x, scale_max_x, scale_min_y, scale_max_y, scale_min_z, scale_max_z):

    #En utilisant le chunk de control Z, on active toutes nos fonctionnalités
    with ctrlz_chunk():

        #On set le range de notre timeline dans Maya pour aller de 0 à duration
        cmds.playbackOptions(minTime = 0, animationStartTime = 0, maxTime = duration.value(), animationEndTime = duration.value())
        #Et on set la frame actuelle à 0, juste par esthétique, pour commencer au début
        cmds.currentTime(0)
        
        #On met tous les objets sélectionnés dans ma variables "objects"
        objects = cmds.ls(selection = True)

        #Pour tous les objets,
        for current_object in range(len(objects)):

            current_frame = 0

            #On set les variables initiales qui seront utilisées pour la première et dernière frame
            initial_trans_x = random.uniform(trans_min_x.value(), trans_max_x.value())
            initial_trans_y = random.uniform(trans_min_y.value(), trans_max_y.value())
            initial_trans_z = random.uniform(trans_min_z.value(), trans_max_z.value())
            initial_rot_x = random.uniform(rot_min_x.value(), rot_max_x.value())
            initial_rot_y = random.uniform(rot_min_y.value(), rot_max_y.value())
            initial_rot_z = random.uniform(rot_min_z.value(), rot_max_z.value())
            initial_scale_x = random.uniform(scale_min_x.value(), scale_max_x.value())
            initial_scale_y = random.uniform(scale_min_y.value(), scale_max_y.value())
            initial_scale_z = random.uniform(scale_min_z.value(), scale_max_z.value())

            while current_frame < duration.value():
                #On vérifie si on est à la frame 1
                if current_frame == 0:
                    #On set les valeurs initiales qui seront identiques à la première et à la dernière frame
                    cmds.setKeyframe(objects[current_object], attribute = "translateX", value = initial_trans_x, time = current_frame)
                    cmds.setKeyframe(objects[current_object], attribute = "translateY", value = initial_trans_y, time = current_frame)
                    cmds.setKeyframe(objects[current_object], attribute = "translateZ", value = initial_trans_z, time = current_frame)

                    cmds.setKeyframe(objects[current_object], attribute = "rotateX", value = initial_rot_x, time = current_frame)
                    cmds.setKeyframe(objects[current_object], attribute = "rotateY", value = initial_rot_y, time = current_frame)
                    cmds.setKeyframe(objects[current_object], attribute = "rotateZ", value = initial_rot_z, time = current_frame)

                    cmds.setKeyframe(objects[current_object], attribute = "scaleX", value = initial_scale_x, time = current_frame)
                    cmds.setKeyframe(objects[current_object], attribute = "scaleY", value = initial_scale_y, time = current_frame)
                    cmds.setKeyframe(objects[current_object], attribute = "scaleZ", value = initial_scale_z, time = current_frame)

                else:
                    #On set les translations X, Y et Z random selon les min et max
                    cmds.setKeyframe(objects[current_object], attribute = "translateX", value = random.uniform(trans_min_x.value(), trans_max_x.value()), time = current_frame)
                    cmds.setKeyframe(objects[current_object], attribute = "translateY", value = random.uniform(trans_min_y.value(), trans_max_y.value()), time = current_frame)
                    cmds.setKeyframe(objects[current_object], attribute = "translateX", value = random.uniform(trans_min_z.value(), trans_max_z.value()), time = current_frame)

                    #On set les rotations X, Y et Z random selon les min et max
                    cmds.setKeyframe(objects[current_object], attribute = "rotateX", value = random.uniform(rot_min_x.value(), rot_max_x.value()), time = current_frame)
                    cmds.setKeyframe(objects[current_object], attribute = "rotateY", value = random.uniform(rot_min_y.value(), rot_max_y.value()), time = current_frame)
                    cmds.setKeyframe(objects[current_object], attribute = "rotateZ", value = random.uniform(rot_min_z.value(), rot_max_z.value()), time = current_frame)

                    #On set les scales X, Y et Z random selon les min et max
                    cmds.setKeyframe(objects[current_object], attribute = "scaleX", value = random.uniform(scale_min_x.value(), scale_max_x.value()), time = current_frame)
                    cmds.setKeyframe(objects[current_object], attribute = "scaleY", value = random.uniform(scale_min_y.value(), scale_max_y.value()), time = current_frame)
                    cmds.setKeyframe(objects[current_object], attribute = "scaleZ", value = random.uniform(scale_min_z.value(), scale_max_z.value()), time = current_frame)

                #On avance dans les frames selon le step
                current_frame = current_frame + step.value()

            #On set la dernière frame + 1 avec les valeurs de la première, pour avoir une animation qui loop parfaitement!
            cmds.setKeyframe(objects[current_object], attribute = "translateX", value = initial_trans_x, time = duration.value() + 1)
            cmds.setKeyframe(objects[current_object], attribute = "translateY", value = initial_trans_y, time = duration.value() + 1)
            cmds.setKeyframe(objects[current_object], attribute = "translateZ", value = initial_trans_z, time = duration.value() + 1)
            
            cmds.setKeyframe(objects[current_object], attribute = "rotateX", value = initial_rot_x, time = duration.value() + 1)
            cmds.setKeyframe(objects[current_object], attribute = "rotateY", value = initial_rot_y, time = duration.value() + 1)
            cmds.setKeyframe(objects[current_object], attribute = "rotateZ", value = initial_rot_z, time = duration.value() + 1)
            
            cmds.setKeyframe(objects[current_object], attribute = "scaleX", value = initial_scale_x, time = duration.value() + 1)
            cmds.setKeyframe(objects[current_object], attribute = "scaleY", value = initial_scale_y, time = duration.value() + 1)
            cmds.setKeyframe(objects[current_object], attribute = "scaleZ", value = initial_scale_z, time = duration.value() + 1)

def delete_animation_keys():

    #On efface toutes les clés d'animation des objets sélectionnés
    cmds.cutKey(clear=True)