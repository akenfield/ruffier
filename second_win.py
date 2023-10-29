# write here a code for the main app and the first screen
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from instr import *
from final_win import *

class Patient_Info():
    def __init__(self, name, age, r_1, r_2, r_3):
        self.name = name
        self.age = int(age)
        self.r_1 = int(r_1)
        self.r_2 = int(r_2)
        self.r_3 = int(r_3)

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
        self.timer = QLabel(txt_timer)

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
        info = Patient_Info(self.full_name_field.text(), self.age_field.text(), self.first_button_field.text(), self.second_button_field.text(), self.third_button_field.text())
        self.ns = Third_screen(info)


    def display_timer_a(self):
        self.timer.setText(time.toString("hh:mm:ss"))
        self.timer.setFont(QFont("Times", 36, QFont.Weight.Bold))
        self.timer.setStyleSheet("color: rgb(0, 0, 0)")

    def cd_a(self):
        global time
        time = time.addSecs(-1)
        self.display_timer_a()
        seconds = QTime(0,0,0).secsTo(time)
        if seconds <= 0:
            self.timer_widget.stop()

    def display_timer_b(self):
        self.timer.setText(time.toString("hh:mm:ss"))
        self.timer.setFont(QFont("Times", 36, QFont.Weight.Bold))
        seconds = QTime(0,0,0).secsTo(time)
        if seconds > 45 or seconds < 16:
            self.timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.timer.setStyleSheet("color: rgb(0,0,0)")

    def cd_b(self):
        global time
        time = time.addSecs(-1)
        self.display_timer_b()
        seconds = QTime(0,0,0).secsTo(time)
        if seconds <= 0:
            self.timer_widget.stop()

    def test_1_timer(self):
        global time
        time = QTime(0, 0 , 15)
        self.display_timer_a()
        self.timer_widget = QTimer()
        self.timer_widget.start(1000)
        self.timer_widget.timeout.connect(self.cd_a)

    def test_2_timer(self):
        global time
        time = QTime(0, 0 , 45)
        self.display_timer_a()
        self.timer_widget = QTimer()
        self.timer_widget.start(1000)
        self.timer_widget.timeout.connect(self.cd_a)

    def test_3_timer(self):
        global time
        time = QTime(0, 1, 0)
        self.display_timer_b()
        self.timer_widget = QTimer()
        self.timer_widget.start(1000)
        self.timer_widget.timeout.connect(self.cd_b)

    def initialise(self):
        self.send_result_button.clicked.connect(self.next_screen)
        self.first_button.clicked.connect(self.test_1_timer)
        self.second_button.clicked.connect(self.test_2_timer)
        self.third_button.clicked.connect(self.test_3_timer)