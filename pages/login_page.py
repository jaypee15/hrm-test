# pages/login_page.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from controllers.login_controller import LoginController

class LoginPage(QWidget):
    def __init__(self, navigation_manager):
        super().__init__()
        self.navigation_manager = navigation_manager
        self.controller = LoginController(self, navigation_manager)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.controller.handle_login)
        layout.addWidget(login_button)
        self.setLayout(layout)