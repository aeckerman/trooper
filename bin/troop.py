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
	os.system('git add .')
	os.system('git commit -m "Initial commit."')
	os.system('git push origin master')

if __name__ == '__main__':
	cli()
