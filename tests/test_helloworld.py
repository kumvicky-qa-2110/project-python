"""Test cases for helloWorld.py"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "python_programming"))


def test_import_helloworld():
    """Test that helloWorld module can be imported"""
    try:
        import helloWorld  # noqa: F401
        assert True
    except ImportError:
        assert False, "Failed to import helloWorld module"


def test_hello_world_execution(capsys):
    """Test that hello world prints correct message"""
    import subprocess
    result = subprocess.run(
        [sys.executable, "python_programming/helloWorld.py"],
        cwd=Path(__file__).parent.parent,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Kumar Vicky" in result.stdout
