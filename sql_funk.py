from connection import connect

def create_author(first_name, last_name):
    sql = f"""
    INSERT INTO author (first_name, last_name) VALUES ('{first_name}', '{last_name}');
    """
    sikorka = connect()
    alibaba = sikorka.cursor()
    alibaba.execute(sql)
    sikorka.close()


def check_if_author_exist(last_name):
    sql = """
    SELECT * FROM author where last_name='{last_name}'
    """
    sikorka = connect()
    alibaba = sikorka.cursor()
    alibaba.execute(sql)
    x = alibaba.fetchall()


    sikorka.close()
    if len(x) > 0:
        return True
    return False

def create_publisher(name, city):
    sql = f"""
    INSERT INTO publisher (name, city) VALUES ('{name}', '{city}');
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

def get_all_publishers():
    sql = """
    SELECT * FROM publisher;
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.close()
    return data

def get_author_by_id(id):
    sql = f"""
        SELECT * FROM author WHERE id={id};
        """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    connection.close()
    return data

def update_author_by_id(first_name,last_name, id):
    sql = f"""
        UPDATE author SET first_name = '{first_name}', last_name='{last_name}' WHERE id = {id};
        """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.close()

if __name__ == "__main__":
    print(get_author_by_id(1))