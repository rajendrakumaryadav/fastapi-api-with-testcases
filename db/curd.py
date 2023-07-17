from typing import Dict

import sqlalchemy.exc
from sqlalchemy.orm import Session

from .UserModel import User
from . import DB


class UserCRUD:
    """
    User CRUD operations
    """
    session: DB

    def __init__(self, session: Session = None):
        """
        :type session: Session
        :param session: SQLAlchemy session
        """
        self.session = DB.DB()

    def get_user(self, user_id: int):
        return self.session.session.query(User).filter(User.id == user_id).first()

    def get_user_by_username(self, username: str):
        return self.session.session.query(User).filter(User.username == username).first()

    def get_users(self, skip: int = 0, limit: int = 100):
        return self.session.session.query(User).offset(skip).limit(limit).all()

    def create_user(self, user: User) -> User | Dict[str, str]:
        """
        :type user: User
        :param user:
        :return: Success or error message
        """
        try:
            self.session.session.add(user)
            self.session.session.commit()
            self.session.session.refresh(user)
            return user
        except sqlalchemy.exc.IntegrityError:
            self.session.session.rollback()
            return {'message': 'User already exists'}
        except sqlalchemy.exc.InvalidRequestError:
            self.session.session.rollback()
            return {'message': 'User already exists'}

    def update_user(self, user: User):
        """
        :type user: User
        :param user:
        :return: User
        """
        self.session.session.query(User).filter(User.id == user.id).update(user)
        self.session.session.commit()
        return user

    def delete_user(self, user: User):
        """
        :type user: User
        :param user:
        :return: User
        """
        self.session.session.query(User).filter(User.id == user.id).delete()
        self.session.session.commit()
        return user
