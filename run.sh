#!/bin/bash

if [[ $# -gt 0 && "$1" == "test" ]]; then
    python3 tests.py
else
    python3 main.py
fi
