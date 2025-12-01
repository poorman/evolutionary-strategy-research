"""Tests for app.py command-line interface"""
import pytest
import sys
import os
import subprocess

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def test_app_help():
    """Test that app shows help message"""
    result = subprocess.run(
        ['python', 'src/app.py', '--help'],
        capture_output=True,
        text=True,
        cwd=os.path.join(os.path.dirname(__file__), '..')
    )
    
    assert result.returncode == 0 or result.returncode == 2  # Help can exit with 2
    assert 'mode' in result.stdout or 'mode' in result.stderr


def test_app_evolve_mode():
    """Test that evolve mode can be called"""
    result = subprocess.run(
        ['python', 'src/app.py', '--mode', 'evolve', '--generations', '1', '--population', '5'],
        capture_output=True,
        text=True,
        cwd=os.path.join(os.path.dirname(__file__), '..')
    )
    
    # Should not crash
    assert result.returncode == 0
    assert 'evolution' in result.stdout.lower() or 'generations' in result.stdout.lower()


def test_app_evaluate_mode_requires_candidate():
    """Test that evaluate mode requires candidate parameter"""
    result = subprocess.run(
        ['python', 'src/app.py', '--mode', 'evaluate'],
        capture_output=True,
        text=True,
        cwd=os.path.join(os.path.dirname(__file__), '..')
    )
    
    # Should show error about missing candidate
    assert 'candidate' in result.stdout.lower() or 'candidate' in result.stderr.lower()

