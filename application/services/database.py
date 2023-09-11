from sqlalchemy_utils import create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from urllib.parse import quote

instance: str = f"mysql+pymysql://test:{quote('test')}@localhost:3306/hamburgueria"

if not database_exists(instance):
    create_database(instance)

engine = create_engine(instance)
session = Session(engine)

