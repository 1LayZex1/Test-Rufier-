from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit
)
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        '''окно, в котором проводится опрос'''
        super().__init__()
        #создаём и настраиваем графические элементы:
        self.initUI()
        #уcтанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        #старт:
        self.show()

def initUI(self):
        '''создаём графические элементы'''
        self.workh_text = QLabel(workheart)
        self.index_text = QLabel(txt_index)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)

    '''уcтанавливает, как будет выглядеть окно (надпись, размер, место)'''
        '''уcтанавливает, как будет выглядеть окно (надпись, размер, место)'''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)