from connection import connect

sql1 = """
CREATE TABLE author (
    id serial primary key,
    first_name varchar(25),
    last_name varchar(25)
);
"""

sql2 = """
CREATE TABLE publisher (
    id serial primary key,
    name varchar(25),
    city varchar(25)
);
"""
sql3 = """
CREATE TABLE book (
    id serial primary key,
    title varchar(25),
    author_id integer,
    publisher_id integer,
    FOREIGN KEY(author_id) REFERENCES author(id) ON DELETE CASCADE,
    FOREIGN KEY(publisher_id) REFERENCES publisher(id) ON DELETE CASCADE
);
"""


def create_tables():
    tables = [sql1, sql2, sql3]
    connection = connect()
    cursor = connection.cursor()
    for table in tables:
        try:
            cursor.execute(table)
        except Exception as e:
            print(e, table[:50])
    connection.close()


if __name__ == "__main__":
    create_tables()
