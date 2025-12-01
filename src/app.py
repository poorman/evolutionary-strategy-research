import argparse
from gp_engine import EvolutionEngine
from data_loader import load_synthetic_data

def main():
    parser = argparse.ArgumentParser(description="Evolutionary Strategy Research Project")
    parser.add_argument("--mode", choices=["evolve", "evaluate"], required=True)
    parser.add_argument("--generations", type=int, default=50)
    parser.add_argument("--population", type=int, default=50)
    parser.add_argument("--candidate", type=str, default=None)
    args = parser.parse_args()

    data = load_synthetic_data()
    engine = EvolutionEngine(data, population=args.population)

    if args.mode == "evolve":
        engine.evolve(generations=args.generations)
    elif args.mode == "evaluate" and args.candidate:
        engine.evaluate(args.candidate)
    else:
        print("Specify --candidate when using evaluate mode.")

if __name__ == "__main__":
    main()
