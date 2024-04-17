from app import get_db_connection
from app.models.builder.Casino import Casino
import uuid

class CasinoDao:

    def create_casino(self, id, staffid, barid, tokencounterid, staffid, managerid):
        
        casino = Casino(tableid, barid, tokencounterid, staffid, managerid)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO casino (id, tableid, barid, tokencounterid, staffid, managerid) VALUES (?, ?, ?, ?, ?)", (casino.get_id(), casino.get_tableid(), casino.get_tokencounterid(), casino.get_staffid(), casino.get_managerid()))
        conn.commit()
        conn.close()
        return gameTable.get_id()