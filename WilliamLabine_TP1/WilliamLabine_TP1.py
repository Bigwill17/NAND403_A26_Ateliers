import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow

import json

with open('data_small.json') as json_file:
    data = json.load(json_file)

print(data)