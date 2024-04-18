from app import get_db_connection
from app.models.builder.Bar import Bar
import uuid

class BarDao:

    def create_bar(self, staffid, drinks):
        id = "bar_" + str(uuid.uuid4())
        bar = Bar(id, staffid, drinks)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bar (id, staffid, drinks) VALUES (?, ?, ?)", (bar.get_id(), bar.get_staffid(), bar.get_drinks()))
        conn.commit()
        conn.close()
        return bar.get_id()
    
    def get_bar_info(self, barId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bar WHERE id = ?", (barId,))
        result = cursor.fetchone()
        conn.close()
        return result
    
    def update_bar_staff(self, barId, staffid):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE bar SET staffid = ? WHERE id = ?", (staffid, barId))
        conn.commit()
        conn.close()
        return barId