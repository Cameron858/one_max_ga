from typing import Callable, Optional
from one_max_ga.population import Population
from one_max_ga.selectors import Selector


class GeneticAlgorithm:

    def __init__(
        self,
        pop_size: int,
        chromosome_length: int,
        crossover_rate: float,
        mutation_rate: float,
        selector: Selector,
        terminator: Optional[Callable[[Population, int], bool]] = None,
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
        self.selector = selector
        self.terminator = terminator or self._default_terminator
        self.max_generations = max_generations

        # init default attrs
        self.population = None
        self.current_generation = 0

    def _default_terminator(self, generation: int) -> bool:
        """
        Default terminator.

        Terminates the algorithm after given 'max_generations'
        """
        return generation >= self.max_generations

    def initialise_population(self):
        self.population = Population(self.pop_size, self.chromosome_length)
