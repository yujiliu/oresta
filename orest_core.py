from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys
import speech_recognition as sr
from PyQt5.QtWidgets import QMessageBox, QApplication
import orest_func
from datetime import datetime


class Orest_Main_Window(object):
    def __init__(self):
        self.request = None
        self.answer = None

    def setupUi(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(500, 500)
        main_window.setStyleSheet("background: transparent;\n""")
        main_window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        main_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("app_ico.ico"))
        main_window.setWindowIcon(icon)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")

        self.mode = QtWidgets.QLabel(self.central_widget)
        self.mode.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.mode.setMinimumSize(QtCore.QSize(500, 500))
        self.mode.setMaximumSize(QtCore.QSize(500, 500))
        self.mode.setObjectName("mode")
        self.mode.mousePressEvent = self.user_click
        image = QtGui.QPixmap("imgs/no_mode.png")
        self.mode.setPixmap(image)

        main_window.setCentralWidget(self.central_widget)

    def image_change_on_listening(self=0):
        image = QtGui.QPixmap("imgs/listening.png")
        self.mode.setPixmap(image)
        QApplication.instance().processEvents()

    def image_change_on_speaking(self=0):
        image = QtGui.QPixmap("imgs/speaking.png")
        self.mode.setPixmap(image)
        QApplication.instance().processEvents()

    def image_change_on_no_mode(self=0):
        image = QtGui.QPixmap("imgs/no_mode.png")
        self.mode.setPixmap(image)
        QApplication.instance().processEvents()

    def user_click(self, event):
        self.image_change_on_listening()
        self.request = self.voice_getter()

        self.image_change_on_speaking()
        orest_func.main(self.request)

        self.request = None
        self.image_change_on_no_mode()

    def voice_getter(self=0):
        r = sr.Recognizer("uk-UK")
        with sr.Microphone() as source:
            audio = r.listen(source)
            command = r.recognize(audio)
        try:
            if len(command) > 0:
                with open('TEMP/log.txt', 'a') as app_log:
                    app_log.write(f'{datetime.now().strftime("%H:%M:%S")} - USER: {command}\n')
                return command
            else:
                raise LookupError
        except LookupError:
            msg = QMessageBox()
            msg.setWindowTitle("Не чує баба")
            msg.setText("Я Вас не чую")
            msg.setInformativeText("Можливо у Вас проблеми з мікрофоном")
            msg.setIcon(QMessageBox.Question)
            msg.exec_()


with open('TEMP/log.txt', 'a') as app_log:
    app_log.write(f'SESSION STARTED'.center(50, "-") + "\n")
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = Orest_Main_Window()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())
