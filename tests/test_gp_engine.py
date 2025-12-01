"""Tests for gp_engine module"""
import pytest
import sys
import os
import pandas as pd

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from gp_engine import EvolutionEngine
from data_loader import load_synthetic_data


def test_evolution_engine_initialization():
    """Test EvolutionEngine can be initialized"""
    data = load_synthetic_data(n_rows=100)
    engine = EvolutionEngine(data, population=50)
    
    assert engine.data is not None
    assert engine.population == 50
    assert isinstance(engine.data, pd.DataFrame)


def test_evolution_engine_custom_population():
    """Test EvolutionEngine with custom population size"""
    data = load_synthetic_data(n_rows=100)
    engine = EvolutionEngine(data, population=100)
    
    assert engine.population == 100


def test_evolution_engine_evolve_method():
    """Test that evolve method can be called"""
    data = load_synthetic_data(n_rows=100)
    engine = EvolutionEngine(data, population=10)
    
    # Should not raise an exception
    engine.evolve(generations=5)


def test_evolution_engine_evaluate_method():
    """Test that evaluate method can be called"""
    data = load_synthetic_data(n_rows=100)
    engine = EvolutionEngine(data, population=10)
    
    # Should not raise an exception (even if file doesn't exist)
    # This is a placeholder test
    try:
        engine.evaluate("nonexistent_file.pkl")
    except FileNotFoundError:
        pass  # Expected for placeholder implementation

