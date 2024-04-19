from app import get_db_connection
from app.models.builder.GameTable import GameTable
import uuid
import random
from datetime import datetime

class GameTableDao:

    def create_gametable(self, staffid, prob, type, tableType):
        gametableid = "gametable" + tableType + "_" + str(uuid.uuid4())
        random_number = random.randint(0, 100000)
        name = "GameTable" + tableType + "-" + str(random_number)
        gameTable = GameTable(gametableid, name, staffid, prob, type)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO gametable (gametableid, name, staffid, prob, type) VALUES (?, ?, ?, ?, ?)", (gameTable.get_id(), gameTable.get_name(), gameTable.get_staffid(), gameTable.get_prob(), gameTable.get_type()))
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
        cursor.execute("SELECT * FROM gametable WHERE gametableid = ?", (gametableId,))
        result = cursor.fetchone()
        conn.close()
        return result
    
    def update_gametable_staff(self, gametableId, staffid):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE gametable SET staffid = ? WHERE gametableid = ?", (staffid, gametableId))
        conn.commit()
        conn.close()
        return gametableId
    
    def delete_gametable(self, gametableId):
        print("delete_gametable")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM gametable WHERE gametableid = ?", (gametableId,))
        conn.commit()
        conn.close()
        return gametableId
    
    def add_play_transaction(self, casinoid, gametableId, amount):
        conn = get_db_connection()
        cursor = conn.cursor()
        date = datetime.now()
        print("date: ", date)
        date_str = date.strftime("%Y-%m-%d %H:%M:%S")
        print("date_str: ", type(date_str))
        cursor.execute("INSERT INTO casino_analytics (casinoid, gametableid, datetime, amount) VALUES (?, ?, ?, ?)", (casinoid, gametableId, date_str, amount))
        conn.commit()
        conn.close()
        return