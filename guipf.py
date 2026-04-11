import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


script_dir = os.path.dirname(os.path.abspath(__file__))  
pic_file = os.path.join(script_dir, "toji.jpg")


class LoginUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login App")
        self.setGeometry(100, 100, 300, 400)

        self.logo = QLabel()
        pixmap = QPixmap(pic_file)
        self.logo.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
        self.logo.setAlignment(Qt.AlignCenter)

        self.title = QLabel("Welcome Back")
        self.title.setAlignment(Qt.AlignCenter)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Enter Username")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Enter Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.button = QPushButton("Login")
        self.button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.logo)
        layout.addWidget(self.title)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def login(self):
        user = self.username.text()
        pwd = self.password.text()

        if user == "Awais" and pwd == "1234":
            self.title.setText("Login Successful ✅")
        else:
            self.title.setText("Wrong Credentials ❌")

app = QApplication(sys.argv)
window = LoginUI()
window.show()
sys.exit(app.exec_())