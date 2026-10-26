import maya.cmds as cmds

#On met tous les objets sélectionnés dans ma variables "objects"
objects = cmds.ls(selection = True)

#Pour tous les objets,
for i in range(len(objects)):
    #On met des valeurs dans le "translate X" pour que la cavalerie s'éloigne!
    cmds.setKeyframe(objects[i], attribute = "translateX")
    cmds.setKeyframe(objects[i], attribute = "translateX", value = 10, time = 30)
    cmds.setKeyframe(objects[i], attribute = "translateX", value = 40, time = 60)
    cmds.setKeyframe(objects[i], attribute = "translateX", value = 100, time = 90)

#On set la durée de l'animation pour commencer à 0 et terminer à 100
cmds.playbackOptions(min = 0, max = 100)