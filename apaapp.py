import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.edit = QLineEdit("nama")
        self.tombol = QPushButton("tombol")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.tombol)

        self.setLayout(layout)

        self.tombol.clicked.connect(self.halo)

    def halo(self):
        print(f"Halo {self.edit.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())