import sys

from PySide6.QtWidgets import QApplication
from mainwidget import MainWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWidget()
    widget.show()

    sys.exit(app.exec_())
