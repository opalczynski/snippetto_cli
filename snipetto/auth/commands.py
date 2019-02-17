
import click

from snipetto.auth.services import AuthService


@click.group('auth')
def auth():
    pass


@auth.command()
@click.argument('login')
@click.argument('password')
def login(user_login, user_password):
    AuthService.login(user_login, user_password)

@auth.command()
def logouot():
    AuthService.logout()
