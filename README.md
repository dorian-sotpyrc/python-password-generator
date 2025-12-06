# Python Password Generator

A fast, secure, and compact password generator module written in Python.
It supports cryptographically strong passwords and memorable passphrases, with options for length, separators, and special characters. The core logic stays under 50 lines of code.

## Overview

This module provides two main styles of password generation:

- **Strong passwords** – fully random, cryptographically secure, ideal for logins, API keys, or secrets.
- **Memorable passphrases** – easier to remember, built from random dictionary words with optional numbers.

The module uses the Python `secrets` library for secure randomness and requires no external dependencies.

## Features

- Cryptographically secure randomness using `secrets`
- Custom length (default 16)
- Optional special characters
- Memorable passphrases with configurable:
  - number of words
  - separator character
  - optional trailing number
- Works as both a CLI tool and an importable module
- Single-file implementation

## Installation

Clone the repository:

    git clone git@github-dorian:dorian-sotpyrc/python-password-generator.git
    cd python-password-generator

## Usage

### Run as a CLI tool

    python3 password_gen.py

Prompts will ask you for:

- Password type (strong or memorable)
- Length (for strong mode)
- Separator or trailing number (for memorable mode)

### Use as a Python module

    from password_gen import strong_password, memorable_password

    print(strong_password(length=24, special=False))
    print(memorable_password(words=5, sep=".", number=True))

## Project Structure

    python-password-generator/
    ├── password_gen.py
    └── README.md

## Security Notes

- Uses `secrets.choice`, not `random.choice`
- Small, auditable codebase
- Word list can be expanded if desired

## SEO Keywords

python password generator, secure password generator, memorable password python, passphrase generator python, cryptographically secure password python, python secrets module example, password generator CLI python

## License

MIT License

## Related PLEX Content

A PLEX article and Medium post will be linked once published.
More at: https://plexdata.online
