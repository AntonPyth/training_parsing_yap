import requests_cache
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from pathlib import Path
# from pygments import highlight
# from pygments.lexers import HtmlLexer  # Лексер для HTML
# from pygments.formatters import TerminalFormatter

DOWNLOADS_URL = 'https://docs.python.org/3/download.html'
BASE_DIR = Path(__file__).parent

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)
    soup = BeautifulSoup(response.text, features='lxml')
    # formatter = TerminalFormatter()  # Поддерживает цвета в большинстве терминалов
    # highlighted = highlight(str(soup), HtmlLexer(), formatter)
    # print(highlighted)
    main_tag = soup.find('div', {'role': 'main'})
    table_tag = main_tag.find('table', {'class': 'docutils'})
    # print(f'Вывод table_tag {table_tag}')
    # pattern = r'.+pdf-a4\.zip$'
    pdf_a4_tag = table_tag.find('a', {'href': re.compile(r'.+pdf-a4\.zip$')})
    pdf_a4_link = pdf_a4_tag['href']
    archive_url = urljoin(DOWNLOADS_URL, pdf_a4_link)
    filename = archive_url.split('/')[-1]
    response = session.get(archive_url)
    print(f'Ссылка на файл: {archive_url}')
    downloads_dir = BASE_DIR / 'downloads'
    downloads_dir.mkdir(exist_ok=True)
    archive_path = downloads_dir / filename
    with open('test.txt', 'w') as test_file:
        test_file.write('Hello, world!')
    with open(archive_path, 'wb') as file:
        file.write(response.content)
