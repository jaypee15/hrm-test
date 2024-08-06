# managers/navigation_manager.py
from PyQt5.QtWidgets import QStackedWidget
from pages.login_page import LoginPage
from pages.employee_list_page import EmployeeListPage
from pages.finance_page import FinancePage

class NavigationManager:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.stack = QStackedWidget()

    def show_login_page(self):
        login_page = LoginPage(self)
        self.stack.addWidget(login_page)
        self.stack.setCurrentWidget(login_page)
        login_page.show()

    def show_employee_list_page(self):
        employee_list_page = EmployeeListPage(self)
        self.stack.addWidget(employee_list_page)
        self.stack.setCurrentWidget(employee_list_page)
        employee_list_page.show()
        employee_list_page.controller.load_employees()  
        
    def show_finance_page(self):
        finance_page = FinancePage(self)
        self.stack.addWidget(finance_page)
        self.stack.setCurrentWidget(finance_page)
        finance_page.controller.load_finance()
        finance_page.show()