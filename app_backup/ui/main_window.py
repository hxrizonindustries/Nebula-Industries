
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGraphicsView,
    QGraphicsScene,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QPainter,
    QLinearGradient,
    QColor,
)

from app.core import theme
from app.ui.navigation import Navigation
from app.ui.components.header import Header


class DesignCanvas(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(
            theme.DESIGN_WIDTH,
            theme.DESIGN_HEIGHT
        )

        # Header
        self.header = Header(self)
        self.header.move(0, 0)

        # Sidebar
        self.navigation = Navigation(self)
        self.navigation.move(
            theme.SIDEBAR_X,
            theme.SIDEBAR_Y
        )

        # Invisible content container
        self.content_frame = QWidget(self)
        self.content_frame.setGeometry(
            theme.CONTENT_X,
            theme.CONTENT_Y,
            theme.CONTENT_WIDTH,
            theme.CONTENT_HEIGHT
        )

        self.content_frame.setStyleSheet("""
            background: transparent;
            border: none;
        """)

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        gradient = QLinearGradient(
            0, 0,
            theme.DESIGN_WIDTH,
            theme.DESIGN_HEIGHT
        )

        gradient.setColorAt(
            0.0,
            QColor("#682164")
        )

        gradient.setColorAt(
            1.0,
            QColor("#552F6F")
        )

        painter.fillRect(
            self.rect(),
            gradient
        )


class ScaledGraphicsView(QGraphicsView):

    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)

        self.setFrameShape(
            QGraphicsView.Shape.NoFrame
        )

        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self.setAlignment(
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignTop
        )

        self.setTransformationAnchor(
            QGraphicsView.ViewportAnchor.NoAnchor
        )

        self.setResizeAnchor(
            QGraphicsView.ViewportAnchor.NoAnchor
        )

        self.setStyleSheet("""
            QGraphicsView {
                border: none;
                background: transparent;
            }
        """)

        self.setBackgroundBrush(
            QColor(0, 0, 0, 0)
        )

        self.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

    def resizeEvent(self, event):

        super().resizeEvent(event)

        # Fill the entire available window.
        # Both axes scale independently.
        self.fitInView(
            self.sceneRect(),
            Qt.AspectRatioMode.IgnoreAspectRatio
        )


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Nebula Industries"
        )

        self.setWindowFlags(
            Qt.WindowType.Window |
            Qt.WindowType.FramelessWindowHint
        )

        self.setup_ui()
        self.set_initial_size()

    def setup_ui(self):

        self.canvas = DesignCanvas()

        self.scene = QGraphicsScene(self)

        self.scene.setSceneRect(
            0,
            0,
            theme.DESIGN_WIDTH,
            theme.DESIGN_HEIGHT
        )

        self.scene.addWidget(
            self.canvas
        )

        self.view = ScaledGraphicsView(
            self.scene
        )

        self.setCentralWidget(
            self.view
        )

    def set_initial_size(self):

        screen = QApplication.primaryScreen()
        available = screen.availableGeometry()

        width = round(
            available.width() *
            theme.MAIN_WINDOW_SCREEN_RATIO
        )

        height = round(
            available.height() *
            theme.MAIN_WINDOW_SCREEN_RATIO
        )

        self.resize(width, height)

        self.move(
            available.x() +
            (available.width() - width) // 2,

            available.y() +
            (available.height() - height) // 2
        )
