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
        return self.chromosomes[indices]

    def sort_by_fitness(
        self, reverse: bool = True, inplace: bool = False
    ) -> list[OneMaxChromosome]:

        sorted_chromosomes = sorted(
            self.chromosomes, key=lambda c: c.fitness(), reverse=reverse
        )

        if inplace:
            self.chromosomes = sorted_chromosomes

        return sorted_chromosomes

    @classmethod
    def from_chromosomes(cls, chromosomes: list[OneMaxChromosome]) -> Self:

        pop = Population(size=len(chromosomes), chromosome_length=chromosomes[0].length)
        pop.chromosomes = chromosomes

        return pop


if __name__ == "__main__":

    p = Population(10, 5)
