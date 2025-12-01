# Evolutionary Strategy Research Project - GitHub Push-Ready Layout with CI, Linting, and Badge

The project scaffold now includes a CI badge in the README and optional Docker build/test in CI.

---

# README.md (updated with CI badge)

```markdown
# Evolutionary Strategy Research Project

[![Python CI](https://github.com/<your-username>/evolutionary-strategy-research/actions/workflows/ci.yml/badge.svg)](https://github.com/<your-username>/evolutionary-strategy-research/actions/workflows/ci.yml)

Scaffold for evolving trading strategies using genetic programming and evolutionary search.

## Goals
- Discover strategy building blocks automatically
- Provide reproducible experiments (versioned data + env capture)
- Include latency-aware backtesting primitives
- Provide a clear promotion path: evolve -> OOS test -> stress test -> candidate pool

## Quickstart
1. Create a virtualenv and install requirements:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run a smoke evolution on synthetic data:

```bash
python src/app.py --mode evolve --generations 50 --population 50
```

3. Evaluate the saved candidate:

```bash
python src/app.py --mode evaluate --candidate outputs/hof/best_candidate.pkl
```

See `examples/` for more advanced scripts.
```

---

# .github/workflows/ci.yml (optional Docker build/test added)

```yaml
name: Python CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python 3.11
      uses: actions/setup-python@v4
      with:
        python-version: 3.11

    - name: Install dependencies
      run: |
        python -m venv venv
        source venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
        pip install black flake8

    - name: Run Tests
      run: |
        source venv/bin/activate
        pytest -v tests/

    - name: Run Linting (Black + Flake8)
      run: |
        source venv/bin/activate
        black --check src/ tests/ examples/
        flake8 src/ tests/ examples/

    - name: Docker Build Test (optional)
      run: |
        docker build -t evolutionary-strategy:ci .
        docker run --rm evolutionary-strategy:ci python src/app.py --mode evolve --generations 1 --population 5
```

---

# Notes

- Replace `<your-username>` in README badge URL with your GitHub username.
- The Docker build/test ensures that the Dockerfile is valid and the app can run inside a container.
- CI now runs tests, linting, and optional Docker build/test on every push and PR.
