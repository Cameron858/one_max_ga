from .chromosome import OneMaxChromosome


class Population:

    def __init__(self, size: int, chromosome_length: int):

        if not isinstance(size, int):
            raise ValueError("'size' must be an integer.")

        self.size = size
        self.chromosomes = [
            OneMaxChromosome(length=chromosome_length) for _ in range(size)
        ]
