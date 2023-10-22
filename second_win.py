# write here a code for the main app and the first screen
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from instr import *
from final_win import *

class Second_screen(QWidget):
    def __init__(self):
        super().__init__()
        self.create_ui()
        self.set_appearance()
        self.initialise()
        self.show()

    def create_ui(self):
        self.full_name = QLabel(txt_name)
        self.full_name_field = QLineEdit()
        self.full_name_field.setPlaceholderText(txt_hintname)
        
        self.age = QLabel(txt_age)
        self.age_field = QLineEdit()
        self.age_field.setPlaceholderText(txt_hintage)

        self.first_instr = QLabel(txt_test1)
        self.first_button = QPushButton(txt_starttest1)
        self.first_button_field = QLineEdit()
        self.first_button_field.setPlaceholderText(txt_hinttest1)

        self.second_instr = QLabel(txt_test2)
        self.second_button = QPushButton(txt_starttest2)
        self.second_button_field = QLineEdit()
        self.second_button_field.setPlaceholderText(txt_hinttest2)

        self.third_instr = QLabel(txt_test3)
        self.third_button = QPushButton(txt_starttest3)
        self.third_button_field = QLineEdit()
        self.third_button_field.setPlaceholderText(txt_hinttest3)

        self.send_result_button = QPushButton(txt_sendresults)
        self.timer = QLabel(txt_timer)\

        self.hlayout = QHBoxLayout()
        self.vlayout_1 = QVBoxLayout()
        self.vlayout_2 = QVBoxLayout()
        
        self.hlayout.addLayout(self.vlayout_1)
        self.hlayout.addLayout(self.vlayout_2)

        self.vlayout_1.addWidget(self.full_name, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout_1.addWidget(self.full_name_field, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout_1.addWidget(self.age, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout_1.addWidget(self.age_field, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout_1.addWidget(self.first_instr, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout_1.addWidget(self.first_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout_1.addWidget(self.first_button_field, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout_1.addWidget(self.second_instr, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout_1.addWidget(self.second_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout_1.addWidget(self.second_button_field, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout_1.addWidget(self.third_instr, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout_1.addWidget(self.third_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout_1.addWidget(self.third_button_field, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout_1.addWidget(self.send_result_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.vlayout_2.addWidget(self.timer, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setLayout(self.hlayout)
    
    def set_appearance(self):
        self.setWindowTitle("Cardiovascular Test")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def next_screen(self):
        self.hide()
        self.ns = Third_screen()
    
    def initialise(self):
        self.send_result_button.clicked.connect(self.next_screen)