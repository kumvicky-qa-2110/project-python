"""Test cases for main.py Flask app"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_flask_app_imports():
    """Test that main Flask app can be imported"""
    try:
        import main  # noqa: F401
        assert True
    except ImportError as e:
        assert False, f"Failed to import main module: {e}"


def test_flask_app_creation():
    """Test that Flask app is created successfully"""
    from main import app
    assert app is not None
    assert app.name == "main"


def test_flask_hello_world_route():
    """Test the /route returns valid response"""
    from main import app
    
    client = app.test_client()
    response = client.get("/")
    
    assert response.status_code == 200
    assert "Hello" in response.data.decode()
