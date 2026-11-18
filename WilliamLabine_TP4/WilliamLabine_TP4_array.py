import random
import os
import sys
import maya.cmds as cmds
from contextlib import contextmanager

#On trouve le path du dossier dans lequel se trouve ce même fichier
absolute_folder_path = os.path.dirname(os.path.abspath(__file__))

#On ajoute le path aux paths auxquels sys a accès
sys.path.append(absolute_folder_path)

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

def make_array_in_a_line():

    #En utilisant le chunk de control Z, on active toutes nos fonctionnalités
    with ctrlz_chunk():

        print("Array in a line!")

def make_array_in_circle():

    #En utilisant le chunk de control Z, on active toutes nos fonctionnalités
    with ctrlz_chunk():

        print("Array in circle!")