import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("eeehwe")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())