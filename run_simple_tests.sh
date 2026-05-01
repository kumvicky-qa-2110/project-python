#!/bin/bash
# Simple test runner without pytest

echo "========================================="
echo "Running Simple Python Tests"
echo "========================================="
echo ""

# Activate virtual environment
source .venv/bin/activate

echo "Test 1: Running helloWorld.py"
echo "------"
python python_programming/helloWorld.py
echo ""

echo "Test 2: Importing main Flask app"
echo "------"
python -c "from main import app; print('✓ Flask app imported successfully')"
echo ""

echo "Test 3: Testing Flask app route"
echo "------"
python -c "from main import app; client = app.test_client(); resp = client.get('/'); print(f'✓ Route /: {resp.status_code} - {resp.data.decode()}')"
echo ""

echo "========================================="
echo "Tests complete!"
echo "========================================="
