# write here a code for the main app and the first screen
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from instr import *

class Third_screen(QWidget):
    def __init__(self, info):
        super().__init__()
        self.info = info
        self.create_ui()
        self.set_appearance()
        self.show()
        
    def create_ui(self):
        self.cardiac_label = QLabel(txt_workheart + self.calculate_result())
        self.ruffier_label = QLabel(txt_index + str(self.index))
        self.name = QLabel("Name: " + self.info.name)
        self.age = QLabel("Age: " + str(self.info.age))

        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.name, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vlayout.addWidget(self.age, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vlayout.addWidget(self.ruffier_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vlayout.addWidget(self.cardiac_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.vlayout)

    def calculate_result(self):
        if self.info.age < 7:
            self.index = 0
            return "No info for this age"
        
        self.index = ((self.info.r_1 + self.info.r_2 + self.info.r_3) - 200) / 10

        if self.info.age >= 7 and self.info.age <= 8:
            if self.index >= 21:
                return txt_res1
            elif self.index >= 17 and self.index <= 20.9:
                return txt_res2
            elif self.index >= 12 and self.index <= 16.9:
                return txt_res3
            elif self.index >= 6.5 and self.index <= 11.9:
                return txt_res4
            elif self.index <= 6.4:
                return txt_res5
            
        elif self.info.age >= 9 and self.info.age <= 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index >= 19.4 and self.index <= 15.5:
                return txt_res2
            elif self.index >= 10.5 and self.index <= 15.4:
                return txt_res3
            elif self.index >= 5 and self.index <= 10.4:
                return txt_res4
            elif self.index <= 5:
                return txt_res5
        
        elif self.info.age >= 11 and self.info.age <= 12:
            if self.index >= 18:
                return txt_res1
            elif self.index >= 14 and self.index <= 17.9:
                return txt_res2
            elif self.index >= 9 and self.index <= 13.9:
                return txt_res3
            elif self.index >= 3.5 and self.index <= 8.9:
                return txt_res4
            elif self.index <= 3.4:
                return txt_res5
            
        elif self.info.age >= 13 and self.info.age <= 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index >= 12.5 and self.index <= 16.4:
                return txt_res2
            elif self.index >= 7.5 and self.index <= 12.4:
                return txt_res3
            elif self.index >= 2 and self.index <= 7.4:
                return txt_res4
            elif self.index <= 1.9:
                return txt_res5

        elif self.info.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index >= 11 and self.index <= 14.9:
                return txt_res2
            elif self.index >= 6 and self.index <= 10.9:
                return txt_res3
            elif self.index >= 0.5 and self.index <= 5.9:
                return txt_res4
            elif self.index <= 0.4:
                return txt_res5
    
    def set_appearance(self):
        self.setWindowTitle("Cardiovascular Test")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def next_screen(self):
        self.hide()
        self.ns = Third_screen()
    
    def initialise(self):
        self.send_result_button.clicked.connect(self.next_screen)