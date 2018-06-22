#!/bin/sh

python -m unittest discover tests
python -m flake8 bitcoin tests
