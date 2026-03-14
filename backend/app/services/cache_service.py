import redis
import json
import os
from dotenv import load_dotenv

load_dotenv()

class CacheService:
    def __init__(self):
        self.client = redis.Redis(
            host=os.getenv("REDIS_HOST", "redis"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            decode_responses=True
        )
        self.ttl = 60 * 60 * 24  

    def get(self, key: str) -> dict | None:
        try:
            data = self.client.get(key)
            if data:
                return json.loads(data)
            return None
        except Exception:
            return None

    def set(self, key: str, value: dict) -> None:
        try:
            self.client.setex(key, self.ttl, json.dumps(value))
        except Exception:
            pass

cache_service = CacheService()