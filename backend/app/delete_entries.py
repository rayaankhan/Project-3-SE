# from config import DB_PATH
import sqlite3
from config import DB_PATH
# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    return user_id

def delete_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE manager_casinos")
    conn.commit()
    conn.close()

# delete_user('efcb22e7-4171-418c-9057-943ebbc7a498')
delete_table()