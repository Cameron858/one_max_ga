from .chromosome import OneMaxChromosome
from .population import Population
from abc import ABC, abstractmethod


class Selector(ABC):

    @abstractmethod
    def select(self, population: Population) -> Population:
        pass


class ElitismSelector(Selector):

    def __init__(self, elite_size: int):
        self.elite_size = elite_size

    def select(self, population: Population) -> Population:

        sorted_chromosomes = population.sort_by_fitness()
        elite_chromosomes = sorted_chromosomes[: self.elite_size]
        elite_pop = Population.from_chromosomes(elite_chromosomes)

        return elite_pop
