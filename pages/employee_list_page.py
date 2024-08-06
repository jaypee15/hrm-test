# pages/employee_list_page.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton
from controllers.employee_list_controller import EmployeeListController

class EmployeeListPage(QWidget):
    def __init__(self, navigation_manager):
        super().__init__()
        self.navigation_manager = navigation_manager
        self.controller = EmployeeListController(self, navigation_manager)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.employee_list = QListWidget()
        layout.addWidget(self.employee_list)
        finance_button = QPushButton("finance page")
        finance_button.clicked.connect(self.controller.handle_finance)
        layout.addWidget(finance_button)
        self.setLayout(layout)

    def display_employees(self, employees):
        self.employee_list.clear()
        for employee in employees:
            self.employee_list.addItem(f"{employee.name} - {employee.position}")
