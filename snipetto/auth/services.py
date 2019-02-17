import os

from settings.common import SNIPETTO_ENV_TOKEN_NAME


class AuthService:
    @classmethod
    def login(cls, login, password):
        # login logic here
        token = f'{login} {password}' # real logic soon
        cls.set_token(token)
        return cls.get_token()

    @classmethod
    def logout(cls):
        return cls.set_token('')

    @classmethod
    def get_token(cls):
        return os.environ.get(SNIPETTO_ENV_TOKEN_NAME, '')

    @classmethod
    def set_token(cls, token):
        os.environ[SNIPETTO_ENV_TOKEN_NAME] = token
        return token

    @classmethod
    def get_credentials(cls):
        return {'HTTP_AUTHORIZATION': 'Bearer {}'.format(cls.get_token())}
