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
