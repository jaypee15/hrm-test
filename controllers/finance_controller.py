from services.finance_service import FinanceService

class FinanceController:
    def __init__(self, view):
        self.view = view
        self.finance_service = FinanceService("")
      
    def load_finance(self):
        finance = self.finance_service.get_all_finance()
        self.view.display_employees_finance(finance)