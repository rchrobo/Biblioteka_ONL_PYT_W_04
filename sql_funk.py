from connection import connect

def create_author(first_name, last_name):
    sql = f"""
    INSERT INTO author (first_name, last_name) VALUES ('{first_name}', '{last_name}');
    """
    sikorka = connect()
    alibaba = sikorka.cursor()
    alibaba.execute(sql)
    sikorka.close()

def create_publisher(name, city):
    sql = f"""
    INSERT INTO author (name, city) VALUES ('{name}', '{city}');
    """
    sikorka = connect()
    alibaba = sikorka.cursor()
    alibaba.execute(sql)
    sikorka.close()


def get_all_authors():
    sql = """
    SELECT * FROM author;
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.close()
    return data


if __name__ == "__main__":
    for author in get_all_authors():
        print(author)