import pytest


def square_num():
    num = input("Enter a number: ")

    try:
        num = num ** 2
    except TypeError:
        num = float(num)
        num = num ** 2

    print(num)


def driver():
    square_num()


def add_two_numbers(a, b):
    if ~isinstance(a, int) or ~isinstance(b, int):
        raise TypeError("One of a or b is not an integer")

    if a < 0 or b < 0:
        raise ValueError("One of a or b is a negative number")

    return a + b


@pytest.mark.parametrize("a, b, expected",
                         [(4, 3, 7),
                          (4, -3, ValueError),
                          (4, 3.1, TypeError)
                          ])
def test_add_two_numbers(a, b, expected):

    answer = add_two_numbers(a, b)  # act

    assert answer == expected
