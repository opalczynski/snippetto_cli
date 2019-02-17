import click

from snipetto.snippets.services import SnippetsService


@click.group('snippets')
def snippets():
    pass


@snippets.command()
def list():
    SnippetsService.list()


@snippets.command()
@click.argument('name', type=str)
def detail(name):
    SnippetsService.detail(name)


@snippets.command()
@click.argument('name', type=str)
def delete(name):
    SnippetsService.delete(name)


@snippets.command()
@click.argument('slug', type=str)
@click.argument('tags', type=str)
@click.argument('snippet', type=click.File('r'))  # for now auto adding just from the file
def create(slug, tags, snippet):
    SnippetsService.create(slug, tags, snippet)
