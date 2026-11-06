from locust import HttpUser, task, between

class Personaje(HttpUser):
    host = "https://thesimpsonsapi.com"
    wait_time = between(2, 5)

    @task
    def consultar_personaje(self):
        self.client.get("/api/characters")