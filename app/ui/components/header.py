
from datetime import datetime, timezone, timedelta

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QColor, QFont

from app.core import theme


class Header(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.scale_factor = 1.0

        self.character_name = "WELCOME, PILOT"

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground,
            True
        )

        self.setFixedHeight(theme.HEADER_HEIGHT)

    def set_character_name(self, name):
        self.character_name = name.upper()
        self.update()

    def set_scale(self, scale):
        self.scale_factor = scale

        self.setFixedSize(
            round(theme.HEADER_WIDTH * scale),
            round(theme.HEADER_HEIGHT * scale)
        )

        self.update()

    def downtime_remaining(self):
        now = datetime.now(timezone.utc)

        downtime = now.replace(
            hour=11,
            minute=0,
            second=0,
            microsecond=0
        )

        if now >= downtime:
            downtime += timedelta(days=1)

        remaining = downtime - now

        total_seconds = int(remaining.total_seconds())

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        painter.scale(
            self.scale_factor,
            self.scale_factor
        )

        # HEADER BACKGROUND
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(
            QColor(255, 255, 255, 26)
        )

        painter.drawRect(
            0, 0,
            theme.HEADER_WIDTH,
            theme.HEADER_HEIGHT
        )

        # DOWNTIME PANEL
        self.draw_panel(
            painter,
            109, 30, 239, 60
        )

        self.draw_text(
            painter,
            "TIME UNTIL DOWNTIME",
            109, 34, 239, 22,
            13
        )

        self.draw_text(
            painter,
            self.downtime_remaining(),
            109, 53, 239, 27,
            20
        )

        # CLOCK AND DATE PANEL
        self.draw_panel(
            painter,
            1078, 12, 403, 96
        )

        now = datetime.now()

        self.draw_text(
            painter,
            now.strftime("%H:%M:%S"),
            1078, 22, 403, 43,
            32
        )

        self.draw_text(
            painter,
            now.strftime("%A, %d %B %Y"),
            1078, 65, 403, 25,
            16
        )

        # CHARACTER GREETING
        self.draw_panel(
            painter,
            2233, 0, 452, 120
        )

        self.draw_text(
            painter,
            self.character_name,
            2233, 0, 452, 120,
            23
        )

    def draw_panel(self, painter, x, y, width, height):
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(
            QColor(255, 255, 255, 26)
        )

        painter.drawRoundedRect(
            x, y, width, height,
            50, 50
        )

    def draw_text(
        self,
        painter,
        text,
        x,
        y,
        width,
        height,
        size
    ):
        font = QFont(theme.FONT_MAIN)
        font.setPixelSize(size)

        painter.setFont(font)
        painter.setPen(QColor(theme.TEXT))

        painter.drawText(
            x, y, width, height,
            Qt.AlignmentFlag.AlignCenter,
            text
        )
