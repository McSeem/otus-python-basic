#!/bin/bash

python3 init.py
gunicorn --bind 0.0.0.0:5000 wsgi:app