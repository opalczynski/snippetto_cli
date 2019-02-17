import click

from snipetto.tags.services import TagsService


@click.group()
def tags():
    pass


@tags.command()
def all():
    TagsService.list_tags()
