from os import environ
from dotenv import load_dotenv

# Загрузка значений переменных окружения
load_dotenv()

API_ID = environ.get('api_id')
API_HASH = environ.get('api_hash')
SESSION_STRING = environ.get('SESSION_STRING')
