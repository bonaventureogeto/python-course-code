import sqlite3


# def initialize_db():
#     conn = sqlite3.connect('tasks.db')
#     cursor = conn.cursor()
#     cursor.executescript(open('schema.sql').read())
#     conn.commit()
#     conn.close()


# if __name__ == '__main__':
#     initialize_db()
#     print("Database initialized!")


def add_user(username, email):
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO users(username, email) VALUES(?,?)',
            (username, email)
        )


add_user("janedoe", "jane@doe.com")


def list_users():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    rows = cursor.execute('SELECT * FROM users').fetchall()
    for row in rows:
        print(dict(row))
    conn.close()


list_users()

# task manager
# blog platform
