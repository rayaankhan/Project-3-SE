from app import get_db_connection

class TokenWalletDao:
    def get_wallet_balance(self, wallet_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT token_balance FROM user_token_wallet WHERE walletid=?", (wallet_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0]

    def update_wallet_balance(self, wallet_id, amount):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE user_token_wallet SET token_balance=? WHERE walletid=?", (amount, wallet_id))
        conn.commit()
        conn.close()
        return wallet_id