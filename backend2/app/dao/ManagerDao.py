from app import get_db_connection
from app.models.Manager import Manager
import uuid

class ManagerDao:
    def get_manager_by_id(self, manager_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        # join manager_salary, and user tables to only have entries which are in both tables
        cursor.execute("SELECT * FROM manager_salary JOIN users ON manager_salary.id=users.id WHERE manager_salary.id=?", (manager_id,))
        manager = cursor.fetchone()
        print(manager)
        # # now get the list of casinos for the manager 
        # cursor.execute("SELECT * FROM casinos WHERE manager_id=?", (manager_id,))
        # casinos = cursor.fetchall()
        casinos = []
        conn.close()
        # convert manager to Manager object
        if manager:
            return Manager(manager[0], manager[1], casinos)
        return None
    
    def create_manager(self, username, email, age, password, salary):
        id = "manager_" + str(uuid.uuid4())
        # create a Manager Object
        manager = Manager(id, salary)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (id, username, email, age, password) VALUES (?, ?, ?, ?, ?)", (manager.get_id(), username, email, age, password))
        cursor.execute("INSERT INTO manager_salary (id, salary) VALUES (?, ?)", (manager.get_id(), salary))
        conn.commit()
        conn.close()
        return manager.get_id()

