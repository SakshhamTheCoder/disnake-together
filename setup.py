from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Natural Language :: English',
    'Topic :: Internet',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name = 'disnake-together',
    version = '1.0.0',
    description = "A 3rd party solution to use discord's VC Party Games feature with disnake",
    long_description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url = '',
    author = 'Joshua Lowe',
    author_email = 'josh@edublocks.org',
    license = 'MIT',
    classifiers = classifiers,
    keywords = 'calculator',
    packages = find_packages(),
    install_requires = ['']
)