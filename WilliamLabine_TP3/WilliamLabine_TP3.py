import os
import sys

# Print le path du dossier dans lequel se trouve ce même fichier
y = os.path.dirname(os.path.abspath(__file__))
print(y)

# x = os.path.abspath(__file__)
# print(x)