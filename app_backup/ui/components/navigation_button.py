
from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QLabel,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from app.core import theme


class NavigationButton(QPushButton):

    def __init__(self, title, description, parent=None):
        super().__init__(parent)

        self.title = title
        self.description = description

        self.selected = False

        self.setup_ui()

    def setup_ui(self):

        # Button dimensions
        self.setFixedSize(
            theme.NAV_BUTTON_WIDTH,
            theme.NAV_BUTTON_HEIGHT
        )

        self.setCheckable(True)

        self.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        # Prevent native focus/default button styling
        self.setFocusPolicy(
            Qt.FocusPolicy.NoFocus
        )

        self.setAutoDefault(False)
        self.setDefault(False)

        # Button layout
        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            22, 6, 22, 6
        )

        layout.setSpacing(0)

        # Title
        self.title_label = QLabel(self.title)

        self.title_label.setFixedHeight(24)

        title_font = QFont(
            theme.FONT_TITLE,
            theme.FONT_SIZE_TITLE
        )

        self.title_label.setFont(title_font)

        self.title_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignVCenter
        )

        # Description
        self.description_label = QLabel(
            self.description
        )

        self.description_label.setFixedHeight(24)

        description_font = QFont(
            theme.FONT_MAIN,
            theme.FONT_SIZE_MAIN
        )

        self.description_label.setFont(
            description_font
        )

        self.description_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignVCenter
        )

        # Labels must never intercept mouse events
        self.title_label.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents
        )

        self.description_label.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents
        )

        # Add labels
        layout.addWidget(self.title_label)
        layout.addWidget(self.description_label)

        # Styling
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: rgba(255, 255, 255, 26);
                border: none;
                border-radius: {theme.GLASS_BORDER_RADIUS}px;
                text-align: left;
                color: #FFFFFF;
            }}

            QPushButton:hover {{
                background-color: rgba(255, 255, 255, 26);
                border: none;
            }}

            QPushButton:checked {{
                background-color: {theme.ACCENT};
                border: none;
            }}

            QPushButton:checked:hover {{
                background-color: {theme.ACCENT};
                border: none;
            }}

            QPushButton:pressed {{
                background-color: rgba(255, 255, 255, 26);
                border: none;
            }}

            QPushButton:checked:pressed {{
                background-color: {theme.ACCENT};
                border: none;
            }}

            QLabel {{
                color: #FFFFFF;
                background: transparent;
                border: none;
            }}
        """)

