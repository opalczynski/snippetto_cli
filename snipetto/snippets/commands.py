import click

from snipetto.snippets.services import SnippetsService


@click.command(name='get')
@click.argument('name', type=str)
def get_snippet(name):
    SnippetsService.get_snippet(name)


@click.command(name='delete')
@click.argument('name', type=str)
def delete_snippet(name):
    SnippetsService.delete_snippet(name)


@click.command(name='add')
@click.option('--slug', 'slug', type=str)
@click.option('--tags', 'tags', type=str)
@click.option('--file', 'file', type=click.File('r'))  # for now auto adding just from the file
def add_snippet(slug, tags, file):
    SnippetsService.add_snippet(slug, tags, file)


@click.command(name='edit')
@click.argument('slug', type=str)
@click.option('--tags', 'tags', type=str)
@click.option('--file', 'file', type=click.File('r'))  # for now auto adding just from the file
def edit_snippet(slug, tags, file):
    SnippetsService.edit_snippet(slug, tags, file)


@click.command(name='search')
@click.option('--tags', 'tags', type=str)
@click.option('--slug', 'slug', type=str)  # for now auto adding just from the file
def search_snippet(slug, tags):
    SnippetsService.search_snippet(slug, tags)


