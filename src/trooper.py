import click
from colorama import Fore, Style
import sys
import os

def pop():
	sys.stdout.write(Style.BRIGHT + '==> ' + Style.RESET_ALL)

@click.command()
@click.argument('git_username')
@click.argument('repository_name')
@click.option('--branch', '-b', default='master', help='Changes branch default is "master".')
def cli(git_username, repository_name, branch):
	os.system('touch ~/git_out')
	pop()
	os.system('git init > ~/git_out')
	print(Style.BRIGHT + Fore.GREEN + 'Initializing Git repository...' + Style.RESET_ALL + Fore.RESET)
	pop()
	os.system('git remote add origin https://github.com/%s/%s > ~/git_out' % (git_username, repository_name))
	print(Style.BRIGHT + Fore.GREEN + 'Adding remote origin...' + Style.RESET_ALL + Fore.RESET)
	pop()
	os.system('git add . > ~/git_out')
	print(Style.BRIGHT + Fore.GREEN + 'Adding files...' + Style.RESET_ALL + Fore.RESET)
	pop()
	os.system('git commit -m "Trooper commit." > ~/git_out')
	print(Style.BRIGHT + Fore.GREEN + 'Commiting files...' + Style.RESET_ALL + Fore.RESET)
	pop()
	os.system('git push origin %s > ~/git_out' % (branch))
	print(Style.BRIGHT + Fore.GREEN + 'Finalizing...' + Style.RESET_ALL + Fore.RESET)
	pop()
	os.system('rm ~/git_out')
	print(Style.BRIGHT + Fore.GREEN + 'Cleaning up...' + Style.RESET_ALL + Fore.RESET)


if __name__ == '__main__':
	cli()