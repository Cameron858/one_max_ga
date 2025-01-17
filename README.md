# One-Max Genetic Algorithm

This project implements a Genetic Algorithm to solve the One-Max problem. The goal is to maximize the number of `1`s in a binary chromosome.

Is this over-engineered? Yes. Does it work? I hope so. Did I learn stuff? Yes. 

## Features
- Customizable population size, chromosome length, crossover rate, mutation rate, and selection rate.
- Flexible termination conditions through terminator classes.
- Logging for monitoring algorithm progress and results.

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management. Ensure Poetry is installed on your system:

```bash
pip install poetry
```

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/Cameron858/one_max_ga
cd one-max-ga
```

Install the dependencies:

```bash
poetry install
```

## Usage

Here's an example of how to run the algorithm:

```python
from one_max_ga.algorithm import GeneticAlgorithm

if __name__ == "__main__":
    ga = GeneticAlgorithm(
        pop_size=100,
        chromosome_length=50,
        crossover_rate=0.7,
        mutation_rate=0.01,
        selection_rate=0.2,
        max_generations=100
    )
    ga.run()
```

To run the script using Poetry:

```bash
poetry run python your_script.py
```

## Testing

The project includes tests written with `pytest`, `pytest-mock`. `pytest-cov` is included for coverage reports. To run the tests:

```bash
poetry run pytest
```

## Project Structure

- `src/one_max_ga/`: Source code.
- `tests/`: Tests for the project.