import random


class OneMaxChromosome:

    def __init__(self, length, genes=None):
        self.length = length

        if genes is None:
            self.genes = [random.randint(0, 1) for _ in range(length)]
        else:
            self.genes = genes

    def __repr__(self):
        return f"OneMaxChromosome(length={self.length}, genes={self.genes})"

    def crossover(self, other):
        pass

    def direct(self):
        pass

    def copy(self):
        pass
