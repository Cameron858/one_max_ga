import logging
import random
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

        self.generation = 0

        # attatch logger
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """"""
        self.generation = 0

        # generate initial population
        population = Population(self.pop_size, self.chromosome_length)

        # either terminate at max_generations or when the given Terminator dictates so.
        while (self.generation < self.max_generations) and (
            not self.terminator.terminate(
                population=population, generation=self.generation
            )
        ):
            self.logger.info(f"Running generation {self.generation + 1}")

            population.sort_by_fitness()

            # log best member of the population
            self.logger.info(f"Best member: {population.best()}")

            # use selection_rate to determine top N% of chromosomes that will be used to breed the next generation
            # ensure the rounded int is in the range [2, pop_size]
            top_n_chromosomes = max(
                2, min(self.pop_size, round(self.pop_size * self.selection_rate))
            )

            parent_pool = population[:top_n_chromosomes]

            # breed new population
            new_population = []
            while len(new_population) < self.pop_size:
                # decide on crossover or direct reproduction
                # crossover
                if random.random() < self.crossover_rate:
                    parent_1, parent_2 = parent_pool.random(k=2)
                    child = parent_1.crossover(parent_2)
                # direct
                else:
                    parent = parent_pool.random()[0]
                    child = parent.direct()

                child.mutate(chance=self.mutation_rate)
                new_population.append(child)

            population = Population.from_chromosomes(new_population)
            self.generation += 1

        # log termination reason
        if self.generation >= self.max_generations:
            self.logger.info("Terminating due to reaching max generations.")
        else:
            self.logger.info(
                f"Terminating due to custom terminator condition: {self.terminator.reason}"
            )
