#!/bin/bash

find src/prettiprint -type f -name "*.py" -exec pylint -E {} +
