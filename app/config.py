import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    def __init__(self):
        self.BOT_TOKEN = os.getenv('BOT_TOKEN')
        self.DB_USERNAME = os.getenv('DB_USERNAME')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')
        self.DB_HOSTNAME = os.getenv('DB_HOSTNAME')
        self.DB_PORT = os.getenv('DB_PORT')
        self.DB_NAME = os.getenv('DB_NAME')

    def get_db_url(self):
        return f'postgresql+asyncpg://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOSTNAME}:{self.DB_PORT}/{self.DB_NAME}'

    def get_bot_token(self):
        return self.BOT_TOKEN


config = Config()
