from setuptools import setup

setup(
	name="trooper",
	version="1.0",
	py_modules=['troop'],
	include_package_data=True,
	install_requires=[
		'click',
		'colorama',
	],
	entry_points='''
		[console_scripts]
		troop=troop:cli
	''',
)