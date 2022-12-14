from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint
from form import Ui_Form
import numpy as np
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
            self.transfer = False
            self.scaling = False
            self.reflection = False
            self.turn = False
            self.arrPol_pi.clear()
            self.arrPol_dek_x.clear()
            self.arrPol_dek_y.clear()
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
        pen_1 = QPen(Qt.black, 1)

        for i in range(len(self.arrPol_pi)):
            qp.setPen(pen)
            qp.drawPoint(self.arrPol_pi[i])
            qp.setPen(pen_1)
            qp.drawText(self.arrPol_pi[i].x(), self.arrPol_pi[i].y(), str(i))

        qp.setPen(pen)
        if len(self.arrPol_pi) != 0 and self.paint_pol:
            qp.drawPolygon(self.arrPol_pi)

        if self.dek:
            for i in range(len(self.arrPol_pi)):
                self.arrPol_dek_x.append((self.arrPol_pi[i].x() - x0_1) / dx)
                self.arrPol_dek_y.append((y0 - self.arrPol_pi[i].y()) / dx)

            self.ui.tableWidget.setColumnCount(len(self.arrPol_pi))
            for i in range(len(self.arrPol_pi)):
                self.ui.tableWidget.setItem(0, i, QTableWidgetItem(str(self.arrPol_dek_x[i])))
                self.ui.tableWidget.setItem(1, i, QTableWidgetItem(str(self.arrPol_dek_y[i])))

        if self.transfer:
            tr_dek = self.ui.doubleSpinBox.value()
            arrPol_dek_y_new = []

            for i in range(len(self.arrPol_dek_y)):
                arrPol_dek_y_new.append(self.arrPol_dek_y[i] + tr_dek)

            arrPol_pi_new = []

            self.ui.tableWidget_2.setColumnCount(len(self.arrPol_pi))
            for i in range(len(self.arrPol_pi)):
                self.ui.tableWidget_2.setItem(0, i, QTableWidgetItem(str(self.arrPol_dek_x[i])))
                self.ui.tableWidget_2.setItem(1, i, QTableWidgetItem(str(arrPol_dek_y_new[i])))

            for i in range(len(self.arrPol_dek_x)):
                arrPol_pi_new.append(QPoint(int(round((self.arrPol_dek_x[i] * dx + x0_2))),
                                            int(round(y0 - arrPol_dek_y_new[i] * dx))))

            qp.drawPolygon(arrPol_pi_new)

        if self.reflection:
            n_top = self.ui.spinBox_2.value()
            arr1 = []

            for i in range(len(self.arrPol_pi)):
                arr1.append([self.arrPol_dek_x[i], self.arrPol_dek_y[i], 1])

            mtrx_1 = [[1, 0, 0],
                      [0, 1, 0],
                      [(-1) * self.arrPol_dek_x[n_top], (-1) * self.arrPol_dek_y[n_top], 1]]

            mtrx_2 = [[-1, 0, 0],
                      [0, -1, 0],
                      [0, 0, 1]]

            mtrx_3 = [[1, 0, 0],
                      [0, 1, 0],
                      [self.arrPol_dek_x[n_top], self.arrPol_dek_y[n_top], 1]]

            for i in range(len(self.arrPol_pi)):
                arr1[i] = np.matmul(arr1[i], mtrx_1)
                arr1[i] = np.matmul(arr1[i], mtrx_2)
                arr1[i] = np.matmul(arr1[i], mtrx_3)

            self.ui.tableWidget_2.setColumnCount(len(self.arrPol_pi))
            for i in range(len(self.arrPol_pi)):
                self.ui.tableWidget_2.setItem(0, i, QTableWidgetItem(str(arr1[i][0])))
                self.ui.tableWidget_2.setItem(1, i, QTableWidgetItem(str(arr1[i][1])))

            arrPol_pi_new = []

            for i in range(len(self.arrPol_pi)):
                arrPol_pi_new.append(QPoint(int(round((arr1[i][0] * dx + x0_2))),
                                            int(round(y0 - arr1[i][1] * dx))))

            qp.drawPolygon(arrPol_pi_new)

        if self.turn:
            fi = self.ui.spinBox_3.value()
            arr1 = []

            for i in range(len(self.arrPol_pi)):
                arr1.append([self.arrPol_dek_x[i], self.arrPol_dek_y[i], 1])

            mtrx_2 = [[np.cos(fi * np.pi / 180), np.sin(fi * np.pi / 180), 0],
                      [(-1) * np.sin(fi * np.pi / 180), np.cos(fi * np.pi / 180), 0],
                      [0, 0, 1]]

            for i in range(len(self.arrPol_pi)):
                arr1[i] = np.matmul(arr1[i], mtrx_2)

            self.ui.tableWidget_2.setColumnCount(len(self.arrPol_pi))
            for i in range(len(self.arrPol_pi)):
                self.ui.tableWidget_2.setItem(0, i, QTableWidgetItem(str(arr1[i][0])))
                self.ui.tableWidget_2.setItem(1, i, QTableWidgetItem(str(arr1[i][1])))

            arrPol_pi_new = []

            for i in range(len(self.arrPol_pi)):
                arrPol_pi_new.append(QPoint(int(round((arr1[i][0] * dx + x0_2))),
                                            int(round(y0 - arr1[i][1] * dx))))

            qp.drawPolygon(arrPol_pi_new)

        if self.scaling:
            scale = self.ui.doubleSpinBox_2.value()
            n_top = self.ui.spinBox.value()

            x1 = self.arrPol_dek_x[n_top]
            y1 = self.arrPol_dek_y[n_top]
            x2 = self.arrPol_dek_x[n_top - 1]
            y2 = self.arrPol_dek_y[n_top - 1]

            l1 = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            l2 = np.sqrt((y1 - y2) ** 2)
            l3 = np.sqrt((x1 - x2) ** 2)

            sin_ = l2 / l1
            cos_ = l3 / l1

            arr1 = []

            for i in range(len(self.arrPol_pi)):
                arr1.append([self.arrPol_dek_x[i], self.arrPol_dek_y[i], 1])

            mtrx_1 = [[1, 0, 0],
                      [0, 1, 0],
                      [(-1) * x2, (-1) * y2, 1]]

            mtrx_2 = [[cos_, (-1) * sin_, 0],
                      [sin_, cos_, 0],
                      [0, 0, 1]]

            mtrx_3 = [[scale, 0, 0],
                      [0, scale, 0],
                      [0, 0, 1]]

            mtrx_4 = [[(-1) * cos_, sin_, 0],
                      [(-1) * sin_, (-1) * cos_, 0],
                      [0, 0, 1]]

            mtrx_5 = [[1, 0, 0],
                      [0, 1, 0],
                      [x2, y2, 1]]

            for i in range(len(self.arrPol_pi)):
                arr1[i] = np.matmul(arr1[i], mtrx_1)
                arr1[i] = np.matmul(arr1[i], mtrx_2)
                arr1[i] = np.matmul(arr1[i], mtrx_3)
                arr1[i] = np.matmul(arr1[i], mtrx_4)
                arr1[i] = np.matmul(arr1[i], mtrx_5)

            self.ui.tableWidget_2.setColumnCount(len(self.arrPol_pi))
            for i in range(len(self.arrPol_pi)):
                self.ui.tableWidget_2.setItem(0, i, QTableWidgetItem(str(arr1[i][0])))
                self.ui.tableWidget_2.setItem(1, i, QTableWidgetItem(str(arr1[i][1])))

            arrPol_pi_new = []

            for i in range(len(self.arrPol_pi)):
                arrPol_pi_new.append(QPoint(int(round((arr1[i][0] * dx + x0_2))),
                                            int(round(y0 - arr1[i][1] * dx))))

            qp.drawPolygon(arrPol_pi_new)




        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = mywindow()

    sys.exit(app.exec())
