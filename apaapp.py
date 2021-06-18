import sys
from PySide2.QtCore import QEvent, Qt
from PySide2.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        menu_widget = QListWidget()
        for i in range(10):
            barang = QListWidgetItem(f"barang {i}")
            barang.setTextAlignment(Qt.AlignCenter)
            menu_widget.addItem(barang)

        teksnya_widget = QLabel("seks")
        teksnya_widget.setAlignment(Qt.AlignCenter)
        tombol = QPushButton("sesuatu")

        content_layout = QVBoxLayout()
        content_layout.addWidget(teksnya_widget)
        content_layout.addWidget(tombol)
        utama_widget = QWidget()
        utama_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(utama_widget, 4)
        self.setLayout(layout)

        self.setWindowTitle("judul")

        self.resize(800, 300)

    def keyPressEvent(self, event):
        print(event)
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Widget()
    w.show()

    with open("gaya.qss", "r") as f:
        gaya = f.read()
        app.setStyleSheet(gaya)

    sys.exit(app.exec_())