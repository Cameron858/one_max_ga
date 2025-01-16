from one_max_ga.population import Population
from one_max_ga.terminators import Terminator, MaxGenerationsTerminator


class GeneticAlgorithm:

    def __init__(
        self,
        pop_size: int,
        chromosome_length: int,
        crossover_rate: float,
        mutation_rate: float,
        terminator: Terminator = None,
        max_generations: int = 100,
    ):

        # validate rates
        if not (0 <= crossover_rate <= 1):
            raise ValueError(f"'crossover_rate' must be between 0 and 1")
        if not (0 <= mutation_rate <= 1):
            raise ValueError(f"'mutation_rate' must be between 0 and 1")

        self.pop_size = pop_size
        self.chromosome_length = chromosome_length
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations

        # init default attrs
        self.population = None
        self.current_generation = 0

        if terminator:
            self.terminator = terminator
        else:
            self.terminator = MaxGenerationsTerminator(self.max_generations)

    def initialise_population(self):
        self.population = Population(self.pop_size, self.chromosome_length)
