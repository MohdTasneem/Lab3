import Lab2.bmi as bmi


def test_bmi_normal_weight():
    result = 0
    input = 55
    test = 0

    result = bmi.calculate_bmi(1.6, input)

    assert (result == test)


def test_bmi_over_weight():
    result = 0
    input = 75
    test = 1

    result = bmi.calculate_bmi(1.6, input)

    assert (result == test)


def test_bmi_under_weight():
    result = 0
    input = 40
    test = -1

    result = bmi.calculate_bmi(1.6, input)

    assert (result == test)
