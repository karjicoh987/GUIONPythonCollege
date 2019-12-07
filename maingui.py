from PyQt5 import (QtWidgets, QtCore, QtGui)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from PyQt5.QtCore import QCoreApplication
import sys, time, smtplib, ssl, csv, requests, mimetypes, os



class auth(QtWidgets.QWidget):
    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self, parent)
        self.setStyleSheet("background:#FFFFFF;")
        #Центрирование окна
        self.desktop = QtWidgets.QApplication.desktop()
        self.setFixedSize(330, 160)
        x = (self.desktop.width() - self.width()) // 2
        y = (self.desktop.height() - self.height()) // 2
        self.move(x, y)
        self.setWindowTitle("Вход")

        #Виджеты аутификации
        self.grid = QtWidgets.QGridLayout()
        self.grid.setGeometry(QtCore.QRect(20, 20, 300, 90))

        self.text_login = QtWidgets.QLabel("Логин")
        self.text_login.setAlignment(QtCore.Qt.AlignHCenter)
        self.text_login.setStyleSheet("font-size:20px; color:#397594;")
        self.grid.addWidget(self.text_login, 0, 0)

        self.text_password = QtWidgets.QLabel("Пароль")
        self.text_password.setStyleSheet("font-size:20px; color:#397594;")
        self.text_password.setAlignment(QtCore.Qt.AlignHCenter)
        self.grid.addWidget(self.text_password, 1, 0)

        self.login = QtWidgets.QLineEdit()
        self.login.setStyleSheet(
            "color:#397594; font-size:20px;border:3px solid #849ECE;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)
        self.grid.addWidget(self.login, 0, 1, 1, 2)

        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setStyleSheet(
            "color:#397594; font-size:20px; border:3px solid #849ECE;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.grid.addWidget(self.password, 1, 1, 1, 2)

        self.submit = QtWidgets.QPushButton("Вход")
        self.submit.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            " border-radius: 4px;"
            "font-size:20px; "
            "padding:5px;"
            "border:2px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:3px ;border-style:solid; border-color:#839CC9;}"
        )
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy)
        self.submit.clicked.connect(self.auth_user)
        self.grid.addWidget(self.submit, 2, 1, 1, 1)

        self.exit = QtWidgets.QPushButton("Выход")
        self.exit.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            " border-radius: 4px;"
            "font-size:20px; "
            "padding:5px;"
            "border:2px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:3px ;border-style:solid; border-color:#839CC9;}"
        )
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.clicked.connect(QCoreApplication.instance().quit)
        self.grid.addWidget(self.exit, 2, 2, 1, 1)

        self.setLayout(self.grid)

    def auth_user(self):
        login = self.login.text()
        password = self.password.text()
        wind = myWindow()
        self.status = None

        f = open("inf/users.csv", "r")
        reader = csv.DictReader(f, delimiter=",")

        for i in reader:
            if login == i["Логин"]:

                if login == i["Логин"] and password == i["Пароль"]:
                    if login == "admin":
                        self.status = "admin"
                        self.close()
                        wind.resize(1000, 800)
                        wind.setWindowTitle("NtmtLern")
                        wind.setWindowIcon(QIcon("image/graduation.png"))
                        wind.show()
                        print("Админ")
                        # self.login.clear()
                        # self.password.clear()
                        self.close()
                        break
                    if login == "hristova-ju":
                        self.status = "teacher"
                        print("Учитель")
                        self.close()
                        wind.resize(1000, 800)
                        wind.setWindowTitle("NtmtLern")
                        wind.setWindowIcon(QIcon("image/graduation.png"))
                        wind.show()
                        # self.login.clear()
                        # self.password.clear()
                        self.close()
                        break
                    else:
                        self.status = "student"
                        print("Ученик")
                        self.close()
                        wind.resize(1000, 800)
                        wind.setWindowTitle("NtmtLern")
                        wind.setWindowIcon(QIcon("image/graduation.png"))
                        wind.show()
                        # self.login.clear()
                        # self.password.clear()
                        self.close()
                        break

        f.close()


class subWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        #Центрирование окна
        self.desktop = QtWidgets.QApplication.desktop()
        self.resize(1350,900 )
        x = (self.desktop.width() - self.width()) // 2
        y = (self.desktop.height() - self.height()) // 2
        self.move(x, y)
        self.setWindowTitle("Журнал")

        self.grid = QtWidgets.QGridLayout()

        #Открытие файла с данными
        data = open("inf/оценки.csv", "r")
        reader = csv.DictReader(data, delimiter=",")

        #Инициализация таблицы
        self.table_list = QtWidgets.QTableWidget()  #Создание таблицы
        self.table_list.setColumnCount(len(
            reader.fieldnames))
        self.table_list.setRowCount(10)
        self.table_list.setHorizontalHeaderLabels(
            reader.fieldnames)  #Установка заголовков таблицы
        item, line, column = 0, 0, 0
        self.table_list.horizontalHeaderItem(0).setTextAlignment(
            QtCore.Qt.AlignHCenter)
        for i in reader:
            column = 0
            for j in i:
                self.item = QtWidgets.QTableWidgetItem(i[j])
                self.item.setTextAlignment(QtCore.Qt.AlignVCenter
                                           | QtCore.Qt.AlignHCenter)
                self.table_list.setItem(line, column, self.item)
                self.item.setBackground(QtGui.QColor("#839CC9"))
                self.item.setFont(QtGui.QFont('Arial', 15))
                self.item.setForeground(QtGui.QColor("white"))
                column += 1
            line += 1

        # делаем ресайз колонок по содержимому
        self.table_list.resizeColumnsToContents()
        self.grid.addWidget(self.table_list)
        self.setLayout(self.grid)


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot(['0', '0', '0', '0', '0', '0', '0', '0', '0'])

    def plot(self, data):
        #data = [0, 1, 2, 3, 4, 5, 2, 3, 4]
        colors = ['blue', 'red', 'black', 'green']
        X = list(range(len(data)))
        Y = data
        ax = self.figure.add_subplot(111)
        ax.set_ylim([-0.5, 5.5])
        ax.set_xlim([0, 9])
        ax.plot(X, Y, linewidth=3, color='blue')
        ax.plot(
            X,
            Y,
            'o',
            color='gray',
            markersize=5,
            linewidth=1,
            markerfacecolor='red',
            markeredgecolor='gray',
            markeredgewidth=2)
        ax.grid(True)
        ax.set_xlabel("Номер задания курса")
        ax.set_ylabel("Оценка")
        ax.set_title('График изменения оценок студента')
        ax.legend(['Изменение', 'Контрольные точки'], loc='lower left')
        self.draw()

    def clear(self):
        #self.axes.figure.canvas.draw()
        self.axes.cla()


class myWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.path_file = []
        self.widget_name = []
        self.buf_widget = []
        self.local_buf = []

        QtWidgets.QWidget.__init__(self, parent)

        QtWidgets.QToolTip.setFont(QFont('Arial', 10))
        #-------------------------------------------
        #start ini layout

        self.horizont_menu = QtWidgets.QHBoxLayout()
        self.grid = QtWidgets.QGridLayout()
        self.vertical_menu_file = QtWidgets.QVBoxLayout()

        #end ini layout
        #--------------------------------------------

        #---------------------------------------------
        #start ini main menu

        self.button_mail = QtWidgets.QPushButton("Почта")
        self.button_mail.setToolTip('<b>Отправка электронных писем</b>')
        self.button_mail.setIcon(
            QtGui.QIcon("image/opened-email-envelope.png"))
        self.button_mail.setIconSize(QtCore.QSize(35, 35))
        self.button_mail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_users = QtWidgets.QPushButton("Пользователи")
        self.button_users.setToolTip(
            '<b>Просмотр информации о пользователе</b>')
        self.button_users.setIcon(QtGui.QIcon("image/users-group.png"))
        self.button_users.setIconSize(QtCore.QSize(35, 35))
        self.button_users.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_tasks = QtWidgets.QPushButton("Задания")
        self.button_tasks.setToolTip('<b>Просмотр и загрузка заданий</b>')
        self.button_tasks.setIcon(QtGui.QIcon("image/list.png"))
        self.button_tasks.setIconSize(QtCore.QSize(35, 35))
        self.button_tasks.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_list = QtWidgets.QPushButton("Журнал")
        self.button_list.setToolTip('<b>Просмотр журнала с оценками</b>')
        self.button_list.setIcon(QtGui.QIcon("image/spreadsheet-cell.png"))
        self.button_list.setIconSize(QtCore.QSize(35, 35))
        self.button_list.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_exit = QtWidgets.QPushButton()
        self.button_exit.setIcon(QtGui.QIcon("image/logout.png"))
        self.button_exit.setIconSize(QtCore.QSize(35, 35))
        self.button_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        #end ini main menu
        #----------------------------------------------

        #------------------------------------------------
        #start mailBlockIni

        self.emailLabel = QtWidgets.QLabel("Введите email")
        self.emailLabel.setAlignment(QtCore.Qt.AlignHCenter)

        self.titleLabel = QtWidgets.QLabel("Заголовок письма")
        self.titleLabel.setAlignment(QtCore.Qt.AlignHCenter)

        self.messageLabel = QtWidgets.QLabel("Сообщение")
        self.messageLabel.setAlignment(QtCore.Qt.AlignHCenter)

        self.emailAddress = QtWidgets.QLineEdit()
        self.emailAddress.setPlaceholderText("Введите адрес эл.почты")
        self.emailTitle = QtWidgets.QLineEdit()
        self.emailTitle.setPlaceholderText("Введите заголовок письма")
        self.emailMessage = QtWidgets.QTextEdit()
        self.emailMessage.setPlaceholderText("Введите текст сообщения")

        self.submit_button = QtWidgets.QPushButton("Отправить сообщение")
        self.submit_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_button.setIcon(QtGui.QIcon("image/paper-plane.png"))
        self.submit_button.setIconSize(QtCore.QSize(50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHeightForWidth(
            self.submit_button.sizePolicy().hasHeightForWidth())
        self.submit_button.setSizePolicy(sizePolicy)

        self.add_file_button = QtWidgets.QPushButton()
        self.add_file_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_file_button.setIcon(QtGui.QIcon("image/clip.png"))
        self.add_file_button.setIconSize(QtCore.QSize(50, 50))

        self.label_list_file = QtWidgets.QLabel()
        self.label_list_file.setAlignment(QtCore.Qt.AlignHCenter)

        #end mailBlockIni
        #--------------------------------------------------

        #-----------------------------------------------------
        #start user block

        self.NameUser = QtWidgets.QLabel("Имя")
        self.NameUser.setAlignment(QtCore.Qt.AlignCenter)
        self.LastNameUser = QtWidgets.QLabel("Фамилия")
        self.LastNameUser.setAlignment(QtCore.Qt.AlignCenter)
        self.emailUser = QtWidgets.QLabel("Электронная почта")
        self.emailUser.setAlignment(QtCore.Qt.AlignCenter)
        self.percentPerfomenceUser = QtWidgets.QLabel("Процент выполнения")
        self.percentPerfomenceUser.setAlignment(QtCore.Qt.AlignCenter)
        self.averagePointUser = QtWidgets.QLabel("Средний балл")
        self.averagePointUser.setAlignment(QtCore.Qt.AlignCenter)
        self.combobox_user = QtWidgets.QComboBox()
        self.combobox_user.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        f = open("inf/users.csv", "r")
        a = csv.DictReader(f, delimiter=',')
        #i = 0
        self.combobox_user.addItem('Выберите пользователя')
        for col in a:
            self.combobox_user.addItem(col["Имя"] + " " + col["Фамилия"])

        #end user block
        #--------------------------------------------------------

        #---------------------------------------------------------
        #start download task block
        self.labelMsWord = QtWidgets.QLabel("MSWord")
        self.labelExcel = QtWidgets.QLabel("MSExcel")
        self.labelAcess = QtWidgets.QLabel("MSAcess")
        self.info = QtWidgets.QLabel("Выберите раздел")
        self.info.setAlignment(QtCore.Qt.AlignCenter)

        self.combobox_download = QtWidgets.QComboBox()
        self.combobox_download.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.combobox_download.addItem("MSWord")
        self.combobox_download.addItem("MSExcel")
        self.combobox_download.addItem("MSAcess")
        self.combobox_download.addItem("MSPowerPoint")

        self.button_task_word_1 = QtWidgets.QPushButton(
            "Пр.работа 2 Оформление деловых документов.pdf")
        self.button_task_word_1.setIcon(QtGui.QIcon("image/pdf.png"))
        self.button_task_word_1.setIconSize(QtCore.QSize(50, 50))
        self.button_task_word_1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_task_word_2 = QtWidgets.QPushButton(
            "Практическая работа № 1 - объекты в Ворде.pdf")
        self.button_task_word_2.setIcon(QtGui.QIcon("image/pdf.png"))
        self.button_task_word_2.setIconSize(QtCore.QSize(50, 50))
        self.button_task_word_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_task_word_3 = QtWidgets.QPushButton(
            "ЦифроваяПодписьДокументаOffice.docx")
        self.button_task_word_3.setIcon(QtGui.QIcon("image/word.png"))
        self.button_task_word_3.setIconSize(QtCore.QSize(50, 50))
        self.button_task_word_3.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_task_word_4 = QtWidgets.QPushButton(
            "КонтрольнаяРабота1.zip")
        self.button_task_word_4.setIcon(QtGui.QIcon("image/zip.png"))
        self.button_task_word_4.setIconSize(QtCore.QSize(50, 50))
        self.button_task_word_4.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_task_excel_1 = QtWidgets.QPushButton(
            "КонтрольнаяРабота.pdf")
        self.button_task_excel_1.setIcon(QtGui.QIcon("image/pdf.png"))
        self.button_task_excel_1.setIconSize(QtCore.QSize(50, 50))
        self.button_task_excel_1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_task_excel_2 = QtWidgets.QPushButton("Поверхности.xls")
        self.button_task_excel_2.setIcon(QtGui.QIcon("image/excel.png"))
        self.button_task_excel_2.setIconSize(QtCore.QSize(50, 50))
        self.button_task_excel_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_task_excel_3 = QtWidgets.QPushButton(
            "ПрактическаяРабота3СоритировкаФильтрация.xls")
        self.button_task_excel_3.setIcon(QtGui.QIcon("image/excel.png"))
        self.button_task_excel_3.setIconSize(QtCore.QSize(50, 50))
        self.button_task_excel_3.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_task_excel_4 = QtWidgets.QPushButton(
            "Практическое задание - функция Если.docx")
        self.button_task_excel_4.setIcon(QtGui.QIcon("image/word.png"))
        self.button_task_excel_4.setIconSize(QtCore.QSize(50, 50))
        self.button_task_excel_4.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_task_acess_1 = QtWidgets.QPushButton(
            "Контрольная работа№ 3.pdf")
        self.button_task_acess_1.setIcon(QtGui.QIcon("image/pdf.png"))
        self.button_task_acess_1.setIconSize(QtCore.QSize(50, 50))
        self.button_task_acess_1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_zip_acess = QtWidgets.QPushButton(
            "ТеоретическийМатериалПоMSAccess.rar")
        self.button_zip_acess.setIcon(QtGui.QIcon("image/zip.png"))
        self.button_zip_acess.setIconSize(QtCore.QSize(50, 50))
        self.button_zip_acess.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.power_point_task = QtWidgets.QPushButton(
            "ПрактическаяСозданиеПрезентации.docx")
        self.power_point_task.setIcon(QtGui.QIcon("image/word.png"))
        self.power_point_task.setIconSize(QtCore.QSize(50, 50))
        self.power_point_task.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.power_point_zip = QtWidgets.QPushButton(
            "СоветыПоОформлениюПрезентации.docx")
        self.power_point_zip.setIcon(QtGui.QIcon("image/word.png"))
        self.power_point_zip.setIconSize(QtCore.QSize(50, 50))
        self.power_point_zip.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #---------------------------------------------------
        #start style
        self.setStyleSheet("myWindow{"
                           "background:	white;}"
                           "QLabel{"
                           "font-size:15px;"
                           "font-family:Arial;"
                           "color:#387791;}"
                           "QLineEdit{"
                           "background:white;"
                           "font-size:14px;"
                           "font-family:Arial;"
                           "border:2px solid;"
                           "border-radius:5px;"
                           "border-color:#839CC9;"
                           "padding-left:15px;"
                           "margin:2px;}")
        self.add_file_button.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "font-family:Arial Black;"
            " border-radius: 4px;"
            "font-size:25px; "
            "padding:25px;"
            "margin-left:100px;}")

        self.button_task_excel_4.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "margin:5px;"
            "align-text:left;"
            "font-family:Arial Black;"
            "width:500px;"
            "height:25px;"
            " border-radius: 4px;"
            "font-size:15px; "
            "padding:25px 0px 25px 0px;"
            "border:2px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}"
        )
        self.button_task_excel_3.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "margin:5px;"
            "align-text:left;"
            "font-family:Arial Black;"
            "width:500px;"
            "height:25px;"
            " border-radius: 4px;"
            "font-size:15px; "
            "padding:25px 0px 25px 0px;"
            "border:2px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}"
        )
        self.button_task_excel_2.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "margin:5px;"
            "align-text:left;"
            "font-family:Arial Black;"
            "width:500px;"
            "height:25px;"
            " border-radius: 4px;"
            "font-size:15px; "
            "padding:25px 0px 25px 0px;"
            "border:2px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}"
        )
        self.button_task_excel_1.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "margin:5px;"
            "align-text:left;"
            "font-family:Arial Black;"
            "width:500px;"
            "height:25px;"
            " border-radius: 4px;"
            "font-size:15px; "
            "padding:25px 0px 25px 0px;"
            "border:2px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}"
        )
        self.button_task_acess_1.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "margin:5px;"
            "align-text:left;"
            "font-family:Arial Black;"
            "width:500px;"
            "height:25px;"
            " border-radius: 4px;"
            "font-size:15px; "
            "padding:25px 0px 25px 0px;"
            "border:2px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}"
        )
        self.button_zip_acess.setStyleSheet("QPushButton {background-color:white;"
            " color: #839CC9;"
            "margin:5px;"
            "font-family:Arial Black;"
            "width:500px;"
            "height:25px;"
            " border-radius: 4px;"
            "font-size:15px; "
            "padding:25px 40px 25px 0px;"
            "border:2px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}")

        self.power_point_task.setStyleSheet("QPushButton {background-color:white;"
            " color: #839CC9;"
            "margin:5px;"
            "font-family:Arial Black;"
            "width:500px;"
            "height:25px;"
            " border-radius: 4px;"
            "font-size:15px; "
            "padding:25px 40px 25px 0px;"
            "border:2px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}")

        self.power_point_zip.setStyleSheet("QPushButton {background-color:white;"
            " color: #839CC9;"
            "margin:5px;"
            "font-family:Arial Black;"
            "width:500px;"
            "height:25px;"
            " border-radius: 4px;"
            "font-size:15px; "
            "padding:25px 40px 25px 0px;"
            "border:2px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}")

        self.button_task_word_1.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "margin:5px;"
            "align-text:left;"
            "font-family:Arial Black;"
            "width:500px;"
            "height:25px;"
            " border-radius: 4px;"
            "font-size:15px; "
            "padding:25px 0px 25px 0px;"
            "border:2px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}"
        )
        self.button_task_word_2.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "margin:5px;"
            "font-family:Arial Black;"
            "align-text:left;"
            "width:500px;"
            "height:18px;"
            " border-radius: 4px;"
            "font-size:15px; "
            "padding:25px 10px 25px 0px;"
            "border:2px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}"
        )
        self.button_task_word_3.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "margin:5px;"
            "font-family:Arial Black;"
            "width:500px;"
            "height:25px;"
            " border-radius: 4px;"
            "font-size:15px; "
            "padding:25px 40px 25px 0px;"
            "border:2px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}"
        )
        self.button_task_word_4.setStyleSheet("QPushButton {background-color:white;"
            " color: #839CC9;"
            "margin:5px;"
            "font-family:Arial Black;"
            "width:500px;"
            "height:25px;"
            " border-radius: 4px;"
            "font-size:15px; "
            "padding:25px 40px 25px 0px;"
            "border:2px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}")

        self.submit_button.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "font-family:Arial Black;"
            " border-radius: 4px;"
            "font-size:25px; "
            "padding:25px;"
            "border:4px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}"
        )

        self.emailMessage.setStyleSheet("background:white;"
                                        "font-size:14px;"
                                        "font-family:Arial;"
                                        "border: 2px solid #839CC9;"
                                        "border-radius:5px;"
                                        "padding-left:15px;"
                                        "margin:2px;")
        self.button_mail.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "font-family:Arial Black;"
            " border-radius: 4px;"
            "font-size:25px; "
            "padding:25px;"
            "border:4px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}"
        )
        self.button_users.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "font-family:Arial Black;"
            " border-radius: 4px;"
            "font-size:25px; "
            "padding:25px;"
            "border:4px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}"
        )

        self.button_tasks.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "font-family:Arial Black;"
            " border-radius: 4px;"
            "font-size:25px; "
            "padding:25px;"
            "border:4px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}"
        )

        self.button_list.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "font-family:Arial Black;"
            " border-radius: 4px;"
            "font-size:25px; "
            "padding:25px;"
            "border:4px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}"
        )

        self.NameUser.setStyleSheet("QLabel{font-size:25px;"
                                    "background-color:white;"
                                    "border:3px;"
                                    "border-style:solid;"
                                    "border-color:#839CC9;"
                                    "margin:5px;}")
        self.emailUser.setStyleSheet("QLabel{font-size:25px;"
                                     "background-color:white;"
                                     "border:3px;"
                                     "border-style:solid;"
                                     "border-color:#839CC9;"
                                     "margin:5px;}")
        self.button_exit.setStyleSheet(
            "QPushButton {background-color:white;"
            " color: #839CC9;"
            "font-family:Arial Black;"
            " border-radius: 4px;"
            "font-size:25px; "
            "padding:25px;"
            "border:4px;"
            "border-color:#839CC9;"
            "border-style:solid;}"
            "QPushButton:hover{background:#E2F9FF;}"
            "QPushButton:pressed {background-color:#E2F9FF ; border:7px ;border-style:solid; border-color:#839CC9;}"
        )

        self.percentPerfomenceUser.setStyleSheet("QLabel{font-size:25px;"
                                                 "background-color:white;"
                                                 "border:3px;"
                                                 "border-style:solid;"
                                                 "border-color:#839CC9;"
                                                 "margin:5px;}")
        self.averagePointUser.setStyleSheet("QLabel{font-size:25px;"
                                            "background-color:white;"
                                            "border:3px;"
                                            "border-style:solid;"
                                            "border-color:#839CC9;"
                                            "margin:5px;}")
        self.LastNameUser.setStyleSheet("QLabel{font-size:25px;"
                                        "background-color:white;"
                                        "border:3px;"
                                        "border-style:solid;"
                                        "border-color:#839CC9;"
                                        "margin:5px;}")
        self.combobox_user.setStyleSheet("QComboBox{"
                                         "font-size:15px;"
                                         "margin:5px;"
                                         "background:white;"
                                         "padding:5px;"
                                         "border:3px solid #839CC9;}")
        self.combobox_download.setStyleSheet("QComboBox{"
                                             "font-size:15px;"
                                             "margin:3px;"
                                             "background:white;"
                                             "padding:5px;"
                                             "border:3px solid #839CC9;}")
        self.info.setStyleSheet("QLabel{" "font-size:25px;}")
        #end style
        #---------------------------------------------------------------

        #---------------------------------------------------------------
        #start layout block

        self.horizont_menu.addWidget(self.button_users)
        self.horizont_menu.addWidget(self.button_list)
        self.horizont_menu.addWidget(self.button_tasks)
        self.horizont_menu.addWidget(self.button_mail)
        self.horizont_menu.addWidget(self.button_exit)
        #self.horizont_menu.addWidget(self.button_stat)

        self.grid.setSpacing(3)
        self.grid.addLayout(self.horizont_menu, 0, 0, 1, 3)

        self.grid.addWidget(self.titleLabel, 1, 0)
        self.grid.addWidget(self.emailTitle, 1, 1)
        self.grid.addWidget(self.emailAddress, 2, 1)
        self.grid.addWidget(self.emailLabel, 2, 0)
        self.grid.addWidget(self.emailMessage, 3, 1, 4, 1)
        self.grid.addWidget(self.messageLabel, 3, 0)
        self.grid.addWidget(self.add_file_button, 7, 1, 1, 1)
        self.grid.addWidget(self.submit_button, 7, 1, 1, 1)
        self.grid.addWidget(self.label_list_file, 8, 1, 1, 1)

        self.grid.addWidget(self.combobox_user, 1, 1)
        self.grid.addWidget(self.NameUser, 2, 0)
        self.grid.addWidget(self.LastNameUser, 2, 1)
        self.grid.addWidget(self.emailUser, 2, 2)
        self.grid.addWidget(self.averagePointUser, 3, 1)
        self.grid.addWidget(self.percentPerfomenceUser, 3, 0)

        self.grid.addWidget(self.combobox_download, 1, 1)
        self.grid.addWidget(self.button_task_word_1, 2, 1)
        self.grid.addWidget(self.button_task_word_2, 3, 1)
        self.grid.addWidget(self.button_task_word_3, 4, 1)
        self.grid.addWidget(self.button_task_word_4, 5, 1)  #1

        self.grid.addWidget(self.button_task_excel_1, 2, 1)
        self.grid.addWidget(self.button_task_excel_2, 3, 1)
        self.grid.addWidget(self.button_task_excel_3, 4, 1)
        self.grid.addWidget(self.button_task_excel_4, 5, 1)

        self.grid.addWidget(self.button_task_acess_1, 2, 1)
        self.grid.addWidget(self.button_zip_acess, 3, 1)

        self.grid.addWidget(self.power_point_task, 2, 1)
        self.grid.addWidget(self.power_point_zip, 3, 1)

        self.plot = PlotCanvas(self, width=5, height=4)
        self.grid.addWidget(self.plot, 4, 0, 5, 3)

        # self.grid.addWidget(self.button_exit, 3, 2)

        self.setLayout(self.grid)
        #end layout block
        #-----------------------------------------------------------------

        #-------------------------------------------------
        #Event block start
        self.button_mail.clicked.connect(self.mail_shower)
        self.submit_button.clicked.connect(self.send_mail)
        self.add_file_button.clicked.connect(self.showDialog)
        self.button_users.clicked.connect(self.user_shower)
        self.combobox_user.activated[str].connect(self.onActivated)
        self.button_tasks.clicked.connect(self.file_shower)
        self.combobox_download.activated[str].connect(self.onActivated_1)
        self.button_task_excel_1.clicked.connect(
            lambda: self.download_file("http://karjicoh98.beget.tech/files/exel/КонтрольнаяРабота.pdf")
        )
        self.button_task_excel_2.clicked.connect(
            lambda: self.download_file("http://karjicoh98.beget.tech/files/exel/Поверхности.xls")
        )
        self.button_task_excel_3.clicked.connect(
            lambda: self.download_file("http://karjicoh98.beget.tech/files/exel/ПрактическаяРабота3СортировкаФильтрация.xls")
        )
        self.button_task_excel_4.clicked.connect(
            lambda: self.download_file("http://karjicoh98.beget.tech/files/exel/ПрактическоеЗаданиеФункцияЕсли.docx")
        )
        self.button_task_word_1.clicked.connect(
            lambda: self.download_file("http://karjicoh98.beget.tech/files/MSWord/ПрРабота2Оформлениеделовыхдокументов.pdf")
        )
        self.button_task_word_2.clicked.connect(
            lambda: self.download_file("http://karjicoh98.beget.tech/files/MSWord/ПрактическаяРабота№1объектыВВорде.pdf")
        )
        self.button_task_word_3.clicked.connect(
            lambda: self.download_file("http://karjicoh98.beget.tech/files/MSWord/ЦифроваяПодписьВдокументеOffice.doc")
        )
        self.button_task_word_4.clicked.connect(
            lambda: self.download_file("http://karjicoh98.beget.tech/files/MSWord/КонтрольнаяРабота№1.zip")
        )
        self.button_task_acess_1.clicked.connect(
            lambda: self.download_file("http://karjicoh98.beget.tech/files/acess/КонтрольнаяРабота№3.pdf")
        )
        self.button_zip_acess.clicked.connect(
            lambda: self.download_file("http://karjicoh98.beget.tech/files/acess/ТеоретическийМатериалПоMSAccess.zip")
        )
        self.power_point_zip.clicked.connect(
            lambda: self.download_file("http://karjicoh98.beget.tech/files/powerpoint/СоветыПоОформлениюПрезентации.docx")
        )
        self.power_point_task.clicked.connect(
            lambda: self.download_file("http://karjicoh98.beget.tech/files/acess/ПрактическаяСозданиеПрезентации.docx")
        )
        self.button_list.clicked.connect(self.showWindow)
        self.button_exit.clicked.connect(self.exit_window)
        # Event block end
        #-------------------------------------------------
        self.main_grid()

    def exit_window(self):
        self.close()
        auth.show()

    def showWindow(self):
        self.subwindow = subWindow()
        self.subwindow.show()

    def main_grid(self):

        for i in range(self.grid.count()):

            item = self.grid.itemAt(i)
            widget = item.widget()

            if widget is not None:
                self.widget_name.append(widget)
                widget.hide()


    #-----------------------------------------------------------
    #start block user

    def user_shower(self):
        if self.buf_widget != []:
            for i in self.buf_widget:
                i.hide()
            self.buf_widget.clear()

        f = open("inf/users.csv", "r")
        print("Логин пользователя", auth.login.text())
        if auth.status == "student":

            for i in range(10, 15):
                self.buf_widget.append(self.widget_name[i])
                self.widget_name[i].show()

            for col in csv.DictReader(f, delimiter=','):

                if col["Фамилия"].lower() in auth.login.text():
                    print(col)
                    print(col["Электронная почта"])
                    self.emailUser.setText(
                        "Электронная почта" + "\n" + col["Электронная почта"])
                    self.LastNameUser.setText(
                        "Фамилия" + "\n" + col["Фамилия"])
                    self.NameUser.setText("Имя" + "\n" + col["Имя"])
                    self.percentPerfomenceUser.setText(
                        "Процент выполнения" + "\n" + "56")
                    self.averagePointUser.setText(
                        "Средний балл" + "\n" + "4.54")
                    f_1 = open("inf/оценки.csv", "r")
                    for i in csv.reader(f_1):
                        if i[1].lower() in auth.login.text():
                            data = [int(item) for item in i[2:]]
                            self.widget_name[28].clear()
                            self.widget_name[28].plot(data)
        else:
            for i in range(9, 15):
                self.buf_widget.append(self.widget_name[i])
                self.widget_name[i].show()
        self.widget_name[28].show()

    def onActivated(self, text):
        f = open("inf/users.csv", "r")
        F_1 = open("inf/avg.csv","r")
        a = csv.DictReader(f, delimiter=',')

        if auth.status != "student":
            for col in a:
                if (text in (col["Имя"] + " " + col["Фамилия"])):

                    self.emailUser.setText(
                        "Электронная почта" + "\n" + col["Электронная почта"])
                    self.LastNameUser.setText(
                        "Фамилия" + "\n" + col["Фамилия"])
                    self.NameUser.setText("Имя" + "\n" + col["Имя"])
                    self.percentPerfomenceUser.setText(
                        "Процент выполнения" + "\n" + "100")

                    for i in csv.DictReader(F_1,delimiter=','):
                        print(text)
                        if text in (i["Имя"] + " " + i["Фамилия"]):
                            print(i)
                            self.averagePointUser.setText("Средний балл" + "\n" + i["Средний балл"])

                            F_1.close()
                            break

                    f_1 = open("inf/оценки.csv", "r")

                    for i in csv.reader(f_1):
                        if i[0] + ' ' + i[1] == col["Имя"] + " " + col["Фамилия"]:
                            data = [int(item) for item in i[2:]]
                            self.widget_name[28].clear()
                            self.widget_name[28].plot(data)

                    f_1.close()

    #end block user
    #----------------------------------------------------------------------

    #-----------------------------------------------------------------------
    #start block functions for send email
    def showDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                      '/home')
        self.path_file.append(fname[0])
        print(fname[0])

    def mail_shower(self):
        if self.buf_widget != []:
            for i in self.buf_widget:
                i.hide()
            self.buf_widget.clear()

        for i in range(9):
            self.buf_widget.append(self.widget_name[i])
            self.widget_name[i].show()

        if auth.status == "student":
            self.emailAddress.setEnabled(False)
            self.emailAddress.setText("lick08@mail.ru")

        self.widget_name[28].hide()

    def send_mail(self):

        sender_email = "mtest8893@gmail.com"
        password = "316853bl98d3"

        subject = self.emailTitle.text()
        receiver_email = self.emailAddress.text()

        message = MIMEMultipart()

        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email
        text_message = self.emailMessage.toPlainText()
        message.attach(MIMEText(text_message, "plain"))
        if self.path_file != []:
            for i in self.path_file:
                filepath = i
                filename = os.path.basename(filepath)

                ctype, encoding = mimetypes.guess_type(
                    filepath)  # Определяем тип файла на основе его расширения
                maintype, subtype = ctype.split('/', 1)

                with open(filepath, 'rb') as fp:
                    file = MIMEBase(maintype, subtype)
                    file.set_payload(fp.read())
                    fp.close()
                encoders.encode_base64(file)
                file.add_header(
                    'Content-Disposition', 'attachment', filename=filename)
                message.attach(file)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
                "smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        if self.path_file:
            self.path_file.clear()
        self.emailMessage.setText("")
        self.emailTitle.setText("")
        self.emailAddress.setText("")
    #end block email
    #-------------------------------------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------------------------------------
    #start download file block
    def onActivated_1(self, text):

        self.buf_widget.clear()
        if text == "MSWord":
            if self.local_buf != []:
                for i in self.local_buf:
                    i.hide()
                self.local_buf.clear()

            for i in range(16, 20):
                self.widget_name[i].show()
                self.local_buf.append(self.widget_name[i])

        elif text == "MSExcel":
            if self.local_buf != []:

                for i in self.local_buf:
                    i.hide()
                self.local_buf.clear()

            for i in range(20, 24):

                self.widget_name[i].show()
                self.local_buf.append(self.widget_name[i])

        elif text == "MSAcess":
            if self.local_buf != []:
                for i in self.local_buf:
                    i.hide()
                self.local_buf.clear()
            for i in range(24, 26):
                self.widget_name[i].show()
                self.local_buf.append(self.widget_name[i])

        elif text == "MSPowerPoint":
            if self.local_buf != []:
                for i in self.local_buf:
                    i.hide()
                self.local_buf.clear()
            for i in range(26, 28):
                self.widget_name[i].show()
                self.local_buf.append(self.widget_name[i])

        self.buf_widget.append(self.widget_name[15])
        self.buf_widget.extend(self.local_buf)

    def file_shower(self):
        if self.buf_widget != []:
            for i in self.buf_widget:
                i.hide()
            self.buf_widget.clear()

        self.buf_widget.append(self.widget_name[15])
        self.widget_name[15].show()
        self.widget_name[28].hide()



    def download_file(self, url):

        file_name = url.split("/")[-1]
        expa = file_name.split(".")[-1]
        f = open("Задания/" + file_name + "." + expa,
                 "wb")  # открываем файл для записи, в режиме wb
        ufr = requests.get(url)  # делаем запрос
        f.write(ufr.content
                )  # записываем содержимое в файл; как видите - content запроса
        f.close()

    #end download file block
    #-------------------------------------------------------------------------------------------------------------------

    #---------------------------------------------------------------
    #start block function delay
    def load_data(self, sp):
        time.sleep(2)
        QtWidgets.qApp.processEvents()

    #end block function delay
    #---------------------------------------------------------------


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("image/graduation.png"))
    splash.show()
    QtWidgets.qApp.processEvents()
    window = myWindow()
    window.load_data(splash)
    splash.finish(window)
    auth = auth()
    auth.setWindowIcon(QIcon("image/user.png"))
    auth.setWindowTitle("Авторизация")
    auth.show()
    sys.exit(app.exec_())
