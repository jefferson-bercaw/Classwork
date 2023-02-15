import pytest


@pytest.mark.parametrize("a, b, expected",
                         [(4, 3, 7),
                          (4, -3, ValueError),
                          (4, 3.1, TypeError)
                          ])
def test_add_two_numbers(a, b, expected):

    from errors import add_two_numbers

    answer = add_two_numbers(a, b)  # act

    assert answer == expected
