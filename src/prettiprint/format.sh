#! /bin/bash
isort --profile black -l 100 .
black -l 100 *.py