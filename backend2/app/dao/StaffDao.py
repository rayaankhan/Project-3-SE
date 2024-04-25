from app import get_db_connection
import uuid

class StaffDao:

    def update_assignedId(self, staff_id, assigned_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE staff SET currentassignedid=? WHERE staffid=?", (assigned_id, staff_id))
        conn.commit()
        conn.close()
        return staff_id
    
    def get_staff_name(self, staff_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM staff WHERE staffid = ?", (staff_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0]
    
    def update_staff_status(self, staff_id, assigned_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE staff SET currentassignedid=? WHERE staffid=?", (assigned_id, staff_id))
        conn.commit()
        conn.close()
        return staff_id