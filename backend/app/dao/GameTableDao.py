from app import get_db_connection
from app.models.builder.GameTable import GameTable
import uuid

class GameTableDao:

    def create_gametable(self, staffid, prob, type, tableType):
        id = "gametable" + tableType + "_" + str(uuid.uuid4())
        gameTable = GameTable(id, staffid, prob, type)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO gametable (id, staffid, prob, type) VALUES (?, ?, ?, ?)", (gameTable.get_id(), gameTable.get_staffid(), gameTable.get_prob(), gameTable.get_type()))
        conn.commit()
        conn.close()
        return gameTable.get_id()
    
    def create_gametableA(self, staffid):
        return self.create_gametable(staffid, 0.3, "dice", 'A')
    
    def create_gametableB(self, staffid):
        return self.create_gametable(staffid, 0.7, "card", 'B')
    
    def create_gametableC(self, staffid):
        return self.create_gametable(staffid, 0.5, "card", 'C')
    
    def create_gametableD(self, staffid):
        return self.create_gametable(staffid, 0.5, "dice", 'D')
    
    def get_table_info(self, gametableId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM gametable WHERE id = ?", (gametableId,))
        result = cursor.fetchone()
        conn.close()
        return result
    
    def update_gametable_staff(self, gametableId, staffid):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE gametable SET staffid = ? WHERE id = ?", (staffid, gametableId))
        conn.commit()
        conn.close()
        return gametableId