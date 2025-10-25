import requests
from bs4 import BeautifulSoup
LOGIN_URL = 'http://158.160.172.156/login/'
# Создаем сессию для сохранения cookies
session = requests.Session()
# Устанавливаем заголовки
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
# }
# Получаем страницу логина для извлечения CSRF-токена
response = session.get(LOGIN_URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
# Ищем CSRF-токен (предполагая, что он в форме с именем 'csrfmiddlewaretoken')
csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})
csrf_value = csrf_token['value'] if csrf_token else None
# Формируем данные для отправки
data = {
    'username': 'test_parser_user',
    'password': 'testpassword',
}
if csrf_value:
    data['csrfmiddlewaretoken'] = csrf_value
# Отправляем POST-запрос с данными и заголовками
response = session.post(LOGIN_URL, data=data, headers=headers)
print(response.status_code)
