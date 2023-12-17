from config.config import REDIS_HOST, REDIS_PORT, REDIS_PWD, REDIS_DB

from redis import Redis


redis_store = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PWD)