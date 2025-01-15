from .chromosome import OneMaxChromosome


class Population:

    def __init__(self, size: int, chromosome_length: int):

        if not isinstance(size, int):
            raise ValueError("'size' must be an integer.")

        self.size = size
        self.chromosomes = [
            OneMaxChromosome(length=chromosome_length) for _ in range(size)
        ]

    def sort_by_fitness(
        self, reverse: bool = True, inplace: bool = False
    ) -> list[OneMaxChromosome]:

        sorted_chromosomes = self.chromosomes.sort(
            key=lambda c: c.fitness(), reverse=reverse
        )

        if inplace:
            self.chromosomes = sorted_chromosomes

        return sorted_chromosomes
