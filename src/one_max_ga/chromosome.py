import random
from typing import Literal, Self


class OneMaxChromosome:

    def __init__(self, length, genes=None):
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
        """"""
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
        """"""
        child = OneMaxChromosome(length=self.length, genes=self.genes)
        return child

    def mutate(self, chance: float):
        """"""
        mutated_genes = []
        for gene in self.genes:
            if random.random() < chance:
                mutated_genes.append(random.randint(0, 1))
            else:
                mutated_genes.append(gene)

        self.genes = mutated_genes

    def __len__(self):
        return self.length
