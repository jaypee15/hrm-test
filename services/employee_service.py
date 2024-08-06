# services/employee_service.py
from models.employee import Employee

class EmployeeService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_all_employees(self):
        # Fetch employees from database
        # This is a mock implementation
        return [
            Employee(1, "John Doe", "Manager"),
            Employee(2, "Jane Smith", "Developer")
        ]
