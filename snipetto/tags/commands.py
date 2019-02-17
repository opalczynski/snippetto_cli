import click

from snipetto.tags.services import TagsService


@click.group('tags')
def tags():
    pass


@tags.command()
def list():
    TagsService.list()


@tags.command()
@click.argument('name', type=str)
def detail(name):
    TagsService.detail(name)


@tags.command()
@click.argument('name', type=str)
def delete(name):
    TagsService.delete(name)
