from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
 
class MessageBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message board")
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message board")
        layout.addWidget(label)

        #QTextEdit

        #QPushButton

        #def on_click(self)
            #print("on clicked call")
            
            #QMessageBox
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
  
main()