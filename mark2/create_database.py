import sqlite3
import os
if not os.path.exists('database.db'):

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    sql = """
    DROP TABLE IF EXISTS users;
    CREATE TABLE users (
               id integer unique primary key autoincrement,
               name text  
    );
    """
    c.executescript(sql)
    conn.commit()
    conn.close() 

