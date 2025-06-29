import redis.asyncio as redis
from settings import REDIS_HOST, REDIS_PORT

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

async def check_redis():
    try:
        pong = await redis_client.ping()
        print("Redis connected", pong)
    except Exception as e:
        print("Redis Error ", e)