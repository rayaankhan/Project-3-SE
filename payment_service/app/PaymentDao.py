from app import get_db_connection
from datetime import datetime
import uuid
class TokenWalletDao:
    def create_wallet(self, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_token_wallet (userid, token_balance) VALUES (?, ?)", (user_id, 0))
        conn.commit()
        conn.close()
        return user_id
    
    def get_wallet_balance(self, user_id):
        conn = get_db_connection()
        print(user_id)
        cursor = conn.cursor()
        cursor.execute("SELECT token_balance FROM user_token_wallet WHERE userid=?", (user_id,))
        result = cursor.fetchone()
        print("RESULTZZZZ",result[0])
        conn.close()
        return result[0]
    def update_transaction(self, user_id, casino_id, amount, transaction_type):
        txnid ="txn_"+str(uuid.uuid4())
        conn = get_db_connection()
        cursor = conn.cursor()
        date = datetime.now()
        date_str = date.strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO final_transactions (txnid, userid, casinoid, amount, datetime) VALUES (?,?, ?, ?,?)", ( txnid,user_id,casino_id, amount, date_str))
        conn.commit()
        conn.close()
        return user_id
    def update_wallet_balance(self, user_id, amount):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE user_token_wallet SET token_balance=? WHERE userid=?", (amount, user_id))
        conn.commit()
        conn.close()
        return user_id