"""Tests for data_loader module"""
import pytest
import pandas as pd
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from data_loader import load_synthetic_data


def test_load_synthetic_data_default():
    """Test loading synthetic data with default parameters"""
    data = load_synthetic_data()
    
    assert isinstance(data, pd.DataFrame)
    assert 'price' in data.columns
    assert len(data) == 1000
    assert data['price'].dtype in [float, 'float64']


def test_load_synthetic_data_custom_rows():
    """Test loading synthetic data with custom number of rows"""
    n_rows = 500
    data = load_synthetic_data(n_rows=n_rows)
    
    assert isinstance(data, pd.DataFrame)
    assert len(data) == n_rows
    assert 'price' in data.columns


def test_synthetic_data_has_price_column():
    """Test that synthetic data contains price column"""
    data = load_synthetic_data()
    
    assert 'price' in data.columns
    assert not data['price'].isna().any()


def test_synthetic_data_price_values():
    """Test that price values are reasonable"""
    data = load_synthetic_data()
    
    # Price should be numeric
    assert pd.api.types.is_numeric_dtype(data['price'])
    
    # Price should have some variation (not all same values)
    assert data['price'].std() > 0

