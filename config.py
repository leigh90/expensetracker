import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))
load_dotenv('.env')
load_dotenv()



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_SECRET_KEY = os.environ.get('SECRET_KEY')


    # SQLALCHEMY_DATABASE_URI = "postgresql://leigh:bezalel84@localhost:5432/tunzamalie"
    SQLALCHEMY_TRACK_MODIFICATIONS = False



