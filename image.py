import imghdr
import sys

from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def browseimage():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog

    filname =QFileDialog.getOpenFileName()
    imagepath = filname[0]

    with open(imagepath, 'rb') as f:
        file_data = f.read()
        print(file_data,'-------------------------\n')
        file_type = imghdr.what(f.name)
        file_name = f.name
        print(file_name)

app = QApplication(sys.argv)
w = QWidget()
w.resize(400,350)
w.move(100,120)

btn = QPushButton('Close', w)
btn.resize(80,80)
btn.move(50,90)
btn.setToolTip('exit')
btn.clicked.connect(browseimage)
w.setGeometry(100,120,400,350)
w.setWindowTitle('browsing image')

w.show()


app.exec_()