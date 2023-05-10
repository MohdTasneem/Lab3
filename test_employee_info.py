import employee_info as info


def test_get_employee_age_range():
    result = []
    result_name = []
    lower_age = 24
    upper_age = 31
    test = ['John', 'Jane']

    result = info.get_employees_by_age_range(lower_age, upper_age)
    for item in result:
        result_name.append(item['name'])

    assert (result_name == test)


def test_calculate_average_salary():
    average = int(info.calculate_average_salary())

    assert (average == 60166)

def test_get_employees_by_dept():
    result = []
    result_name = []
    department = 'Engineering'
    test = ['Chloe', 'Mike']
    result = info.get_employees_by_dept(department)
    for item in result:
        result_name.append(item['name'])

    assert (result_name == test)
