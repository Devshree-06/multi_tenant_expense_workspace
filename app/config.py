from dotenv import load_dotenv

import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")

SECRET_KEY = os.getenv("SECRET_KEY")