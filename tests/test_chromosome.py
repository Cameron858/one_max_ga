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


@pytest.mark.parametrize("l", [-1, 0.1, "a", ()])
def test_invalid_length_argument(l):

    with pytest.raises(ValueError):
        OneMaxChromosome(length=l)
