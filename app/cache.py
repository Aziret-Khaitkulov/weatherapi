from cachetools import TTLCache

# Создаем кэш, который хранит 50 записей, срок жизни - 10 минут (600 секунд)
cache = TTLCache(maxsize=50, ttl=600)
