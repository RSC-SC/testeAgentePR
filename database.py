import sqlite3

def get_user(id):
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id=' + str(id))
    return cursor.fetchone()