from abc import ABC, abstractmethod

from one_max_ga.population import Population


class Terminator(ABC):

    @abstractmethod()
    def terminate(self, population: Population, generation: int) -> bool:
        pass


class MaxGenerationsTerminator(Terminator):

    def __init__(self, max_generations: int):
        self.max_generations = max_generations
        super().__init__()

    def terminate(self, population, generation):
        """Return `True` if the given generation is equal to or greater than the `max_generations`, otherwise returns `False`."""
        if generation >= self.max_generations:
            return True

        return False
