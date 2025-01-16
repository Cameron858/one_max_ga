import pytest
from pytest import param
from one_max_ga.algorithm import GeneticAlgorithm


@pytest.mark.parametrize(
    "crossover, mutation, selection, msg",
    [
        param(
            -0.1,
            0,
            0,
            "'crossover_rate' must be between 0 and 1",
            id="negative_crossover",
        ),
        param(
            0,
            -0.1,
            0,
            "'mutation_rate' must be between 0 and 1",
            id="negative_mutation",
        ),
        param(
            0,
            0,
            -0.1,
            "'selection_rate' must be between 0 and 1",
            id="negative_selection",
        ),
        param(
            1.1,
            0,
            0,
            "'crossover_rate' must be between 0 and 1",
            id="crossover_larger_than_one",
        ),
        param(
            0,
            1.1,
            0,
            "'mutation_rate' must be between 0 and 1",
            id="mutation_larger_than_one",
        ),
        param(
            0,
            0,
            1.1,
            "'selection_rate' must be between 0 and 1",
            id="selection_larger_than_one",
        ),
    ],
)
def test_invalid_rates_raise_value_error_and_message(
    crossover, mutation, selection, msg
):
    with pytest.raises(ValueError) as excinfo:
        GeneticAlgorithm(
            100,
            10,
            crossover_rate=crossover,
            mutation_rate=mutation,
            selection_rate=selection,
        )
    assert str(excinfo.value) == msg


@pytest.mark.parametrize(
    "crossover, mutation, selection",
    [
        param(
            0,
            0,
            0,
            id="all_rates_zero",
        ),
        param(
            1,
            1,
            1,
            id="all_rates_one",
        ),
        param(
            0.5,
            0.5,
            0.5,
            id="all_rates_within_range",
        ),
    ],
)
def test_valid_rates_do_not_raise_error(crossover, mutation, selection):

    GeneticAlgorithm(
        100,
        10,
        crossover_rate=crossover,
        mutation_rate=mutation,
        selection_rate=selection,
    )
