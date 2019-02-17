from getpass import getpass

import click

from snipetto.auth.services import AuthService


@click.command()
def configure():
    login = str(input("Username:"))
    password = getpass()
    AuthService.login(login, password)


@click.command()
def logout():
    AuthService.logout()
