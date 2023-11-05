# Importing from the PyQt6 libraries
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

# Importing from other .py files
from instr import *
from second_win import *

# Creating the application container
app = QApplication([])

# Creating our own class for the first window, INHERITING from QWidget
class First_screen(QWidget):
    def __init__(self):
        # Call the parent constructor to inherit everything
        super().__init__()

        # Create and organise the user interface components
        self.create_ui()

        # Give the window a name, resize it, and move it to specific location
        self.set_appearance()

        # Initialise the buttons
        self.initialise()

        # Show the first window
        self.show()

    def create_ui(self):
        self.intro = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.start_button = QPushButton(txt_next)

        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.intro, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout.addWidget(self.instruction, alignment=Qt.AlignmentFlag.AlignLeft)
        self.vlayout.addWidget(self.start_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(self.vlayout)
    
    def set_appearance(self):
        self.setWindowTitle("Cardiovascular Test")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def next_screen(self):
        self.hide()
        self.ns = Second_screen()
    
    def initialise(self):
        self.start_button.clicked.connect(self.next_screen)

first_screen = First_screen()
app.exec()