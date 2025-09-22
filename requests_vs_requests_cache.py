from time import sleep
import requests
import requests_cache

from tqdm import tqdm

DELAYED_URL = 'https://httpbin.org/delay/3'

if __name__ == '__main__':
    for i in tqdm(range(3), desc='Загрузка с сервера'):
        requests.get(DELAYED_URL)

    requests_cache.install_cache('demo_cache')
    requests.get(DELAYED_URL)

    session = requests_cache.CachedSession()
    session.cache.clear()

    for i in tqdm(range(3), desc='Загрузка из кэша'):
        requests.get(DELAYED_URL)
    requests_cache.clear()
    
print('Это наконец случилось !!!')
