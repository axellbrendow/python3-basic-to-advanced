import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QSizePolicy


class ResponsiveButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        font = self.font()
        font.setPixelSize(self.height() * 0.5)
        self.setFont(font)


class ResponsiveLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        font = self.font()
        font.setPixelSize(self.height() * 0.5)
        self.setFont(font)


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyCalc')
        self.cw = QWidget()  # Similar às divs do HTML ou Panels do java.swing
        self.grid = QGridLayout(self.cw)
        self.setStyleSheet('background-color: #3d3d3d')

        self.display = ResponsiveLineEdit()
        self.display.setDisabled(True)
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.display.setStyleSheet('background-color: rgba(255, 255, 255, 0.5)')
        self.grid.addWidget(self.display, 0, 0, 1, 5)

        for i in range(3):
            for j in range(3):
                self.add_btn(ResponsiveButton(f'{i * 3 + j + 1}'), i + 1, j, 1, 1)

        self.add_btn(ResponsiveButton('.'), 4, 0, 1, 1)
        self.add_btn(ResponsiveButton('0'), 4, 1, 1, 1)
        self.add_btn(ResponsiveButton(','), 4, 2, 1, 1)

        self.add_btn(ResponsiveButton('+'), 1, 3, 1, 1)
        self.add_btn(ResponsiveButton('-'), 2, 3, 1, 1)
        self.add_btn(ResponsiveButton('*'), 3, 3, 1, 1)
        self.add_btn(ResponsiveButton('/'), 4, 3, 1, 1)

        self.add_btn(ResponsiveButton('Backspace'), 1, 4, 1, 1,
                     lambda: self.display.setText(self.display.text()[:-1])
                     if self.display.text() else None)
        self.add_btn(ResponsiveButton('C'), 2, 4, 1, 1, lambda: self.display.setText(''))
        self.add_btn(ResponsiveButton(''), 3, 4, 1, 1)
        self.add_btn(ResponsiveButton('='), 4, 4, 1, 1, self.eval_eq)

        self.setCentralWidget(self.cw)

    def add_btn(self, btn: QPushButton, row, column, rowspan, columnspan, funcao=None, style=None):
        btn.clicked.connect(
            funcao if funcao
            else lambda: self.display.setText(self.display.text() + btn.text()))
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        if style:
            btn.setStyleSheet('background-color: #ffaf40')

        else:
            btn.setStyleSheet('background-color: gray')

        self.grid.addWidget(btn, row, column, rowspan, columnspan)

    def eval_eq(self):
        try:
            self.display.setText(str(eval(self.display.text())))

        except Exception as e:
            self.display.setText('Expressão inválida')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Calculadora()
    app.show()
    qt.exec_()
