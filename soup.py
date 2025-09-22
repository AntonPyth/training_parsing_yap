import requests
from bs4 import BeautifulSoup
# Загрузка страницы с документацией для Python четвёртой версии.
response = requests.get('https://docs.python.org/3.9/')
# Создание "супа" из веб-страницы.
soup = BeautifulSoup(response.text, features='lxml')

# Печать "супа".
print(soup.html.p.prettify())

# from bs4 import BeautifulSoup

# simple_html = '<html><body><p>Это самый простой HTML!</p></body></html>'
# soup = BeautifulSoup(simple_html, features='lxml')
# tag_p = soup.html
# print(tag_p)


# import requests
# from bs4 import BeautifulSoup
# # Загрузка страницы с документацией для Python четвёртой версии.
# response = requests.get('https://docs.python.org/3.9/')
# # Создание "супа" из веб-страницы.
# soup = BeautifulSoup(response.text, features='lxml')
# # Печать "супа".
# print(soup.prettify())
