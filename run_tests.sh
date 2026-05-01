#!/bin/bash
# Test runner script

echo "========================================="
echo "Running Python Project Tests"
echo "========================================="
echo ""

# Activate virtual environment
source .venv/bin/activate

echo "Installing test dependencies..."
pip install pytest pytest-cov -q

echo ""
echo "Running tests..."
pytest

echo ""
echo "========================================="
echo "Test run complete!"
echo "========================================="
