# Testing Guide

This document explains how to test the Evolutionary Strategy Research project.

## Prerequisites

1. Install dependencies (including pytest):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running Tests

### Run All Tests

```bash
# Activate virtual environment first
source venv/bin/activate

# Run all tests
pytest tests/ -v

# Or with more detailed output
pytest tests/ -v -s
```

### Run Specific Test Files

```bash
# Test data loader only
pytest tests/test_data_loader.py -v

# Test evolution engine only
pytest tests/test_gp_engine.py -v

# Test app CLI only
pytest tests/test_app.py -v
```

### Run Specific Tests

```bash
# Run a specific test function
pytest tests/test_data_loader.py::test_load_synthetic_data_default -v
```

### Run Tests with Coverage

```bash
# Install coverage first
pip install pytest-cov

# Run tests with coverage report
pytest tests/ --cov=src --cov-report=html --cov-report=term
```

## Manual Testing

### Test the Application Directly

1. **Test Evolution Mode:**
```bash
python3 src/app.py --mode evolve --generations 5 --population 10
```

2. **Test Evaluate Mode:**
```bash
# First create a dummy candidate file (for testing)
python3 src/app.py --mode evaluate --candidate outputs/hof/test_candidate.pkl
```

3. **Test Help:**
```bash
python3 src/app.py --help
```

### Test Data Loading

```bash
python3 -c "import sys; sys.path.insert(0, 'src'); from data_loader import load_synthetic_data; data = load_synthetic_data(); print(data.head()); print('Shape:', data.shape)"
```

### Test Docker Build

```bash
# Build the Docker image
docker build -t evolutionary-strategy:test .

# Run a quick test in Docker
docker run --rm evolutionary-strategy:test python src/app.py --mode evolve --generations 1 --population 5
```

## Test Structure

```
tests/
├── __init__.py              # Package marker
├── test_data_loader.py      # Tests for data loading
├── test_gp_engine.py        # Tests for evolution engine
└── test_app.py              # Tests for CLI interface
```

## Continuous Integration

Tests can be run in CI/CD pipelines. See `.github/workflows/ci.yml` for GitHub Actions configuration.

## Writing New Tests

When adding new functionality, add corresponding tests:

1. Create test file in `tests/` directory
2. Name it `test_<module_name>.py`
3. Use pytest fixtures and assertions
4. Run tests to ensure they pass

Example:
```python
def test_new_feature():
    """Test description"""
    result = new_function()
    assert result is not None
    assert result == expected_value
```

