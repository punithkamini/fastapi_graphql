from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
conn_string = URL.create(drivername="postgresql+psycopg2", username="postgres", password="Punith007#",
                         host="localhost", database="fastapi")

engine = create_engine(conn_string)

conn = engine.connect()
Base = declarative_base()
metadata = MetaData(bind=engine)
MetaData.reflect(metadata)
tables = metadata.tables
