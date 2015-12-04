import click
from colorama import Fore, Back, Style
import os

@click.command()
@click.argument('username')
@click.argument('repo')
def cli(username, repo):
	'''Trooper quickly puts any folder your in up on Github.'''
	os.system('git init')
	os.system('git remote add origin http://github.com/%s/%s' % (username, repo))

if __name__ == '__main__':
	cli()
