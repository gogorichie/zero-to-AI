#!/bin/bash

# This script executes the complete set of unit tests,
# with code coverage reporting.
# Chris Joakim, 3Cloud/Cognizant, 2026

echo "========== Activating the virtual environment =========="
source .venv/bin/activate
python --version

rm -rf htmlcov

echo "========== Executing unit tests with code coverage =========="
pytest -v --cov=src/ --cov-report html tests/

echo "========== Running pylint =========="
pylint --errors-only *.py src
