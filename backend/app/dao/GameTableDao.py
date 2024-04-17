from app import get_db_connection
from app.models.builder.GameTable import GameTable
import uuid

class GameTableDao:

    def create_gametable(self, staffid, prob, type):
        id = str(uuid.uuid4())
        gameTable = GameTable(id, staffid, prob, type)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO gametable (id, staffid, prob, type) VALUES (?, ?, ?, ?, ?)", (gameTable.get_id(), gameTable.get_staffid(), gameTable.get_prob(), gameTable.get_type()))
        conn.commit()
        conn.close()
        return gameTable.get_id()