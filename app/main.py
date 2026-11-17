import sys

from PySide6.QtWidgets import QApplication

from app.core.config import APP_NAME, APP_ORGANIZATION
from app.ui.main_window import MainWindow


def main():

    app = QApplication(sys.argv)

    app.setApplicationName(APP_NAME)
    app.setOrganizationName(APP_ORGANIZATION)

    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
