from django.test import TestCase, Client

from .models import Challenge

class TestAll(TestCase):

    def test_register_login_getuser_getchallenge(self):
        client = self.register()
        self.login(client)
        self.get_user(client)
        self.get_challenge(client)
        self.start_challenge(client)

    def register(self):
        client = Client()
        response = client.post('/register', {"email":'test@test.com',
                                            "username":'test',
                                            "password":'1234'})
        self.assertEqual(response.json()["action"], "success")
        return client

#    def test_validate_account(self):
#        client = Client()
#        response = client.get('/validate_account')
#        self.assertEqual(response.json()["action"], "success")

    def login(self, client):
        response = client.post('/login', {"username":'test',
                                         "password":'1234'})
        self.assertEqual(response.json()["action"], "success")

    def test_login_bad_username(self):
        client = Client()
        response = client.post('/login', {"username":"unknow",
                                         "password":"1234"})
        self.assertEqual(response.json()["action"], "failure")

    def get_user(self, client):
        response = client.get('/users/1')
        print(response.json())
        self.assertEqual(response.json()["action"], "success")

    def get_challenge(self, client):
        c = Challenge.objects.create(id=1)
        c.save()
        response = client.get('/challenges/1')
        print(response.json())
        self.assertEqual(response.json()["action"], "success")
        self.assertEqual(response.json()["challenge"]["id"], 1)
        response = client.get('/challenges')
        self.assertEqual(response.json()["action"], "success")
        self.assertEqual(response.json()["challenges"][0]["id"], 1)

    def start_challenge(self, client):
        c = Challenge(name="Exercice 1", description="none", docker_name="ex_1")
        c.save()
        print(c.docker_name)
        response = client.get('/challenges/2/start')
        r = response.json()
        print(r)
        self.assertEqual(r["action"], "success")
        # response = client.get('/challenges/2/stop')
        # print(response.json())
        # self.assertEqual(response.json()["action"], "success")
        
