from config import IS_DEVELOPMENT
from config import POSTGRES_DB as db
from config import POSTGRES_HOST as host
from config import POSTGRES_PASSWORD as password
from config import POSTGRES_PORT as port
from config import POSTGRES_USER as user
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    f"postgresql://{user}:{password}@{host}:{port}/{db}", echo=IS_DEVELOPMENT
)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()


def reset_db():
    if IS_DEVELOPMENT:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
