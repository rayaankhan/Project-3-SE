from app import get_db_connection

class TokenWalletDao:
    def get_wallet_balance(self, wallet_id):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO user_token_wallet (userid, token_balance) VALUES (?, ?)", (user_id, 0))
        conn.commit()
        conn.close()
        return user_id
    
    def get_wallet_balance(self, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT token_balance FROM user_token_wallet WHERE userid=?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0]

    def update_wallet_balance(self, wallet_id, amount):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE user_token_wallet SET token_balance=? WHERE walletid=?", (amount, wallet_id))
        conn.commit()
        conn.close()
        return user_id
    def update_transaction(self, user_id, casino_id, amount, transaction_type):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO final_transactions (userid,casinoid, amount, transaction_type) VALUES (?, ?, ?,?)", (user_id,casino_id, amount, transaction_type))
        conn.commit()
        conn.close()
        return user_id