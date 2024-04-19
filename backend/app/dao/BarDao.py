from app import get_db_connection
from app.models.builder.Bar import Bar
import uuid
import random

class BarDao:

    def create_bar(self, staffid, drinks):
        id = "bar_" + str(uuid.uuid4())
        random_number = random.randint(0, 100000)
        name = "Bar-" + str(random_number)
        bar = Bar(id, name, staffid, drinks)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bar (barid, name, staffid, drinks) VALUES (?, ?, ?, ?)", (bar.get_id(), bar.get_name(), bar.get_staffid(), bar.get_drinks()))
        conn.commit()
        conn.close()
        return bar.get_id()
    
    def get_bar_info(self, barId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bar WHERE barid = ?", (barId,))
        result = cursor.fetchone()
        conn.close()
        return result
    
    def update_bar_staff(self, barId, staffid):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE bar SET staffid = ? WHERE barid = ?", (staffid, barId))
        conn.commit()
        conn.close()
        return barId
    
    def delete_bar(self, barId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM bar WHERE barid = ?", (barId,))
        conn.commit()
        conn.close()
        return barId