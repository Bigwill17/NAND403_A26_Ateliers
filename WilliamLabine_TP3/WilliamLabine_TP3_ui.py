from PySide6.QtWidgets import QWidget

class RandomAnimationUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Animation Tool")
        self.setMinimumWidth(400)