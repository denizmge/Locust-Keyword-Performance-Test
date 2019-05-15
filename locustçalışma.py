from locust import HttpLocust,TaskSet,task

class Keyword(TaskSet):
    @task
    def func(self):
        with self.client.get("/arama?adult=&q=iPhone",catch_response=True) as response:
            if response.status_code == 200:
                response.success()

class test (HttpLocust):
    host = "https://www.n11.com"
    task_set = Keyword
    min_wait = 4000
    max_wait = 8000
