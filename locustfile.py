from locust import HttpUser, task, between


class DeviceUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def create_device(self):
        self.client.post("/devices", json={"name": "test_device", "user_id": None})

    @task(3)
    def add_measurement(self):
        self.client.post("/devices/1/measurements", json={"x": 1.5, "y": 2.3, "z": 0.8})

    @task(2)
    def get_stats(self):
        self.client.get("/devices/1/stats")