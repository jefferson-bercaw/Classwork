import pytest


@pytest.mark.parametrize("point_1, point_2, x, expected",
                         [((0, 0), (1, 1), 0.4, 0.4),
                          ((0, 0), (2, 1), 1, 0.5),
                             ((0, 0), (1, 2), 0.5, 1)])
                             
def test_on_line(point_1, point_2, x, expected):

    from on_line import on_line

    answer = on_line(point_1, point_2, x)  # act

    assert answer == expected
    
    
@pytest.mark.parametrize("point_1, point_2, expected",
                         [((0, 0), (1, 1), 1),
                          ((0, 0), (2, 1), 0.5),
                             ((0, 0), (1, 2), 2)])
                             
def test_get_slope(point_1, point_2, expected):

    from on_line import get_slope

    answer = get_slope(point_1, point_2)  # act

    assert answer == expected
    
    