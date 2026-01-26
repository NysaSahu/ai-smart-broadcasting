import time

class MetricsLogger:
    
    #Records system-level events for observability and demo purposes.
    

    def log_switch(self, old_mode, new_mode):
        
        #Log a successful delivery-mode switch.
        
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] SWITCH: {old_mode} → {new_mode}")

    def log_blocked(self, current_mode, requested_mode):
        
        #Log a blocked delivery-mode switch due to stability constraints.
        
        timestamp = time.strftime("%H:%M:%S")
        print(
            f"[{timestamp}] BLOCKED: "
            f"{current_mode} → {requested_mode} (stability protection)"
        )
