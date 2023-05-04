import Lab2.Lab2 as lab

def test_find_min_max():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 90]

    result = lab.find_min_max(input_arr)

    assert (result == test_arr)


def test_calc_average():

    input_arr = [1,3,5,7,9]
    test_arr = 5

    result = lab.calc_average(input_arr)

    assert (result == test_arr)


def test_median_temperature():
    input_arr = [1,3,5,7,9]
    test = 5

    result = lab.calc_median_temperature(input_arr)

    assert (result == test)
