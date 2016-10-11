#!/usr/bin/env python
# coding: UTF-8

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from random import randint
import sys
import time

WINDOW_SIZE = (400, 400)
CELL_MAX_X = CELL_MAX_Y = 15
CELL_WIDTH = CELL_HEIGHT = 32
SPACING_BETWEEN_CELLS = 1

DEFAULT_ROBOT_POS = (1, 1)


class Cell(QtWidgets.QPushButton):
    def __init__(self, master=None):
        super(Cell, self).__init__(master)
        self.setStyleSheet("background-color: black")
        self.setFixedWidth(CELL_WIDTH)
        self.setFixedHeight(CELL_HEIGHT)


class LoadCell(Cell):
    pass


class UserCell(Cell):
    def __init__(self, master=None, pos=None):
       super(UserCell, self).__init__(master)
       self.setIcon(QtGui.QIcon('robo.png'))
       self.setText('U')
       self._pos = pos

    def move(self, vec):
        self._pos[0] += vec[0]
        self._pos[1] += vec[1]


class Bord(QtWidgets.QWidget):
    def __init__(self, master=None):
        super(Bord, self).__init__(master)

        self._grid = QtWidgets.QGridLayout()
        self.initUI()
        self.show()

    def initUI(self):
        self._grid.setSpacing(SPACING_BETWEEN_CELLS)
        self.setLayout(self._grid)
        self.cell_mat = [
            [0 for y in range(CELL_MAX_Y)] for x in range(CELL_MAX_X)]
        for i in range(CELL_MAX_Y):
            for j in range(CELL_MAX_X):
                self.cell_mat[i][j] = LoadCell(master=self)
                self._grid.addWidget(self.cell_mat[i][j], i, j)
        usercell = UserCell(self, pos=list(DEFAULT_ROBOT_POS))
        self._grid.addWidget(usercell, DEFAULT_ROBOT_POS[0], DEFAULT_ROBOT_POS[1])
        self.update()


    def update(self):
        time.sleep(3)
        self._grid.removeWidget(self.cell_mat[1][1])
        self.cell_mat[1][1].setParent(None)
        print("stu")


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Bord()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
