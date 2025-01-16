import pytest
from pytest import param
from one_max_ga.algorithm import GeneticAlgorithm
from one_max_ga.terminators import MaxGenerationsTerminator


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


def test_terminator_defaults_to_correct_terminator():

    ga = GeneticAlgorithm(100, 10, 0.5, 0.01)

    assert isinstance(ga.terminator, MaxGenerationsTerminator)


@pytest.mark.parametrize("max_generations", [1, 50, 100])
def test_run_stops_at_max_generations_with_default_terminator(max_generations):
    ga = GeneticAlgorithm(100, 10, 0.5, 0.01, max_generations=max_generations)
    ga.run()

    assert ga.generation == max_generations


@pytest.mark.parametrize("max_generations", [1, 50, 100])
def test_run_stops_at_max_generations_with_mocked_terminator(mocker, max_generations):
    """This test mocks a Terminator object to always return False.

    This isolates the built in behaviour of (self.generation < self.max_generations)
    """
    mock_terminator = mocker.MagicMock()
    mock_terminator.terminate.return_value = False

    ga = GeneticAlgorithm(
        100, 10, 0.5, 0.01, max_generations=max_generations, terminator=mock_terminator
    )

    ga.run()

    assert ga.generation == max_generations
    assert mock_terminator.terminate.call_count == max_generations
