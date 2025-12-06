


Python Password Generator

A fast, secure, and compact password generator module written in Python.
It supports cryptographically strong passwords and memorable passphrases, with options for length, separators, and special characters. The core logic stays under 50 lines of code.

Overview

This module provides two main styles of password generation:

1. Strong passwords – fully random, cryptographically secure, ideal for logins, API keys, or secrets.


2. Memorable passphrases – easier to remember, built from random dictionary words with optional numbers.



The module uses Python’s secrets library for secure randomness and does not require any external dependencies.

Features

Cryptographically secure randomness (via secrets)

Custom length (default 16 characters)

Optional special characters

Memorable passphrases with configurable:

number of words

separator character

optional trailing number


Works as both a CLI tool and an importable Python module

Single-file implementation, easy to read and extend


Installation

Clone the repository:

git clone git@github-dorian:dorian-sotpyrc/python-password-generator.git
cd python-password-generator

No additional packages are required beyond the Python standard library.

Usage

Run as a CLI tool

From the project folder:

python3 password_gen.py

You will be prompted to choose:

Password type: strong or memorable

Length (for strong passwords)

Separator and trailing number option (for memorable passwords)


Use as a Python module

from password_gen import strong_password, memorable_password

# Example: strong 24-character password without special characters
print(strong_password(length=24, special=False))

# Example: 5-word memorable passphrase separated by dots, with a trailing number
print(memorable_password(words=5, sep=".", number=True))

Project Structure

python-password-generator/
├── password_gen.py   # Main module and CLI logic
└── README.md         # Project documentation

Security Notes

Uses secrets.choice instead of random.choice for all random selection.

Keeps the implementation small and auditable.

The internal word list can be extended to increase variety if needed.


SEO Keywords

python password generator, secure password generator, memorable password python, passphrase generator python, cryptographically secure password python, python secrets module example, password generator CLI python.

License

This project is released under the MIT License.

Related PLEX Content

A PLEX article and Medium post will be linked here when published.
For more tools and tutorials, visit: https://plexdata.online
