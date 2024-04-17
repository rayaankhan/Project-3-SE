from app import get_db_connection
from app.models.builder.Bar import Bar
import uuid

class BarDao:

    def create_bar(self, staffid, prob, drinks):
        id = str(uuid.uuid4())
        bar = Bar(id, staffid, drinks)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO gametable (id, staffid, drinks) VALUES (?, ?, ?, ?, ?)", (bar.get_id(), bar.get_staffid(), bar.get_drinks()))
        conn.commit()
        conn.close()
        return bar.get_id()