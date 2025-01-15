from one_max_ga.selectors import ElitismSelector
from one_max_ga.population import Population
import pytest


@pytest.mark.parametrize("elite_size", [1, 3, 5, 7])
def test_selector_returns_pop_of_correct_size(elite_size):

    pop = Population(10, 5)

    selector = ElitismSelector(elite_size)
    new_pop = selector.select(pop)

    assert new_pop.size == elite_size
