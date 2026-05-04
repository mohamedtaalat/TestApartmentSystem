import requests


class TestLoginEndpoint:
    def test_sign_in(self):
        self.url ="http://localhost:5000/api/auth/login"
        response = requests.post(self.url,json = {"email":"Test10@test.com","password":"123456"})
        assert response.status_code == 200

    def test_sign_in_without_email(self):
        self.url ="http://localhost:5000/api/auth/login"
        response = requests.post(self.url,json = {"email":"","password":"123456"})
        assert response.status_code == 400

    def test_sign_in_without_password(self):
        self.url ="http://localhost:5000/api/auth/login"
        response = requests.post(self.url,json = {"email":"Test10@test.com","password":""})
        assert response.status_code == 400

    def test_sign_in_without_email_and_password(self):
        self.url ="http://localhost:5000/api/auth/login"
        response = requests.post(self.url,json = {"email":"","password":""})
        assert response.status_code == 400