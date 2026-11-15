import random
import os
import sys
import maya.cmds as cmds

#On trouve le path du dossier dans lequel se trouve ce même fichier
absolute_folder_path = os.path.dirname(os.path.abspath(__file__))

#On ajoute le path aux paths auxquels sys a accès
sys.path.append(absolute_folder_path)

#On importe le fichier du ui
import WilliamLabine_TP3_ui

#On reload le fichier ui pour que Maya ne perde pas la tête
import importlib
importlib.reload(WilliamLabine_TP3_ui)

def generate_random_animation(duration, step,
                              trans_min_x, trans_max_x, trans_min_y, trans_max_y, trans_min_z, trans_max_z,
                              rot_min_x, rot_max_x, rot_min_y, rot_max_y, rot_min_z, rot_max_z,
                              scale_min_x, scale_max_x, scale_min_y, scale_max_y, scale_min_z, scale_max_z):
    #On met tous les objets sélectionnés dans ma variables "objects"
    objects = cmds.ls(selection = True)

    # print(step.value())

    #Pour tous les objets,
    for i in range(len(objects)):

        current_frame = 1

        #On set les variables initiales qui seront utilisées pour la première et dernière frame
        initial_trans_x = random.uniform(trans_min_x, trans_max_x)
        initial_trans_y = random.uniform(trans_min_y, trans_max_y)
        initial_trans_z = random.uniform(trans_min_z, trans_max_z)
        initial_rot_x = random.uniform(rot_min_x, rot_max_x)
        initial_rot_y = random.uniform(rot_min_y, rot_max_y)
        initial_rot_z = random.uniform(rot_min_z, rot_max_z)
        initial_scale_x = random.uniform(scale_min_x, scale_max_x)
        initial_scale_y = random.uniform(scale_min_y, scale_max_y)
        initial_scale_z = random.uniform(scale_min_z, scale_max_z)

        while current_frame < duration.value():
            #On vérifie si on est à la frame 1
            if current_frame == 1:
                #On set les valeurs initiales qui seront identiques à la première et à la dernière frame
                cmds.setKeyframe(objects[i], attribute = "translateX", value = initial_trans_x, time = current_frame)
                cmds.setKeyframe(objects[i], attribute = "translateY", value = initial_trans_y, time = current_frame)
                cmds.setKeyframe(objects[i], attribute = "translateZ", value = initial_trans_z, time = current_frame)

                cmds.setKeyframe(objects[i], attribute = "rotateX", value = initial_rot_x, time = current_frame)
                cmds.setKeyframe(objects[i], attribute = "rotateY", value = initial_rot_y, time = current_frame)
                cmds.setKeyframe(objects[i], attribute = "rotateZ", value = initial_rot_z, time = current_frame)

                cmds.setKeyframe(objects[i], attribute = "scaleX", value = initial_scale_x, time = current_frame)
                cmds.setKeyframe(objects[i], attribute = "scaleY", value = initial_scale_y, time = current_frame)
                cmds.setKeyframe(objects[i], attribute = "scaleZ", value = initial_scale_z, time = current_frame)

            #On set les translations X, Y et Z random selon les min et max
            cmds.setKeyframe(objects[i], attribute = "translateX", value = random.uniform(trans_min_x, trans_max_x), time = current_frame)
            cmds.setKeyframe(objects[i], attribute = "translateY", value = random.uniform(trans_min_y, trans_max_y), time = current_frame)
            cmds.setKeyframe(objects[i], attribute = "translateX", value = random.uniform(trans_min_z, trans_max_z), time = current_frame)

            #On set les rotations X, Y et Z random selon les min et max
            cmds.setKeyframe(objects[i], attribute = "rotateX", value = random.uniform(rot_min_x, rot_max_x), time = current_frame)
            cmds.setKeyframe(objects[i], attribute = "rotateY", value = random.uniform(rot_min_y, rot_max_y), time = current_frame)
            cmds.setKeyframe(objects[i], attribute = "rotateZ", value = random.uniform(rot_min_z, rot_max_z), time = current_frame)

            #On set les scales X, Y et Z random selon les min et max
            cmds.setKeyframe(objects[i], attribute = "scaleX", value = random.uniform(scale_min_x, scale_max_x), time = current_frame)
            cmds.setKeyframe(objects[i], attribute = "scaleY", value = random.uniform(scale_min_y, scale_max_y), time = current_frame)
            cmds.setKeyframe(objects[i], attribute = "scaleZ", value = random.uniform(scale_min_z, scale_max_z), time = current_frame)

            #On avance dans les frames selon le step
            current_frame = current_frame + step.value()

        #On met des valeurs dans le "translate X" pour que la cavalerie s'éloigne!
        # cmds.setKeyframe(objects[i], attribute = "translateX")
        # cmds.setKeyframe(objects[i], attribute = "translateX", value = 10, time = 30)
        # cmds.setKeyframe(objects[i], attribute = "translateX", value = 40, time = 60)
        # cmds.setKeyframe(objects[i], attribute = "translateX", value = 100, time = 100)