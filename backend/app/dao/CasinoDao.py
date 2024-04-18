from app import get_db_connection
from app.models.builder.Casino import Casino
import uuid

class CasinoDao:

    def create_casino(self, id, tableid, staffid, barid, tokencounterid, managerid):
        
        casino = Casino(id, tableid, barid, tokencounterid, staffid, managerid)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO casino (id, tableid, barid, tokencounterid, staffid, managerid) VALUES (?, ?, ?, ?, ?)", (casino.get_id(), casino.get_tableid(), casino.get_tokencounterid(), casino.get_staffid(), casino.get_managerid()))
        conn.commit()
        conn.close()
        return casino.get_id()
    
    def add_casinoTokenMg(self, casinoId, tokenCounterId, managerId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO casino_token_mg (id, tokencounterid, managerid) VALUES (?, ?, ?)", (casinoId, tokenCounterId, managerId))
        conn.commit()
        conn.close()
        return
    
    def add_casinogametable(self, casinoId, gameTableId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO casino_gametable (id, gametableid) VALUES (?, ?)", (casinoId, gameTableId))
        conn.commit()
        conn.close()
        return
    
    def add_casinobar(self, casinoId, barId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO casino_bar (id, barid) VALUES (?, ?)", (casinoId, barId))
        conn.commit()
        conn.close()
        return
    
    def get_casino_list_mg(self, managerId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM casino_token_mg WHERE managerid = ?", (managerId,))
        result = cursor.fetchall()
        print(type(result))
        conn.close()
        return result
    
    def get_table_casinos(self, casinoId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT gametableid FROM casino_gametable WHERE id = ?", (casinoId,))
        result = cursor.fetchall()
        conn.close()
        return result
    
    def get_bar_casinos(self, casinoId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT barid FROM casino_bar WHERE id = ?", (casinoId,))
        result = cursor.fetchall()
        conn.close()
        return result
    
    def get_tokencounter_casinos(self, casinoId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT tokencounterid FROM casino_token_mg WHERE id = ?", (casinoId,))
        result = cursor.fetchall()
        conn.close()
        return result
    
    def add_gametable(self, gametableId, casinoId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO casino_gametable (id, gametableid) VALUES (?, ?)", (casinoId, gametableId))
        conn.commit()
        conn.close()
        return
    
    def add_bar(self, barId, casinoId):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO casino_bar (id, barid) VALUES (?, ?)", (casinoId, barId))
        conn.commit()
        conn.close()
        return
