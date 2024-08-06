# services/employee_service.py
from models.finance import Finance

class FinanceService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_all_finance(self):
        # Fetch employees from database
        # This is a mock implementation
        return [
            Finance(1, "John Doe", "Manager", "1000"),
            Finance(2, "Jane Smith", "Developer", "2000")
        ]
