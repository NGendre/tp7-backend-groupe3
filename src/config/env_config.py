from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv('DATABASE_URL')
database_user = os.getenv('DATABASE_USER')
database_password = os.getenv('DATABASE_PASSWORD')
database_name = os.getenv('DATABASE_NAME')
