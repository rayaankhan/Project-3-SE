from app import get_db_connection
# make a static subscriptionDao class
class SubscriptionDao:
    @staticmethod
    def get_subscribers_by_casino_id(casinoid):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT userid FROM user_subscription WHERE casinoid = ?", (casinoid,))
        subscriber_ids = [row[0] for row in cursor.fetchall()]
        conn.close()
        return subscriber_ids
    
    @staticmethod
    def create_user_subscription( userid, casinoid):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_subscription (userid, casinoid) VALUES (?, ?)", (userid, casinoid))
        conn.commit()
        conn.close()
        return userid
    
    @staticmethod
    def check_user_subscription(userid, casinoid):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_subscription WHERE userid=? AND casinoid=?", (userid, casinoid))
        user_subscription = cursor.fetchone()
        conn.close()
        if user_subscription:
            return True
        return False
    
    @staticmethod
    def remove_user_subscription(userid, casinoid):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user_subscription WHERE userid=? AND casinoid=?", (userid, casinoid))
        conn.commit()
        conn.close()
        return userid
