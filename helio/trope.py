import sys
from PySide2 import QtGui
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QIcon, QKeyEvent
from PySide2.QtWidgets import QApplication, QMainWindow

GLOBAL_STATE = 0


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Heliotrope")
        self.setWindowIcon(QIcon("helio/saebasol.icon.png"))
        start_size = QSize(800, 600)
        self.resize(start_size)
        self.setMinimumSize(start_size)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.show()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()


class UIFunctions(MainWindow):
    a = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont("fonts/segoeui.ttf")
    QtGui.QFontDatabase.addApplicationFont("fonts/segoeuib.ttf")
    window = MainWindow()
    with open("helio/gaya.qss", "r") as f:
        gaya = f.read()
        app.setStyleSheet(gaya)
    sys.exit(app.exec_())
# fckwup