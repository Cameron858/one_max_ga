import pytest
from one_max_ga.chromosome import OneMaxChromosome
from one_max_ga.population import Population


@pytest.fixture
def population():
    return Population(10, 5)


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
    assert pop.chromosomes[0] == chromosomes[0]


def test_single_index(population):
    pop_single = population[1]
    assert isinstance(pop_single, Population)
    assert len(pop_single) == 1
    assert pop_single.chromosomes[0].genes == population.chromosomes[1].genes


def test_slice_end(population):
    pop_slice_end = population[1:]
    assert len(pop_slice_end) == 9
    assert pop_slice_end.chromosomes[0].genes == population.chromosomes[1].genes


def test_slice_first_three(population):
    pop_first_three = population[:3]
    assert len(pop_first_three) == 3
    assert pop_first_three.chromosomes[0].genes == population.chromosomes[0].genes


@pytest.mark.parametrize("k", [0, 3, 5, 7, 9])
def test_random_returns_list_of_correct_size(k):
    # create with k+1 to ensure there are always enough chromosomes
    population = Population(k + 1, 5)
    assert len(population.random(k=k)) == k


def test_sampling_more_items_than_pop_size_raises_error(population):

    with pytest.raises(ValueError) as excinfo:
        population.random(k=len(population) + 5)
    assert str(excinfo.value) == "'k' cannot be greater than the population size."


def test_best_method_returns_fittest_member():

    best = OneMaxChromosome(genes=[1, 1, 1])

    chromosomes = [
        OneMaxChromosome(genes=[0, 0, 0]),
        OneMaxChromosome(genes=[0, 0, 1]),
        best,
    ]

    population = Population.from_chromosomes(chromosomes)

    assert population.best() == best
    assert population.best().genes == [1, 1, 1]
    assert population.best().fitness() == 3
