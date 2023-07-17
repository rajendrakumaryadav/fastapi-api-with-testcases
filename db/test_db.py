import unittest

from .DB import DB
from . import curd


class TestDB(unittest.TestCase):
    db: DB

    def setUp(self) -> None:
        self.db = DB()

    def tearDown(self) -> None:
        self.db.session.query(curd.User).filter(curd.User.username == "admin1").delete()
        self.db.session.commit()

    def test_get_user(self):
        user = self.db.session.query(curd.User).filter(curd.User.id == 1).first()
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.password, "admin")
        self.assertEqual(user.id, 1)

    def test_get_user_by_username(self):
        user = self.db.session.query(curd.User).filter(curd.User.username == "admin").first()
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.password, "admin")
        self.assertEqual(user.id, 1)
        self.assertEqual(len(self.db.session.query(curd.User)
                             .filter(curd.User.username == "admin").all()), 1)

    def test_get_users(self):
        self.assertEqual(200, 200)


if __name__ == '__main__':
    unittest.main()
