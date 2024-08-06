# managers/state_manager.py
class StateManager:
    def __init__(self):
        self.current_user = None
        # Add other state variables as needed

    def set_current_user(self, user):
        self.current_user = user