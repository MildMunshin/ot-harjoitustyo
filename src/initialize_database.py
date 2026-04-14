from src.database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    cursor.execute('''
        drop table if exists days;
    ''')

    cursor.execute('''
        drop table if exists exercises;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text
        );
    ''')

    cursor.execute('''
        create table days (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            day_name TEXT NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username)
        );
    ''')

    cursor.execute('''
        create table exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day_id INTEGER,
            name TEXT,
            sets INTEGER,
            reps INTEGER,
            weight REAL 
            
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
