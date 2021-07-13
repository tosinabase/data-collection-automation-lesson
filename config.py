import os
from dotenv import load_dotenv

# https://pypi.org/project/python-dotenv/
dotenv_path = os.path.join(os.path.dirname(__file__), 'credentials.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


OMDB_API_KEY = os.environ.get("OMDB_API_KEY")
