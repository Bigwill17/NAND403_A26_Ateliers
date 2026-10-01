from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QTextEdit, QPushButton, QMessageBox
import sys

#Cette ligne est là pour faire fonctionner le code sans Maya
#app = QApplication(sys.argv)
 
class MessageBoard(QWidget):
    def __init__(self):
        #Initialisation de mon message board avec le contructeur de base
        super().__init__()
        self.setWindowTitle("Message board")
        self.create_ui()

    def create_ui(self):

        #Création du layout de mon message board
        layout = QVBoxLayout(self)

        #Création du texte de base dans mon message board
        label = QLabel("Message board")
        layout.addWidget(label)

        #Ajout de la zone d'entrée de texte
        text = QTextEdit()
        text.setPlaceholderText("Écrivez votre message")
        layout.addWidget(text)

        #Fonction appelée lorsqu'on appuie sur le bouton du message board
        def on_click(self):
            #On met le texte du QTextEdit dans la variable message_text
            message_text = text.toPlainText()

            #On crée la message box et on set son titre et son message
            message_box = QMessageBox()
            message_box.setText(message_text)
            message_box.setWindowTitle("Message box")

            #On l'affiche
            message_box.show()
            message_box.exec()

        #Création du bouton de mon message board
        button = QPushButton()
        button.setText("Envoyer")
        button.clicked.connect(on_click)
        layout.addWidget(button)

 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()

main()

#Cette ligne est là pour faire fonctionner le code sans Maya
#sys.exit(app.exec())