import psycopg2
from settings import dbinfo

def connect():
    c = psycopg2.connect(**dbinfo)
    c.autocommit = True
    return c