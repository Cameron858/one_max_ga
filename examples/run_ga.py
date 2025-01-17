from one_max_ga import GeneticAlgorithm
import logging

if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    ga = GeneticAlgorithm(
        pop_size=100,
        chromosome_length=10,
        crossover_rate=0.7,
        mutation_rate=0.01,
        max_generations=50,
    )

    ga.run()
