# redis-rate-limiter

# Redis key design:
The format rate:<ip_address>:<api_route> was chosen so that each IP address and API route combination has its own counter. The value stored is simply the request count in current window.

# How expiration is handled:

We use Redis SET with:

- ex = window_seconds, this sets TTL
- nx = True, this only create if NOT exists
- SET key 1 EX window_seconds NX, this part sets the key value pair
- First request creates key and starts the fixed window and subsequent requests do NOT reset TTL. Redis automatically deletes key when window ends. Next request after expiry creates a fresh window
- Counter increments using INCR key
- Requests counted in discrete time slots. If count exceeds limit we block remaining requests. When TTL expires, a new window starts

# Assumptions:

- Single Redis instance
- Local Redis server running
- No distributed cluster considerations
- No HTTP server, only class + driver usage
- Basic correctness is the main focus
