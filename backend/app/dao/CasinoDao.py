from app import get_db_connection
from app.models.builder.Casino import Casino
import uuid
import random
from datetime import datetime

class CasinoDao:

    # def create_casino(self, id, tableid, staffid, barid, tokencounterid, managerid):
        
    #     casino = Casino(id, tableid, barid, tokencounterid, staffid, managerid)
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     cursor.execute("INSERT INTO casino (id, tableid, barid, tokencounterid, staffid, managerid) VALUES (?, ?, ?, ?, ?)", (casino.get_id(), casino.get_tableid(), casino.get_tokencounterid(), casino.get_staffid(), casino.get_managerid()))
    #     conn.commit()
    #     conn.close()
    #     return casino.get_id()
    
    def add_casinoTokenMg(self, casinoId, tokenCounterId, managerId, casinoType):
        conn = get_db_connection()
        cursor = conn.cursor()
        random_number = random.randint(0, 100000)
        casinoName = "Casino" + casinoType + "-" + str(random_number)
        tokenCounterName = "TokenCounter" + "-" + str(random_number)
        cursor.execute("INSERT INTO casino_token_mg (casinoid, casinoname, tokencountername, tokencounterid, managerid) VALUES (?, ?, ?, ?, ?)", (casinoId, casinoName, tokenCounterName, tokenCounterId, managerId))
        conn.commit()
        conn.close()
        return
    
    def add_casinogametable(self, casinoId, gameTableId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO casino_gametable (casinoid, gametableid) VALUES (?, ?)", (casinoId, gameTableId))
        conn.commit()
        conn.close()
        return
    
    def add_casinobar(self, casinoId, barId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO casino_bar (casinoid, barid) VALUES (?, ?)", (casinoId, barId))
        conn.commit()
        conn.close()
        return
    
    def get_casino_list_mg(self, managerId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT casinoid, casinoname FROM casino_token_mg WHERE managerid = ?", (managerId,))
        result = cursor.fetchall()
        print(type(result))
        conn.close()
        return result
    
    def get_table_casinos(self, casinoId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT gametableid, name FROM gametable WHERE gametableid IN (SELECT gametableid FROM casino_gametable WHERE casinoid = ?)", (casinoId,))
        result = cursor.fetchall()
        conn.close()
        return result
    
    def get_bar_casinos(self, casinoId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT barid, name from bar where barid IN (SELECT barid FROM casino_bar WHERE casinoid = ?)", (casinoId,))
        result = cursor.fetchall()
        conn.close()
        return result
    
    def get_tokencounter_casinos(self, casinoId):
        conn = get_db_connection()
        cursor = conn.cursor()
        print("casinoId: ", casinoId)
        cursor.execute("SELECT tokencounterid, tokencountername FROM casino_token_mg WHERE casinoid = ?", (casinoId,))
        result = cursor.fetchall()
        conn.close()
        print("result: ", result)
        return result
    
    def add_gametable(self, gametableId, casinoId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO casino_gametable (casinoid, gametableid) VALUES (?, ?)", (casinoId, gametableId))
        conn.commit()
        conn.close()
        return
    
    def add_bar(self, barId, casinoId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO casino_bar (casinoid, barid) VALUES (?, ?)", (casinoId, barId))
        conn.commit()
        conn.close()
        return
    
    def delete_casino_overall(self, casinoId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM casino_token_mg WHERE casinoid = ?", (casinoId,))
        cursor.execute("DELETE FROM casino_gametable WHERE casinoid = ?", (casinoId,))
        cursor.execute("DELETE FROM casino_bar WHERE casinoid = ?", (casinoId,))
        cursor.execute("DELETE FROM casino_analytics WHERE casinoid = ?", (casinoId,))
        cursor.execute("DELETE FROM user_subscription WHERE casinoid = ?", (casinoId,))
        conn.commit()
        conn.close()
        return
    
    def unassign_staff(self, objectIdList):
        conn = get_db_connection()
        cursor = conn.cursor()
        for objectId in objectIdList:
            cursor.execute("UPDATE staff SET currentassignedid = -1 WHERE currentassignedid = ?", (objectId,))
        conn.commit()
        conn.close()
        return
    
    def get_all_casinos(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT casinoid, casinoname FROM casino_token_mg")
        result = cursor.fetchall()
        conn.close()
        return result
    
    def get_casino_id_by_gametableid(self, gametableId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT casinoid FROM casino_gametable WHERE gametableid = ?", (gametableId,))
        result = cursor.fetchone()
        conn.close()
        return result[0]
