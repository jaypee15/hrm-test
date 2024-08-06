# controllers/login_controller.py
class LoginController:
    def __init__(self, view, navigation_manager):
        self.view = view
        self.navigation_manager = navigation_manager

    def handle_login(self):
        # Implement login logic here
        # For simplicity, we're just moving to the employee list page
        self.navigation_manager.show_employee_list_page()

    