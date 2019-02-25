import click


class Printer:
    """We would like to have snippets very nicely printed in the output."""

    def __init__(self, json_snippet, is_list=False):
        if not is_list:
            self.json_snippet = [json_snippet]
        else:
            self.json_snippet = json_snippet['results']

    def print_message(self, message=None):
        if message:
            click.echo(message)

    def print(self, message=None):
        self.print_message(message=message)
        for json_data in self.json_snippet:
            self.print_separator()
            self.print_header(json_data)
            self.print_snippet(json_data)
            self.print_separator()

    def print_header(self, json_data):
        """
        Basic information goes here:
            * slug
            * created at
            * updated at
            * author
        """
        click.echo("Snippet slug: {}".format(json_data['slug']))
        click.echo("Created at: {}".format(json_data['created_at']))
        click.echo("Updated at: {}".format(json_data['updated_at']))
        click.echo("Author: {}".format(json_data['author']['username']))
        click.echo("Tags: {}".format(
            ', '.join(tag['name'] for tag in json_data['tags']))
        )

    def print_snippet(self, json_data, snippet_only=False):
        if snippet_only:
            click.echo(json_data['snippet'])
        else:
            click.echo('Snippet:')
            click.echo()
            click.echo(json_data['snippet'])

    def print_separator(self):
        click.echo()
        click.echo(79*'-')
        click.echo()
