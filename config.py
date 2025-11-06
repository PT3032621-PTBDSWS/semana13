import os
from dotenv import load_dotenv

# Carrega .env 
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "troque_esta_chave_por_uma_secreta")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///usuarios.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mailgun
    MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY", "")
    MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN", "")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "flaskaulasweb@zohomail.com")
