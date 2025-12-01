# Evolutionary Strategy Research Project

A research framework for evolving trading strategies using genetic programming and evolutionary algorithms. This project provides tools for automatically discovering strategy building blocks, running reproducible experiments, and evaluating candidate strategies through backtesting.

## 🎯 Goals

- **Automatic Strategy Discovery**: Discover strategy building blocks automatically using genetic programming
- **Reproducible Experiments**: Versioned data and environment capture for consistent results
- **Latency-Aware Backtesting**: Backtesting primitives that account for execution latency
- **Clear Promotion Path**: Structured workflow from evolution → out-of-sample testing → stress testing → candidate pool

## ✨ Features

- Genetic programming engine for strategy evolution
- Synthetic data generation for testing
- Docker containerization for easy deployment
- Distributed computing support via Ray
- Modular architecture for easy extension

## 📋 Requirements

- Python 3.11+
- See `requirements.txt` for full dependency list

## 🚀 Quick Start

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd proj_esr
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Basic Usage

#### Run Evolution

Evolve trading strategies using genetic programming:
```bash
python src/app.py --mode evolve --generations 50 --population 50
```

#### Evaluate a Candidate Strategy

Evaluate a saved candidate strategy:
```bash
python src/app.py --mode evaluate --candidate outputs/hof/best_candidate.pkl
```

### Command Line Options

- `--mode`: Operation mode - `evolve` or `evaluate` (required)
- `--generations`: Number of evolution generations (default: 50)
- `--population`: Population size for evolution (default: 50)
- `--candidate`: Path to candidate file for evaluation (required for evaluate mode)

## 🐳 Docker Usage

### Build the Docker Image

```bash
docker build -t evolutionary-strategy:latest .
```

### Run Evolution in Docker

```bash
docker run --rm evolutionary-strategy:latest python src/app.py --mode evolve --generations 50 --population 100
```

### Custom Docker Run

```bash
docker run --rm -v $(pwd)/outputs:/app/outputs evolutionary-strategy:latest python src/app.py --mode evolve --generations 100 --population 200
```

## 📁 Project Structure

```
proj_esr/
├── src/
│   ├── app.py              # Main application entry point
│   ├── gp_engine.py        # Genetic programming evolution engine
│   └── data_loader.py      # Data loading utilities
├── examples/               # Example scripts and notebooks
├── outputs/               # Generated outputs and results
│   └── hof/              # Hall of Fame (best candidates)
├── tests/                 # Unit tests
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🔧 Development

### Running Tests

```bash
pytest -v tests/
```

### Code Formatting

Format code with Black:
```bash
black src/ tests/ examples/
```

### Linting

Run Flake8 for code quality checks:
```bash
flake8 src/ tests/ examples/
```

## 📊 Workflow

1. **Evolution**: Run genetic programming to evolve trading strategies
2. **Evaluation**: Test evolved candidates on historical data
3. **Out-of-Sample Testing**: Validate strategies on unseen data
4. **Stress Testing**: Test strategies under various market conditions
5. **Candidate Pool**: Store promising strategies for further analysis

## 🛠️ Dependencies

Key dependencies include:
- `numpy` - Numerical computing
- `pandas` - Data manipulation
- `ray` - Distributed computing framework
- `matplotlib` - Visualization
- `cloudpickle` - Serialization
- `pytest` - Testing framework

See `requirements.txt` for the complete list.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

[Specify your license here]

## 🔗 Resources

- [Genetic Programming Documentation](https://en.wikipedia.org/wiki/Genetic_programming)
- [Ray Documentation](https://docs.ray.io/)
- [Evolutionary Algorithms](https://en.wikipedia.org/wiki/Evolutionary_algorithm)

## 📧 Contact

[Add your contact information or project maintainer details]

---

**Note**: This is a research project. Use at your own risk for trading decisions.

