# write here a code for the main app and the first screen
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from instr import *

class Third_screen(QWidget):
    def __init__(self):
        super().__init__()
        self.create_ui()
        self.set_appearance()
        self.show()

    def create_ui(self):
        self.ruffier_label = QLabel(txt_index)
        self.cardiac_label = QLabel(txt_workheart)

        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.ruffier_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vlayout.addWidget(self.cardiac_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.vlayout)

    
    def set_appearance(self):
        self.setWindowTitle("Cardiovascular Test")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def next_screen(self):
        self.hide()
        self.ns = Third_screen()
    
    def initialise(self):
        self.send_result_button.clicked.connect(self.next_screen)