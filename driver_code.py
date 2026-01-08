import time
from rate_limiter import RateLimiter

rateLimiter = RateLimiter()

ip = "1.1.1.1"
route = "/order"
max_requests = 3
window_seconds = 10

print("Testing Fixed Window Rate Limiter...")

for i in range(5):
    allowed = rateLimiter.allow_request(ip, route, max_requests, window_seconds)
    print(f"Request {i+1}: {'Allowed' if allowed else 'Blocked'}")

    time.sleep(2)

print("\nWaiting for window to expire...")
time.sleep(window_seconds + 1)

print("\nAfter window reset:")
for i in range(2):
    allowed = rateLimiter.allow_request(ip, route, max_requests, window_seconds)
    print(f"Request {i+1}: {'Allowed' if allowed else 'Blocked'}")