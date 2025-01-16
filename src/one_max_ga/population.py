import random
from typing import Self
from one_max_ga.chromosome import OneMaxChromosome


class Population:

    def __init__(self, size: int, chromosome_length: int):

        if not isinstance(size, int):
            raise ValueError("'size' must be an integer.")

        self.size = size
        self.chromosomes = [
            OneMaxChromosome(length=chromosome_length) for _ in range(size)
        ]

    def __getitem__(self, indices):

        # from_chromosomes() expects a list
        # single value indexing a list returns the member, NOT in a list
        if isinstance(indices, int):
            new_pop = Population.from_chromosomes([self.chromosomes[indices]])
        else:
            new_pop = Population.from_chromosomes(self.chromosomes[indices])

        return new_pop

    def __len__(self):
        return len(self.chromosomes)

    def sort_by_fitness(self, reverse: bool = True) -> list[OneMaxChromosome]:

        self.chromosomes.sort(key=lambda c: c.fitness(), reverse=reverse)
        return self.chromosomes

    def random(self, k=1) -> list[OneMaxChromosome]:
        if k > len(self):
            raise ValueError("'k' cannot be greater than the population size.")
        return random.sample(self.chromosomes, k=k)

    @classmethod
    def from_chromosomes(cls, chromosomes: list[OneMaxChromosome]) -> Self:

        pop = Population(size=len(chromosomes), chromosome_length=chromosomes[0].length)
        pop.chromosomes = chromosomes

        return pop


if __name__ == "__main__":

    p = Population(10, 5)
