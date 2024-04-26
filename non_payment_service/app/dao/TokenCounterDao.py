from app import get_db_connection
from app.models.builder.TokenCounter import TokenCounter
import uuid

class TokenCounterDao:

    def create_tokencounter(self):
        id = "tokencounter_" + str(uuid.uuid4())
        tokenCounter = TokenCounter(id)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tokencounter (tokencounterid) VALUES (?)", (tokenCounter.get_id(),))
        conn.commit()
        conn.close()
        return tokenCounter.get_id()