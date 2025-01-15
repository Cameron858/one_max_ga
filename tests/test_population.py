import pytest
from one_max_ga.chromosome import OneMaxChromosome
from one_max_ga.population import Population


def test_population_init_with_valid_size():
    size = 10
    chromosome_length = 5
    population = Population(size=size, chromosome_length=chromosome_length)
    assert len(population.chromosomes) == size
    for chromosome in population.chromosomes:
        assert isinstance(chromosome, OneMaxChromosome)
        assert chromosome.length == chromosome_length


def test_population_init_with_invalid_size():
    with pytest.raises(ValueError):
        Population(size="invalid", chromosome_length=5)


def test_sorting_population_not_inplace_returns_correct_order():

    pop = Population(10, 5)

    sorted_chromosomes = pop.sort_by_fitness()

    assert sorted_chromosomes is not None
    assert isinstance(sorted_chromosomes, list)

    for first, second in zip(sorted_chromosomes[:-1], sorted_chromosomes[1:]):
        assert first.fitness() >= second.fitness()


def test_creating_pop_from_chromosomes():

    chromosomes = [OneMaxChromosome(5) for _ in range(10)]
    pop = Population.from_chromosomes(chromosomes)

    assert pop.size == len(chromosomes)
    assert pop.chromosomes == chromosomes
