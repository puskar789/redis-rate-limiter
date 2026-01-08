import redis

class RateLimiter:
    def __init__(self):
        self.redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def allow_request(self, ip_address, api_route, max_requests, window_seconds) -> bool:
        key = f"rate:{ip_address}:{api_route}"

        created = self.redis_client.set(key, 1, ex=window_seconds, nx=True)

        if created:
            return True

        count = int(self.redis_client.incr(key))

        if count <= max_requests:
            return True

        return False
    
