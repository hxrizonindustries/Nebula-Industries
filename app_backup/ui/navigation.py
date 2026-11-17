from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import Qt

from app.ui.components.glass_panel import GlassPanel
from app.ui.components.navigation_button import NavigationButton
from app.core import theme


class Navigation(GlassPanel):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.buttons = {}

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

        self.setup_ui()

    def setup_ui(self):

        self.setFixedSize(
            theme.SIDEBAR_WIDTH,
            theme.SIDEBAR_HEIGHT
        )

        layout = QVBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(theme.NAV_BUTTON_SPACING)

        # Vertical centering
        layout.addStretch()

        for title, description in self.sections:

            button = NavigationButton(title, description)

            button.clicked.connect(
                lambda checked=False, name=title:
                self.select_button(name)
            )

            layout.addWidget(
                button,
                alignment=Qt.AlignmentFlag.AlignHCenter
            )

            self.buttons[title] = button

        # Vertical centering
        layout.addStretch()

        # Dashboard selected by default
        self.select_button("DASHBOARD")

    def select_button(self, selected_title):

        for title, button in self.buttons.items():

            button.setChecked(title == selected_title)
