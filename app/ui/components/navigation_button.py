
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPainter, QColor, QFont

from app.core import theme


class NavigationButton(QWidget):

    clicked = Signal()

    def __init__(self, title, description, parent=None):
        super().__init__(parent)

        self.title = title
        self.description = description
        self.selected = False
        self.hovered = False
        self.scale_factor = 1.0

        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setMouseTracking(True)

        self.setup_shadow()
        self.set_scale(1.0)

    def setup_shadow(self):
        self.shadow = QGraphicsDropShadowEffect(self)

        self.shadow.setColor(QColor(0, 0, 0, 64))
        self.setGraphicsEffect(self.shadow)

    def set_scale(self, scale):
        self.scale_factor = scale

        self.setFixedSize(
            round(theme.NAV_BUTTON_WIDTH * scale),
            round(theme.NAV_BUTTON_HEIGHT * scale)
        )

        self.shadow.setBlurRadius(
            theme.BUTTON_SHADOW_BLUR * scale
        )

        self.shadow.setOffset(
            theme.BUTTON_SHADOW_OFFSET_X * scale,
            theme.BUTTON_SHADOW_OFFSET_Y * scale
        )

        self.update()

    def set_selected(self, selected):
        if self.selected == selected:
            return

        self.selected = selected
        self.update()

    def enterEvent(self, event):
        self.hovered = True
        self.update()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.hovered = False
        self.update()
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()

        super().mousePressEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        scale = self.scale_factor

        if self.selected:
            background = QColor(230, 211, 103, 115)
        elif self.hovered:
            background = QColor(255, 255, 255, 38)
        else:
            background = QColor(255, 255, 255, 26)

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(background)

        painter.drawRoundedRect(
            self.rect().adjusted(
                round(scale),
                round(scale),
                -round(scale),
                -round(scale)
            ),
            theme.GLASS_BORDER_RADIUS * scale,
            theme.GLASS_BORDER_RADIUS * scale
        )

        title_font = QFont(theme.FONT_TITLE)
        title_font.setPixelSize(
            round(theme.FONT_SIZE_TITLE * scale)
        )

        painter.setFont(title_font)
        painter.setPen(QColor(theme.TEXT))

        painter.drawText(
            round(22 * scale),
            round(6 * scale),
            round(308 * scale),
            round(24 * scale),
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignVCenter,
            self.title
        )

        description_font = QFont(theme.FONT_MAIN)
        description_font.setPixelSize(
            round(theme.FONT_SIZE_MAIN * scale)
        )

        painter.setFont(description_font)

        painter.drawText(
            round(22 * scale),
            round(30 * scale),
            round(308 * scale),
            round(24 * scale),
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignVCenter,
            self.description
        )
