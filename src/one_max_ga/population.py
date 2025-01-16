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
        new_pop = Population.from_chromosomes(self.chromosomes[indices])
        return new_pop

    def sort_by_fitness(self, reverse: bool = True) -> list[OneMaxChromosome]:

        self.chromosomes.sort(key=lambda c: c.fitness(), reverse=reverse)
        return self.chromosomes

    def random(self, k=1) -> list[OneMaxChromosome]:
        return random.choices(self.chromosomes, k=k)

    @classmethod
    def from_chromosomes(cls, chromosomes: list[OneMaxChromosome]) -> Self:

        pop = Population(size=len(chromosomes), chromosome_length=chromosomes[0].length)
        pop.chromosomes = chromosomes

        return pop


if __name__ == "__main__":

    p = Population(10, 5)
