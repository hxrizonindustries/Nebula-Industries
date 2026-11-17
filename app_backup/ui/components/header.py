
from datetime import datetime, timedelta, timezone

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)
from PySide6.QtCore import Qt, QTimer

from app.ui.components.glass_panel import GlassPanel
from app.core import theme


class Header(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.character_name = "Capsuleer"

        self.setFixedSize(
            theme.HEADER_WIDTH,
            theme.HEADER_HEIGHT
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_StyledBackground,
            True
        )

        self.setStyleSheet("""
            background-color: rgba(255, 255, 255, 18);
            border: none;
        """)

        self.setup_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(
            self.update_information
        )
        self.timer.start(1000)

        self.update_information()

    def setup_ui(self):

        # ==================================
        # DOWNTIME COUNTDOWN - LEFT
        # ==================================

        self.downtime_panel = GlassPanel(
            self,
            radius=50
        )

        self.downtime_panel.setGeometry(
            109, 30, 239, 60
        )

        downtime_layout = QVBoxLayout(
            self.downtime_panel
        )

        downtime_layout.setContentsMargins(
            15, 5, 15, 5
        )

        downtime_layout.setSpacing(0)

        self.downtime_title = QLabel(
            "TIME UNTIL RESTART"
        )

        self.downtime_value = QLabel(
            "--:--:--"
        )

        for label in (
            self.downtime_title,
            self.downtime_value
        ):

            label.setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            label.setStyleSheet(f"""
                color: {theme.TEXT};
                font-family: "{theme.FONT_MAIN}";
                font-size: {theme.FONT_SIZE_MAIN}px;
                background: transparent;
                border: none;
            """)

        downtime_layout.addWidget(
            self.downtime_title
        )

        downtime_layout.addWidget(
            self.downtime_value
        )

        # ==================================
        # CLOCK AND DATE - CENTER
        # ==================================

        self.clock_panel = GlassPanel(
            self,
            radius=50
        )

        self.clock_panel.setGeometry(
            1078, 12, 403, 96
        )

        clock_layout = QVBoxLayout(
            self.clock_panel
        )

        clock_layout.setContentsMargins(
            20, 10, 20, 10
        )

        clock_layout.setSpacing(0)

        self.clock_label = QLabel()
        self.date_label = QLabel()

        for label in (
            self.clock_label,
            self.date_label
        ):

            label.setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            label.setStyleSheet(f"""
                color: {theme.TEXT};
                font-family: "{theme.FONT_MAIN}";
                font-size: {theme.FONT_SIZE_MAIN}px;
                background: transparent;
                border: none;
            """)

        clock_layout.addWidget(
            self.clock_label
        )

        clock_layout.addWidget(
            self.date_label
        )

        # ==================================
        # PLAYER GREETING - RIGHT
        # ==================================

        self.greeting_panel = GlassPanel(
            self,
            radius=50
        )

        self.greeting_panel.setGeometry(
            2188, 12, 341, 96
        )

        greeting_layout = QVBoxLayout(
            self.greeting_panel
        )

        greeting_layout.setContentsMargins(
            15, 10, 20, 10
        )

        greeting_layout.setSpacing(0)

        self.greeting_label = QLabel(
            "HELLO THERE,"
        )

        self.character_label = QLabel(
            self.character_name.upper()
        )

        for label in (
            self.greeting_label,
            self.character_label
        ):

            label.setAlignment(
                Qt.AlignmentFlag.AlignRight |
                Qt.AlignmentFlag.AlignVCenter
            )

            label.setStyleSheet(f"""
                color: {theme.TEXT};
                font-family: "{theme.FONT_MAIN}";
                font-size: {theme.FONT_SIZE_MAIN}px;
                background: transparent;
                border: none;
            """)

        greeting_layout.addWidget(
            self.greeting_label
        )

        greeting_layout.addWidget(
            self.character_label
        )

    def update_information(self):

        now = datetime.now().astimezone()

        # Local system clock
        self.clock_label.setText(
            now.strftime("%H:%M")
        )

        # Local system date
        self.date_label.setText(
            now.strftime("%A %d, %B, %Y").upper()
        )

        # EVE Online daily downtime: 11:00 UTC
        downtime = datetime.combine(
            now.date(),
            datetime.min.time(),
            tzinfo=timezone.utc
        ) + timedelta(hours=11)

        now_utc = now.astimezone(timezone.utc)

        if now_utc >= downtime:
            downtime += timedelta(days=1)

        remaining = downtime - now_utc

        total_seconds = int(
            remaining.total_seconds()
        )

        hours, remainder = divmod(
            total_seconds, 3600
        )

        minutes, seconds = divmod(
            remainder, 60
        )

        self.downtime_value.setText(
            f"{hours:02}:{minutes:02}:{seconds:02}"
        )

    def set_character(self, character_name):

        self.character_name = character_name

        self.character_label.setText(
            character_name.upper()
        )
