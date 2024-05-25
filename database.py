from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import dotenv
import os

dotenv.load_dotenv()

# Load the credentials and database
creds = "{0}:{1}".format(os.environ.get("DB_USER"), os.environ.get("DB_PASS"))
database = "{0}/{1}".format(os.environ.get("DB_HOST"), os.environ.get("DB_DATABASE"))

database_url = "mysql+mysqlconnector://" + creds + "@" + database
engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def start_db():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def close_db(session):
    session.close()
