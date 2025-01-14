import random
from typing import Literal, Self


class OneMaxChromosome:
    """Represents a chromosome for the One Max Problem."""

    def __init__(self, length, genes=None):

        if not isinstance(length, int) or length < 0:
            raise ValueError("Length must be a positive integer.")

        self.length = length

        if genes is None:
            self.genes = [random.randint(0, 1) for _ in range(length)]
        else:
            self.genes = genes

    def __repr__(self):
        return f"OneMaxChromosome(length={self.length}, genes={self.genes})"

    def crossover(
        self, other: Self, method: Literal["uniform", "single", "two"] = "uniform"
    ) -> Self:
        """
        Perform crossover with another chromosome to produce an offspring.

        Parameters
        ----------
        other : Self
            Another chromosome to mate with.
        method : {'uniform', 'single', 'two'}, optional
            The crossover method to use. Default is 'uniform'.

            - 'uniform': Randomly selects each gene from either parent.
            - 'single': Splits at a single random point and swaps segments.
            - 'two': Splits at two random points and swaps the middle segment.

        Returns
        -------
        Self
            The offspring chromosome.

        Raises
        ------
        ValueError
            If the lengths of the chromosomes do not match or the method is invalid.
        """
        if len(self) != len(other):
            raise ValueError(
                f"Chromosome lengths must match. ({len(self)} != {len(other)})"
            )

        if method not in ["uniform", "single", "two"]:
            raise ValueError(f"method '{method}' is not a valid option.")

        if method != "uniform":
            raise NotImplementedError(f"Method '{method}' has not been implemented.")

        if method == "uniform":
            # randomly select each gene from each parent
            new_genes = [random.choice(genes) for genes in zip(self.genes, other.genes)]

        child = OneMaxChromosome(length=len(new_genes), genes=new_genes)
        return child

    def direct(self) -> Self:
        """
        Create a direct copy of the chromosome.

        Returns
        -------
        Self
            A new OneMaxChromosome instance with the same length and genes as the original.
        """
        child = OneMaxChromosome(length=self.length, genes=self.genes)
        return child

    def mutate(self, chance: float):
        """
        Randomly mutate the genes.

        Parameters
        ----------
        chance : float
            The probability of each gene mutating, between 0 and 1.

        Returns
        -------
        None
            The mutation is applied in-place.

        Raises
        ------
        ValueError
            If `chance` is not between 0 and 1.
        """
        if not (0.0 <= chance <= 1.0):
            raise ValueError("Mutation chance must be between 0 and 1.")

        mutated_genes = []
        for gene in self.genes:
            if random.random() < chance:
                # flip gene i.e. 0 -> 1 and 1 -> 0
                mutated_genes.append(1 - gene)
            else:
                mutated_genes.append(gene)

        self.genes = mutated_genes

    def __len__(self):
        return self.length
