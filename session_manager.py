import time

class MBOSSession:
    
    #Maintains delivery-mode state and enforces stability constraints.
    

    def __init__(self, initial_mode="UNICAST", min_dwell_time=5):
        # Current delivery mode (UNICAST / MULTICAST / BROADCAST)
        self.current_mode = initial_mode

        # Timestamp of the last successful switch
        self.last_switch_time = time.time()

        # Minimum time (seconds) to stay in one mode
        self.min_dwell_time = min_dwell_time

    def can_switch(self):
        
        #Check whether the minimum dwell time has passed.
        
        elapsed = time.time() - self.last_switch_time
        return elapsed >= self.min_dwell_time

    def switch_mode(self, new_mode):
        
        #Switch to a new delivery mode if allowed.
        
        if new_mode == self.current_mode:
            return False  # No switch needed

        if not self.can_switch():
            return False  # Stability protection

        self.current_mode = new_mode
        self.last_switch_time = time.time()
        return True
