import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde .env
load_dotenv()

class Config:
    # Database Configuration
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_SERVER = os.getenv('DB_SERVER')
    DB_NAME = os.getenv('DB_NAME')
    
    # Agregar el SECRET_KEY
    SECRET_KEY = os.getenv('SECRET_KEY')  # Aquí es donde defines el SECRET_KEY
    
    SQLALCHEMY_DATABASE_URI = (
        f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
