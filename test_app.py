
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Nebula Industries")
window.resize(900, 600)

layout = QVBoxLayout()

title = QLabel("NEBULA INDUSTRIES")
title.setStyleSheet("""
    font-size: 28px;
    font-weight: bold;
    color: #55C8FF;
""")

subtitle = QLabel("Corporate Operations Platform")
subtitle.setStyleSheet("""
    font-size: 15px;
    color: #AAB8D0;
""")

window.setStyleSheet("background-color: #0B1020; color: white;")

layout.addWidget(title)
layout.addWidget(subtitle)

window.setLayout(layout)
window.show()

sys.exit(app.exec())
