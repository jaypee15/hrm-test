from services.employee_service import EmployeeService

class EmployeeListController:
    def __init__(self, view, navigation_manager):
        self.view = view
        self.employee_service = EmployeeService("db_connection")  # You'd pass the actual connection
        self.navigation_manager = navigation_manager
      

    def load_employees(self):
        employees = self.employee_service.get_all_employees()
        self.view.display_employees(employees)

    def handle_finance(self): 
        self.navigation_manager.show_finance_page()