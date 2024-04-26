from locust import task, between, events, SequentialTaskSet, HttpUser
import uuid
import random
import time

class LoadTestingUser(SequentialTaskSet):
    access_token = None
    manager_access_token = None
    username = None
    casino_id = None
    casino_id_list = []
    gametable_id_list = []
    userId = None
    
    @task
    def create_user(self):
        # print(1)
        username = "user_" + str(uuid.uuid4())
        self.username = username
        email = username + "@gmail.com"
        age = random.randint(18, 60)
        password = "password"
        response = self.client.post("/users/add", json={"username": username, "email": email, "age": age, "password": password})
        res = response.json()
        if response.status_code == 200:
            # print("User created successfully")
            self.userId = res.get("id")
        # else:
            # print("User creation failed")
    
    @task
    def login(self):
        # print(2)
        username = self.username
        password = "password"
        response = self.client.post("/users/login", json={"username": username, "password": password})
        res = response.json()
        # print(res)
        if response.status_code == 200:
            self.access_token = res.get("access_token")
            # print(self.access_token)
            # print("User logged in successfully")
        # else:
            # print("User login failed")

    @task
    def get_casino_list(self):
        # print(3)
        headers = {"content-type": "application/json", "Authorization": "Bearer " + self.access_token}
        response = self.client.post("/all_casinos", headers=headers)
        res = response.json()
        # print(res)
        if response.status_code == 200:
            self.casino_id_list = res.get("casino_id_list")
            # flatten the list
            self.casino_id_list = [item for sublist in self.casino_id_list for item in sublist]
            # print("Casino list fetched successfully")
        # else:
            # print("Casino list fetch failed")

    @task
    def get_gametables(self):
        # print(4)
        # randomly select a casino from the list
        casino_id = random.choice(self.casino_id_list)
        self.casino_id = casino_id
        # print(casino_id)
        headers = {"content-type": "application/json", "Authorization": "Bearer " + self.access_token}
        response = self.client.post("/casino_info", json=({ "casinoId": casino_id }), headers=headers)
        # print(response)
        res = response.json()
        casino_info = res.get("casino_info")
        # print(casino_info)
        if response.status_code == 200:
            # print("Game tables fetched successfully")
            self.gametable_id_list = casino_info.get("table_id_list")
            # print(self.gametable_id_list)
        # else:
            # print("Game tables fetch failed")

    @task
    def pay_in_casino(self):
        # print(5)
        # randomly select a gametable from the list
        gametable_id = random.choice(self.gametable_id_list)
        headers = {"content-type": "application/json", "Authorization": "Bearer " + self.access_token}
        amt = random.randint(100, 1000)
        response = self.client.post("/wallet/addBalance", json=({ "amount": amt, "strategy": "cash", "currency":"INR"}), headers=headers)
        # if response.status_code == 200:
            # print("Payment successful")
        # else:
            # print("Payment failed")
        
    @task
    def exit_casino(self):
        # print(6)
        headers = {"content-type": "application/json", "Authorization": "Bearer " + self.access_token}
        response = self.client.post("/wallet/update", json=({ "amount": 0 }), headers=headers)
        # if response.status_code == 200:
        #     print("Exit successful")

    @task
    def stop(self):
        # print(6)
        self.interrupt()


class CMSUser(HttpUser):
    # execute LoadTestingUser tasks sequentially
    tasks = [LoadTestingUser]
    wait_time = between(1, 2)
    host = "http://localhost:5000"
