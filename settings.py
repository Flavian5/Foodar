# settings.py
from os import environ as env
from os.path import join, dirname
from dotenv import load_dotenv

DOTENV_PATH = join(dirname(__file__), '.env')

load_dotenv(DOTENV_PATH, verbose=True, override=False)
GOOGLE_APPLICATION_CREDENTIALS = env.get('GOOGLE_APPLICATION_CREDENTIALS')
API_KEY = env.get('API_KEY')
