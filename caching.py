import requests_cache


if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(DOC)
