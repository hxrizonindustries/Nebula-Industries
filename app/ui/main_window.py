
import sys
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedWidget,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QPainter,
    QLinearGradient,
    QColor,
    QPixmap,
)

from app.core import theme
from app.ui.navigation import Navigation
from app.ui.components.header import Header


class DesignCanvas(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.scale_factor = 1.0
        self.offset_x = 0
        self.offset_y = 0

        # NAVIGATION
        self.navigation = Navigation(self)

        # HEADER
        self.header = Header(self)

        # MAIN CONTENT AREA
        self.content_area = QStackedWidget(self)

        self.content_area.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground,
            True
        )

        self.content_area.setStyleSheet("""
            QStackedWidget {
                background: transparent;
                border: none;
            }
        """)

        # DECORATIVE SYMBOL
        symbol_path = (
            Path(__file__).resolve().parents[1]
            / "assets"
            / "images"
            / "nbi_symbol.png"
        )

        self.symbol = QPixmap(str(symbol_path))

        self.setMinimumSize(900, 506)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        design_width = theme.DESIGN_WIDTH
        design_height = theme.DESIGN_HEIGHT

        # PROPORTIONAL SCALING
        self.scale_factor = min(
            self.width() / design_width,
            self.height() / design_height
        )

        scaled_width = design_width * self.scale_factor
        scaled_height = design_height * self.scale_factor

        self.offset_x = (
            self.width() - scaled_width
        ) / 2

        self.offset_y = (
            self.height() - scaled_height
        ) / 2

        # MAIN CONTENT AREA
        self.content_area.setGeometry(
            round(
                self.offset_x
                + theme.CONTENT_X * self.scale_factor
            ),
            round(
                self.offset_y
                + theme.CONTENT_Y * self.scale_factor
            ),
            round(
                theme.CONTENT_WIDTH * self.scale_factor
            ),
            round(
                theme.CONTENT_HEIGHT * self.scale_factor
            )
        )

        # SIDEBAR
        self.navigation.set_scale(self.scale_factor)

        self.navigation.move(
            round(
                self.offset_x
                + theme.SIDEBAR_X * self.scale_factor
            ),
            round(
                self.offset_y
                + theme.SIDEBAR_Y * self.scale_factor
            )
        )

        # HEADER
        self.header.set_scale(self.scale_factor)

        self.header.move(
            round(self.offset_x),
            round(self.offset_y)
        )

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        # BACKGROUND GRADIENT
        gradient = QLinearGradient(
            0, 0,
            self.width(), self.height()
        )

        gradient.setColorAt(
            0.0,
            QColor(theme.GRADIENT_START)
        )

        gradient.setColorAt(
            1.0,
            QColor(theme.GRADIENT_END)
        )

        painter.fillRect(
            self.rect(),
            gradient
        )

        # DESIGN COORDINATE SYSTEM
        painter.save()

        painter.translate(
            self.offset_x,
            self.offset_y
        )

        painter.scale(
            self.scale_factor,
            self.scale_factor
        )

        # DECORATIVE NBI SYMBOL
        if not self.symbol.isNull():

            painter.setOpacity(0.05)

            painter.drawPixmap(
                1261,
                255,
                1522,
                1518,
                self.symbol
            )

        painter.restore()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nebula Industries")

        self.setWindowFlags(
            Qt.WindowType.Window
            | Qt.WindowType.FramelessWindowHint
        )

        self.canvas = DesignCanvas()
        self.setCentralWidget(self.canvas)

        self.set_initial_size()

    def set_initial_size(self):

        screen = QApplication.primaryScreen()
        available = screen.availableGeometry()

        width = round(
            available.width()
            * theme.MAIN_WINDOW_SCREEN_RATIO
        )

        height = round(
            available.height()
            * theme.MAIN_WINDOW_SCREEN_RATIO
        )

        self.resize(width, height)

        self.move(
            available.x()
            + (available.width() - width) // 2,

            available.y()
            + (available.height() - height) // 2
        )


def main():

    app = QApplication(sys.argv)

    app.setApplicationName(theme.APP_NAME if hasattr(theme, "APP_NAME") else "Nebula Industries")

    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
