# Snipetto CLI 

Simple CLI to handle Snipetto Service for storing code snippets.

## Overview

* Snippetto CLI allows you to create snippets directly from files in terminal.
* Snippetto by default makes your snippets available only for you.

## Installation

I will add this to `pypi` soon, but currently simple:

    pip3 install https://github.com/opalczynski/snippetto_cli/archive/master.zip 

## Build

| Build  | Status  | 
|---|---|
| CircleCI  | [![CircleCI](https://circleci.com/gh/opalczynski/snippetto_cli.svg?style=svg)](https://circleci.com/gh/opalczynski/snipetto_cli) |


## Commands

At the beginning you will be asked to setup your account, I only need username
and a password to make this work. Follow the instructions on terminal.

> Note use --help if you are not sure how command work.

* Add snippet - allow to add new snippet

      snippetto add --slug myfirstsnippet --tags=click,python --desc "example add for README" --file setup.py 

You can also specify `--start` and `--end` to tell which fragment of the file
should be used as a snippet.

* List snippets

      snippetto list

Here you can use `--skip-snippet` do make a quick overview.

* Search snippets

      snippetto search --slug myfirstsnippet
      snippetto search --slug myfirstsnippet --tags python
      snippetto search --tags python,click

Search works on two parameters: `slug` or `tags` or both

Tags filter is `OR-like` - you will get all snippets with `python` or `click` 
tags;

* Edit snippet

      snippetto edit myfirstsnippet --desc "New description"

Following fields can be edited: tags, description, file (snippet)

* Get snippet 

      snippetto get myfirstsnippet
      snippetto get --snippet-only myfirstsnippet
      
Here interesting functionality is `--snippet-only`, this way you can redirect
stream and create file with the code:

    snippetto get --snippet-only myfirstsnippet > myfirstsnippet.py

* Delete snippet - will remove snippet from you collection.

      snippetto delete  myfirstsnippet

* List tags - will list all tags collected in system.

      snippetto tags list

## Stack

Snippetto CLI is build based on:

* [click](https://click.palletsprojects.com/en/7.x/) 
* [requests](http://docs.python-requests.org/en/master/)

## Notes

> Working only with python3
