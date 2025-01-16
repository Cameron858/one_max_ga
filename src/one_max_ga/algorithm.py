import logging
from one_max_ga.population import Population
from one_max_ga.terminators import Terminator, MaxGenerationsTerminator


class GeneticAlgorithm:

    def __init__(
        self,
        pop_size: int,
        chromosome_length: int,
        crossover_rate: float,
        mutation_rate: float,
        selection_rate: float = 0.2,
        max_generations: int = 100,
        terminator: Terminator = None,
    ):

        # validate rates
        if not (0 <= crossover_rate <= 1):
            raise ValueError(f"'crossover_rate' must be between 0 and 1")
        if not (0 <= mutation_rate <= 1):
            raise ValueError(f"'mutation_rate' must be between 0 and 1")
        if not (0 <= selection_rate <= 1):
            raise ValueError(f"'selection_rate' must be between 0 and 1")

        self.pop_size = pop_size
        self.chromosome_length = chromosome_length
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.selection_rate = selection_rate
        self.max_generations = max_generations
        # default to terminating at max_generations
        self.terminator = terminator or MaxGenerationsTerminator(max_generations)

        # attatch logger
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """"""
        population = Population(self.pop_size, self.chromosome_length)
        generation = 0

        # either terminate at max_generations or when the given Terminator dictates so.
        while (generation <= self.max_generations) and (
            not self.terminator.terminate(population=population, generation=generation)
        ):
            self.logger.info(f"Running generation {generation + 1}")

            generation += 1

        # log termination reason
        if generation >= self.max_generations:
            self.logger.info("Terminating due to reaching max generations.")
        else:
            self.logger.info(
                f"Terminating due to custom terminator condition: {self.terminator.reason}"
            )
