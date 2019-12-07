from PyQt5 import (QtWidgets, QtCore)
import sys

class subWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.grid = QtWidgets.QGridLayout()
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(8)
        self.table.setRowCount(10)
        self.table.setHorizontalHeaderLabels(["1","1","1","1","1","1","1","1",])

        line = 0
        for i in range(11):
            column = 0
            for j in range(8):
                print(j)
                self.item = QtWidgets.QTableWidgetItem(str(j))
                self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.table.setItem(line, column, self.item)

                column += 1
            line += 1
        self.table.resizeColumnsToContents()
        self.grid.addWidget(self.table)
        self.setLayout(self.grid)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = subWindow()
    window.resize(1000, 800)
    window.show()
    sys.exit(app.exec_())