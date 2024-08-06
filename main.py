# main.py
from PyQt5.QtWidgets import QApplication, QMainWindow
from managers.navigation_manager import NavigationManager
from managers.state_manager import StateManager
from managers.config_manager import ConfigManager

class HRMApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.config_manager = ConfigManager()
        self.state_manager = StateManager()
        self.navigation_manager = NavigationManager(self.state_manager)
        self.main_window = QMainWindow()
        self.main_window.setCentralWidget(self.navigation_manager.stack)
        self.main_window.resize(1024, 768)
        self.main_window.show()

    def run(self):
        self.navigation_manager.show_login_page()
        return self.exec_()

if __name__ == "__main__":
    import sys
    app = HRMApp(sys.argv)
    sys.exit(app.run())