from .session_manager import MBOSSession

class MBOSCoordinator:
    
    #Applies delivery-mode decisions using MBOS session rules.
    

    def __init__(self, session: MBOSSession):
        self.session = session

    def apply_decision(self, decision):
        
        #Apply a delivery-mode decision.
        #Returns True if switch applied, False otherwise.
        
        if decision == self.session.current_mode:
            return False  # Already in desired mode

        if not self.session.can_switch():
            return False  # Stability protection

        return self.session.switch_mode(decision)
