import time
import threading

class RateLimiter:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window   
        self.requests = {}   
        self.lock = threading.Lock()   

    def allow_request(self, user_id: str) -> bool:
        current_time = time.time()
        
        with self.lock:   
            
            if user_id not in self.requests:
                self.requests[user_id] = []

            # Remove timestamps older than the time window
            self.requests[user_id] = [
                timestamp for timestamp in self.requests[user_id]
                if timestamp > current_time - self.time_window
            ]

             
            if len(self.requests[user_id]) < self.max_requests:
                self.requests[user_id].append(current_time)   
                return True
            else:
                return False   
