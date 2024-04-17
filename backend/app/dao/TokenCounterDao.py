from app import get_db_connection
from app.models.builder.TokenCounter import TokenCounter
import uuid

class TokenCounterDao:

    def create_tokencounter(self):
        id = str(uuid.uuid4())
        TokenCounter = TokenCounter(id)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tokencounter (id) VALUES (?, ?, ?, ?, ?)", (tokenCounter.get_id()))
        conn.commit()
        conn.close()
        return user.get_id()