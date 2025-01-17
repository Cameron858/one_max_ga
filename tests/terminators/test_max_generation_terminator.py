from one_max_ga.terminators import MaxGenerationsTerminator
import pytest


@pytest.mark.parametrize(
    "max_generations, current_generation, expected",
    [(100, 50, False), (100, 99, False), (100, 100, True), (50, 100, True)],
)
def test_termination_is_correct(max_generations, current_generation, expected):
    terminator = MaxGenerationsTerminator(max_generations=max_generations)

    assert terminator.terminate(None, generation=current_generation) == expected
