#!/usr/bin/env python
# coding: UTF-8

from PyQt4 import QtGui
import sys

WINDOW_SIZE = (400, 400)
CELL_MAX_X = CELL_MAX_Y = 15

class Bord(QtGui.QWidget):
    def __init__(self, master=None):
        super(Bord, self).__init__(master)
        self.initUI()
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Bord()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
