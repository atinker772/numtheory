# numtheory

My first project: number theory functions in Python.

## Install (development)
    python -m venv .venv
    .venv\Scripts\activate
    pip install -e ".[dev]"

## Run tests
    pytest

## Example
    >>> from numtheory import is_prime, gcd
    >>> is_prime(97)
    True
    >>> gcd(48, 18)
    6
