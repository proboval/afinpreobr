from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint
from form import Ui_Form

import sys


class mywindow(QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Form()
        self.start_paint = False
        self.paint_pol = True
        self.dek = True
        self.transfer = False
        self.scaling = False
        self.reflection = False
        self.turn = False

        self.arrPol_pi = []
        self.arrPol_dek_x = []
        self.arrPol_dek_y = []
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.buttonClicked())
        self.ui.pushButton_2.clicked.connect(lambda: self.buttonClicked_2())
        self.ui.pushButton_3.clicked.connect(lambda: self.buttonClicked_3())
        self.ui.pushButton_4.clicked.connect(lambda: self.buttonClicked_4())
        self.ui.pushButton_5.clicked.connect(lambda: self.buttonClicked_5())
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Афинные преобразования")
        self.show()

    def buttonClicked(self):
        if self.ui.pushButton.text() == "Начать отрисовку Фигуры":
            self.ui.pushButton.setText("Закончить отрисовку")
            self.start_paint = True
            self.paint_pol = False
            self.dek = False
            self.arrPol_pi.clear()
            self.ui.tableWidget.clear()
        else:
            self.ui.pushButton.setText("Начать отрисовку Фигуры")
            self.start_paint = False
            self.paint_pol = True
            self.dek = True
            self.update()

    def buttonClicked_2(self):
        self.transfer = True
        self.scaling = False
        self.reflection = False
        self.turn = False
        self.update()

    def buttonClicked_3(self):
        self.transfer = False
        self.scaling = True
        self.reflection = False
        self.turn = False
        self.update()

    def buttonClicked_4(self):
        self.transfer = False
        self.scaling = False
        self.reflection = True
        self.turn = False
        self.update()

    def buttonClicked_5(self):
        self.transfer = False
        self.scaling = False
        self.reflection = False
        self.turn = True
        self.update()

    def mousePressEvent(self, event):
        if self.start_paint:
            pos = event.pos()
            self.arrPol_pi.append(pos)

            self.update()

    def paintEvent(self, e):
        qp = QPainter()
        size = self.size()
        dx = 20
        qp.begin(self)
        mid = size.width() // 2
        qp.drawRect(5, 5, mid - 10, mid - 10)
        qp.drawRect(mid, 5, mid - 5, mid - 10)
        y0 = mid // 2
        x0_1 = mid // 2
        x0_2 = x0_1 + mid
        n = mid // dx
        n = n // 2 + 1

        for i in range(n):
            if i == 0:
                qp.setPen(QPen(Qt.red))
                qp.drawLine(x0_1 + dx * i, 5, x0_1 + dx * i, mid - 5)
                qp.drawLine(x0_1 + dx * i, 5, x0_1 + dx * i - 4, 5 + 8)
                qp.drawLine(x0_1 + dx * i, 5, x0_1 + dx * i + 4, 5 + 8)
                qp.drawText(x0_1 + dx * i + 4, 5 + 8, "y")

                qp.drawLine(x0_2 + dx * i, 5, x0_2 + dx * i, mid - 5)
                qp.drawLine(x0_2 + dx * i, 5, x0_2 + dx * i - 4, 5 + 8)
                qp.drawLine(x0_2 + dx * i, 5, x0_2 + dx * i + 4, 5 + 8)
                qp.drawText(x0_2 + dx * i + 4, 5 + 8, "y")
                qp.setPen((QPen(Qt.black)))
            else:
                qp.drawLine(x0_1 + dx * i, 5, x0_1 + dx * i, mid - 5)
                qp.drawLine(x0_1 - dx * i, 5, x0_1 - dx * i, mid - 5)

                qp.drawLine(x0_2 + dx * i, 5, x0_2 + dx * i, mid - 5)
                qp.drawLine(x0_2 - dx * i, 5, x0_2 - dx * i, mid - 5)

        k = mid // dx // 2

        for i in range(0, k + 1):
            if i == 0:
                qp.setPen(QPen(Qt.red))
                qp.drawLine(5, y0 + dx * i, mid - 5, y0 + dx * i)
                qp.drawLine(mid - 5, y0 + dx * i, mid - 15, y0 + dx * i - 4)
                qp.drawLine(mid - 5, y0 + dx * i, mid - 15, y0 + dx * i + 4)
                qp.drawText(mid - 18, y0 + dx * i - 6, "x")
                qp.drawLine(mid, y0 + dx * i, size.width() - 5, y0 + dx * i)
                qp.drawLine(size.width() - 5, y0 + dx * i, size.width() - 15, y0 + dx * i - 4)
                qp.drawLine(size.width() - 5, y0 + dx * i, size.width() - 15, y0 + dx * i + 4)
                qp.drawText(size.width() - 18, y0 + dx * i - 6, "x")
                qp.setPen((QPen(Qt.black)))
            else:
                qp.drawLine(5, y0 + dx * i, mid - 5, y0 + dx * i)
                qp.drawLine(5, y0 - dx * i, mid - 5, y0 - dx * i)
                qp.drawLine(mid, y0 + dx * i, size.width() - 5, y0 + dx * i)
                qp.drawLine(mid, y0 - dx * i, size.width() - 5, y0 - dx * i)

        pen = QPen(QPen(Qt.darkBlue, 2))

        qp.setPen(pen)
        for i in range(len(self.arrPol_pi)):
            qp.drawPoint(self.arrPol_pi[i])

        if len(self.arrPol_pi) != 0 and self.paint_pol:
            qp.drawPolygon(self.arrPol_pi)

        if self.dek:
            for i in range(len(self.arrPol_pi)):
                self.arrPol_dek_x.append((self.arrPol_pi[i].x() - x0_1) / dx)
                self.arrPol_dek_y.append((y0 - self.arrPol_pi[i].y()) / dx)

            self.ui.tableWidget.setColumnCount(len(self.arrPol_pi))
            for i in range(len(self.arrPol_dek_x)):
                self.ui.tableWidget.setItem(0, i, QTableWidgetItem(str(self.arrPol_dek_x[i])))
                self.ui.tableWidget.setItem(1, i, QTableWidgetItem(str(self.arrPol_dek_y[i])))



        if self.transfer:
            tr_dek = self.ui.doubleSpinBox.value()
            arrPol_dek_y_new = []
            for i in range(len(self.arrPol_dek_y)):
                arrPol_dek_y_new.append(self.arrPol_dek_y[i] + tr_dek)

            arrPol_pi_new = []

            self.ui.tableWidget_2.setColumnCount(len(self.arrPol_pi))
            for i in range(len(self.arrPol_dek_x)):
                self.ui.tableWidget_2.setItem(0, i, QTableWidgetItem(str(self.arrPol_dek_x[i])))
                self.ui.tableWidget_2.setItem(1, i, QTableWidgetItem(str(arrPol_dek_y_new[i])))

            for i in range(len(self.arrPol_dek_x)):
                arrPol_pi_new.append(QPoint(int(round((self.arrPol_dek_x[i] * dx + x0_2))), int(round(y0 - arrPol_dek_y_new[i] * dx))))

            qp.drawPolygon(arrPol_pi_new)

        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = mywindow()

    sys.exit(app.exec())
