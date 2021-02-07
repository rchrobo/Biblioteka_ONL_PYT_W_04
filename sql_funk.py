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


if __name__ == "__main__":
    create_author('slawek', 'boguslawski')