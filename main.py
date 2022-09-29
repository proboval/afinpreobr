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
        self.arrPol_pi = []
        self.arrPol_dek_x = []
        self.arrPol_dek_y = []
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.buttonClicked())
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
        else:
            self.ui.pushButton.setText("Начать отрисовку Фигуры")
            self.start_paint = False
            self.paint_pol = True
            self.dek = True
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

            for i in range(len(self.arrPol_dek_x)):
                col_count = self.ui.tableWidget.columnCount()
                col_count += 1
                self.ui.tableWidget.setColumnCount(col_count)
                self.ui.tableWidget.setItem(0, i, QTableWidgetItem(str(self.arrPol_dek_x[i])))
                self.ui.tableWidget.setItem(1, i, QTableWidgetItem(str(self.arrPol_dek_y[i])))

        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = mywindow()

    sys.exit(app.exec())