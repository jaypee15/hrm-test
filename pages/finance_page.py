# pages/finance_page.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton
from controllers.finance_controller import FinanceController

class FinancePage(QWidget):
    def __init__(self, navigation_manager):
        super().__init__()
        self.navigation_manager = navigation_manager
        self.controller = FinanceController(self)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.finance_list = QListWidget()
        layout.addWidget(self.finance_list)
        finance_button = QPushButton("finance page")
        # finance_button.clicked.connect(self.controller.handle_finance)
        layout.addWidget(finance_button)
        self.setLayout(layout)

    def display_employees_finance(self, finance):
        self.finance_list.clear()
        for employee in finance:
            self.finance_list.addItem(f"{employee.amount} - {employee.name} ")
