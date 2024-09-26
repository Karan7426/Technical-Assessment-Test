import time
from rate_limiter import RateLimiter

def main():
    rate_limiter = RateLimiter(max_requests=5, time_window=60)   

    user_id = "user123"

    for i in range(10):
        if rate_limiter.allow_request(user_id):
            print(f"Request {i+1} allowed.")
        else:
            print(f"Request {i+1} denied.")

         
        time.sleep(10)   

if __name__ == "__main__":
    main()
