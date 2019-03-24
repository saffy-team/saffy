from setuptools import setup, find_packages

with open('requirements.txt', 'r') as reqs:
	requirements = [r.strip() for r in reqs.readlines()]

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='Saffy',
	packages=find_packages(),
	version='0.1.4',
	license='MIT',
	description='Signal Analysis Framework For You',
	author='Paweł A. Pierzchlewicz',
	author_email='paul@teacode.io',
	url='https://github.com/PPierzc/Saffy',
	keywords=['python', 'signal', 'analysis', 'EEG', 'neuroinformatics'],
	install_requires=requirements,
	long_description=long_description,
	long_description_content_type="text/markdown",
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	],
)
