#!/usr/bin/python

import sys, random
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

@Slot()
def say_hello():
    price = random.randint(0, 10000)
    print(price)

# Create the Qt Application
app = QApplication(sys.argv)
# Create a button, connect it and show it
button = QPushButton("Price")
button.clicked.connect(say_hello)
button.show()
# Run the main Qt loop
app.exec()