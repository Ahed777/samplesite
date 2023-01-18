import psycopg2


def cursor():
    """Returns cursor

    Returns:
        cursor: returns cursor object
    """
    with psycopg2.connect(
        database="Saurabh254",
        user="saurabh",
        password='12345678',
        host="localhost",
        port='5432',
    ) as connection:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS userinfo(
            id INT PRIMARY KEY NOT NULL,
            firstname VARCHAR(50) NOT NULL,
            lastname VARCHAR(50),
            password VARCHAR(50) NOT NULL,
            lastlogin DATE NOT NULL)
            """)
        connection.commit()
    return cursor, connection
