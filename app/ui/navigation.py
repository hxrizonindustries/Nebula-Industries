
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor

from app.ui.components.navigation_button import NavigationButton
from app.core import theme


class Navigation(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.buttons = {}
        self.scale_factor = 1.0

        self.sections = [
            ("DASHBOARD", "Main overview"),
            ("MARKET", "Browse and compare market prices"),
            ("APPRAISAL", "Evaluate item lists"),
            ("CALCULATOR", "Profit, taxes, hauling, manufacturing, etc"),
            ("SHIPS AND ITEMS", "Browse EVE's item database"),
            ("FITTINGS", "Create and manage ship fits"),
            ("SKILL PLANS", "Plan character training"),
            ("NOTEPADS", "Store notes"),
            ("TO-DO LISTS", "Manage tasks"),
            ("OVERVIEWS", "Manage overview configurations"),
            ("CORPORATION", "NBI corporation information"),
            ("PHONE NOTIFICATIONS", "Send notifications when something goes on"),
            ("SETTINGS", "Configure the application"),
        ]

        self.setAttribute(
            Qt.WidgetAttribute.WA_StyledBackground,
            True
        )

        self.setup_shadow()
        self.create_buttons()
        self.set_scale(1.0)
        self.select_button("DASHBOARD")

    def setup_shadow(self):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setColor(QColor(0, 0, 0, 64))
        self.setGraphicsEffect(self.shadow)

    def create_buttons(self):
        for title, description in self.sections:
            button = NavigationButton(
                title,
                description,
                self
            )

            button.clicked.connect(
                lambda name=title: self.select_button(name)
            )

            self.buttons[title] = button

    def set_scale(self, scale):
        self.scale_factor = scale

        self.setFixedSize(
            round(theme.SIDEBAR_WIDTH * scale),
            round(theme.SIDEBAR_HEIGHT * scale)
        )

        self.shadow.setBlurRadius(
            theme.SIDEBAR_SHADOW_BLUR * scale
        )

        self.shadow.setOffset(
            theme.SIDEBAR_SHADOW_OFFSET_X * scale,
            theme.SIDEBAR_SHADOW_OFFSET_Y * scale
        )

        button_x = round(
            (theme.SIDEBAR_WIDTH - theme.NAV_BUTTON_WIDTH)
            / 2 * scale
        )

        for index, button in enumerate(self.buttons.values()):
            button.set_scale(scale)

            button_y = round(
                (
                    theme.NAV_BUTTON_START_Y
                    + index * (
                        theme.NAV_BUTTON_HEIGHT
                        + theme.NAV_BUTTON_SPACING
                    )
                ) * scale
            )

            button.move(button_x, button_y)

    def select_button(self, selected_title):
        for title, button in self.buttons.items():
            button.set_selected(title == selected_title)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(255, 255, 255, 26))

        radius = theme.GLASS_BORDER_RADIUS * self.scale_factor

        painter.drawRoundedRect(
            self.rect().adjusted(1, 1, -1, -1),
            radius,
            radius
        )
