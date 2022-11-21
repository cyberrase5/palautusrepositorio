from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 4:
            raise AuthenticationError("Username too short")

        if len(password) < 9:
            raise AuthenticationError("Password too short")

        if username in self._user_repository._users:
            raise AuthenticationError("Username already in use")

        if re.match("^[a-z]+$", password):
            raise AuthenticationError("Password can't be only letters")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
