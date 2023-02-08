import pytest


@pytest.mark.parametrize("HDL_input, expected",
                         [(65, "Normal"),
                          (45, "Borderline low"),
                             (30, "Low")
                          ])
def test_HDL_analysis(HDL_input, expected):

    from blood_calculator import HDL_analysis

    answer = HDL_analysis(HDL_input)  # act

    assert answer == expected


@pytest.mark.parametrize("LDL_input, expected",
                         [(200, "Very high"),
                          (175, "High"),
                             (150, "Borderline high"),
                             (100, "Normal")
                          ])
def test_LDL_analysis(LDL_input, expected):

    from blood_calculator import LDL_analysis

    answer = LDL_analysis(LDL_input)

    assert answer == expected
