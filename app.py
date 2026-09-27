import redis
r = redis.Redis(host='redis', port=6379)
r.set('message', 'Hello from Python!')
value = r.get('message')
print('Value from Redis:', value.decode())
