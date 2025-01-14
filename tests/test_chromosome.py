import random
from one_max_ga.chromosome import OneMaxChromosome
import pytest


def test_init_random_genes(mocker):
    mock_random = mocker.patch("random.randint", side_effect=[0, 1, 0, 1, 0])
    chromosome = OneMaxChromosome(length=5)
    assert chromosome.genes == [0, 1, 0, 1, 0]
    assert chromosome.length == 5
    mock_random.assert_called_with(0, 1)


def test_init_with_genes():
    genes = [1, 0, 1, 1, 0]
    chromosome = OneMaxChromosome(length=5, genes=genes)
    assert chromosome.genes == genes


@pytest.mark.parametrize("l", [-1, 0.1, "a", (), 0])
def test_invalid_length_argument(l):

    with pytest.raises(ValueError):
        OneMaxChromosome(length=l)


def test_crossover_different_length_chromosomes_raises_value_error():
    p1 = OneMaxChromosome(length=5)
    p2 = OneMaxChromosome(length=10)

    with pytest.raises(ValueError):
        p1.crossover(p2)


def test_crossover_invalid_method_raises_value_error():

    p1 = OneMaxChromosome(length=5)
    p2 = OneMaxChromosome(length=5)

    with pytest.raises(ValueError):
        p1.crossover(p2, method="abc")


@pytest.mark.parametrize(
    "genes", [[0, 1, 0, 1, 0], [1, 1, 1], [0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1]]
)
def test_crossover_uniform(genes, mocker):
    p1 = OneMaxChromosome(length=len(genes))
    p2 = OneMaxChromosome(length=len(genes))

    mocker.patch("random.choice", side_effect=genes)

    child = p1.crossover(p2, method="uniform")

    assert child.genes == genes
    assert len(child) == len(genes)


def test_direct_reproduction_creates_correct_child():
    p1 = OneMaxChromosome(length=5)

    child = p1.direct()

    assert len(child) == len(p1)
    assert child.genes == p1.genes
    # child should be new instance
    assert child is not p1


@pytest.mark.parametrize("mutation_chance", [-0.1, -1, 1.0001, 2])
def test_invalid_mutation_value_raises_value_error(mutation_chance):
    p1 = OneMaxChromosome(length=5)

    with pytest.raises(ValueError):
        p1.mutate(chance=mutation_chance)


@pytest.mark.parametrize("mutation_chance", [0, 0.0001, 0.1, 0.9999, 1])
def test_valid_mutation_value_raises_no_error(mutation_chance):
    p1 = OneMaxChromosome(length=5)
    p1.mutate(chance=mutation_chance)


@pytest.mark.parametrize(
    "original, mutated",
    [
        ([0, 1, 0], [1, 0, 1]),
        ([0, 0, 0], [1, 1, 1]),
        ([1, 0, 1, 0, 1], [0, 1, 0, 1, 0]),
    ],
)
def test_mutation_produces_different_genes(original, mutated):

    p1 = OneMaxChromosome(length=5, genes=original)
    p1.mutate(chance=1)
    assert p1.genes == mutated


def test_mutate_always_changes_genes(mocker):
    mocker.patch("random.random", side_effect=[0.1, 0.8, 0.2, 0.9, 0.05])
    original_genes = [0, 1, 0, 1, 1]
    p1 = OneMaxChromosome(length=5, genes=original_genes)
    p1.mutate(chance=0.5)
    assert p1.genes == [1, 1, 1, 1, 0]


@pytest.mark.parametrize("l", [3, 5, 7, 9])
def test_chromosome_length_is_correct(l):
    assert len(OneMaxChromosome(length=l)) == l
