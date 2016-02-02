#!/usr/bin/env python
# coding: UTF-8

from PyQt4 import QtGui
from random import randint
import sys

WINDOW_SIZE = (400, 400)
CELL_MAX_X = CELL_MAX_Y = 15
CELL_WIDTH = CELL_HEIGHT = 32
SPACING_BETWEEN_CELLS = 1

class Cell(QtGui.QPushButton):
    def __init__(self, master=None):
        super(Cell, self).__init__(master)
        self.setStyleSheet("background-color: black")
        self.setFixedWidth(CELL_WIDTH)
        self.setFixedHeight(CELL_HEIGHT)

class LoadCell(Cell):
    pass

class UserCell(Cell):
    def __init__(self, master=None):
       super(UserCell, self).__init__(master)
       # self.setIcon(QtGui.QIcon('robo.png'))
       self.setText('U')

class Bord(QtGui.QWidget):
    def __init__(self, master=None):
        super(Bord, self).__init__(master)
        self.initUI()
        self.show()

    def initUI(self):
        grid = QtGui.QGridLayout()
        grid.setSpacing(SPACING_BETWEEN_CELLS)
        self.setLayout(grid)
        self.cell_mat = [
            [0 for y in range(CELL_MAX_Y)] for x in range(CELL_MAX_X)]
        for i in range(CELL_MAX_Y):
            for j in range(CELL_MAX_X):
                self.cell_mat[i][j] = LoadCell(master=self)
                grid.addWidget(self.cell_mat[i][j], i, j)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Bord()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
