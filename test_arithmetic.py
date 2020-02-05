import pytest


@pytest.mark.parametrize("input, output, expected", [
    ((2, 1), 1, True),
    ((5, 6.1), -1.1, True),
    ((1.4, 4.0), -2, False),
])
def test_subtract(input, output, expected):
    from arithmetic import subtract
    answer = subtract(input)
    print(answer)
    bool = pytest.approx(answer) == output
    assert bool == expected
