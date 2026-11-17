from PySide6.QtWidgets import QFrame, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt

from app.core import theme


class GlassPanel(QFrame):

    def __init__(
        self,
        parent=None,
        radius=theme.GLASS_BORDER_RADIUS,
        shadow=True
    ):
        super().__init__(parent)

        self.radius = radius
        self.shadow_enabled = shadow

        self.setup_style()

    def setup_style(self):

        self.setAttribute(
            Qt.WidgetAttribute.WA_StyledBackground,
            True
        )

        self.setStyleSheet(f"""
            QFrame {{
                background-color: rgba(255, 255, 255, 26);
                border: none;
                border-radius: {self.radius}px;
            }}
        """)

        if self.shadow_enabled:
            self.add_shadow()

    def add_shadow(self):

        shadow = QGraphicsDropShadowEffect(self)

        shadow.setColor(
            QColor(0, 0, 0, 46)
        )

        shadow.setBlurRadius(theme.SHADOW_BLUR)

        shadow.setOffset(
            theme.SHADOW_OFFSET_X,
            theme.SHADOW_OFFSET_Y
        )

        self.setGraphicsEffect(shadow)
