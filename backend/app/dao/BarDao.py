
from app import get_db_connection
from app.models.Bar import Bar
import uuid

class BarDao:
    def create_bar(self, name, location, manager):
        id = str(uuid.uuid4())
        # create a Bar Object
        bar = Bar(id, name, location, manager)
        print(bar.get_id())
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bars (id, name, location, manager_id) VALUES (?, ?, ?, ?)", (bar.get_id(), name, location, manager))
        conn.commit()
        conn.close()
        return bar.get_id()
