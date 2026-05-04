import requests
class TestSignUpEndpoint:
    def test_create_tenant(self):
        self.url = "http://localhost:5000/api/auth/register"
        response = requests.post(url = self.url, json = {
            "name":"Mohamed",
            "email":"Test10@test.com",
            "password":"123456",
            "confirmPassword":"123456",
            "role":"tenant"
        })
        assert response.status_code == 201

    def test_create_owner(self):
        self.url = "http://localhost:5000/api/auth/register"
        response = requests.post(url = self.url, json = {
            "name":"Mohamed",
            "email":"Test9@test.com",
            "password":"123456",
            "confirmPassword":"123456",
            "role":"owner"
        })
        print(response.json())
        assert response.status_code == 201

    def test_get_on_endpoint(self):
        self.url = "http://localhost:5000/api/auth/register"
        response = requests.get(url = self.url)
        assert response.status_code == 400
        assert response.json() ==  "GET not allowed on /register"

    def test_create_user_without_email(self):
        self.url = "http://localhost:5000/api/auth/register"
        response = requests.post(url = self.url, json = {
            "name":"Mohamed",
            "email":"",
            "password":"123456",
            "confirmPassword":"123456",
            "role":"owner"
        })
        assert response.status_code == 400

    def test_create_user_without_password(self):
        self.url = "http://localhost:5000/api/auth/register"
        response = requests.post(url = self.url, json = {
            "name":"Mohamed",
            "email":"Test902392329323897238971239812738912@test.com",
            "password":"",
            "confirmPassword":"",
            "role":"owner"
        })
        assert response.status_code == 400

    def test_create_user_without_name(self):
        self.url = "http://localhost:5000/api/auth/register"
        response = requests.post(url = self.url, json = {
            "name":"",
            "email":"Test213890238219381209381@test.com",
            "password":"123456",
            "confirmPassword":"123456",
            "role":"owner"
        })
        assert response.status_code == 400