import unittest

from starlette.testclient import TestClient

from .main import app


class TestEndPoint(unittest.TestCase):
    client: TestClient
    name: str
    user1: dict

    def setUp(self) -> None:
        self.name: str = "User"
        self.client = TestClient(app)
        self.user1 = {"username": "admin1", "password": "admin1"}

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

    def test_name(self):
        response = self.client.get(f'/hello/{self.name}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": f"Hello {self.name}"})

    def test_login(self):
        response = self.client.post('/login', data={"username": "admin", "password": "admin"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Login successful"})

        # Testing wrong password or username
        response = self.client.post('/login', data={"username": "admin", "password": "wrong"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Login failed"})
        # self.assertEqual(response.headers['server'], 'uvicorn')

    # Skip this test
    def test_register_exists(self):
        response = self.client.post('/register', data=self.user1,
                                    headers={"Content-Type": "application/x-www-form-urlencoded"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "User already exists"})

    def test_update_password(self):
        response = self.client.put('/update-password',
                                   data={"username": "admin1", "password": "admin1", "new_password": "password"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Password updated successfully"})

    # skip this testcase
    def test_delete_user(self):
        from .db.DB import DB
        from .db.UserModel import User

        db = DB()
        user = db.session.query(User).filter(User.username == "admin1").first()
        # response = self.client.delete(f'/delete-user/{user.}')
        self.assertEqual(200, 200)


if __name__ == '__main__':
    unittest.main()
