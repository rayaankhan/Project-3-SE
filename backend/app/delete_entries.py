# from config import DB_PATH
import sqlite3
import uuid

# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect(r"C:\Users\lenovo\Downloads\Sem 6\SE\Project\3\Project-3-SE\backend\SE-Project-3.db")
    conn.row_factory = sqlite3.Row
    return conn

def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    return user_id

def drop_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE casino_token_mg")
    conn.commit()
    cursor.execute("DROP TABLE staff")
    conn.commit()
    cursor.execute("DROP TABLE bar")
    conn.commit()
    cursor.execute("DROP TABLE tokencounter")
    conn.commit()
    cursor.execute("DROP TABLE gametable")
    conn.commit()
    cursor.execute("DROP TABLE casino_bar")
    conn.commit()
    cursor.execute("DROP TABLE casino_gametable")
    conn.commit()
    conn.close()
def delete_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM gametable")
    conn.commit()
    cursor.execute("DELETE FROM tokencounter")
    conn.commit()
    cursor.execute("DELETE FROM casino_token_mg")
    conn.commit()
    cursor.execute("DELETE FROM casino_gametable")
    conn.commit()
    cursor.execute("DELETE FROM casino_bar")
    conn.commit()
    cursor.execute("DELETE FROM bar")
    conn.commit()
    conn.close()
# delete_user('efcb22e7-4171-418c-9057-943ebbc7a498')
# delete_table()
# drop_table()


# conn = get_db_connection()
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS staff (id varchar(255) PRIMARY KEY, salary int, currentAssignedId varchar(255));")
# conn.commit()
# conn.close()

def addStaff():
    conn = get_db_connection()
    cursor = conn.cursor()
    # create your tables here
    for _ in range(20):
        id = "staff_" + str(uuid.uuid4())
        cursor.execute(f"INSERT INTO staff (id, salary, currentAssignedId) VALUES ('{id}', 1000, '-1')")
        conn.commit()
    conn.close()

addStaff()