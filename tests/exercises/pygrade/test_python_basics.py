import numpy as np
from exercises.pygrade import python_basics


def test_one():
    A = np.array(range(18, 34))
    assert np.array_equal(
        python_basics.solution_one(A), np.array([range(18 + i, 18 + i + 7) for i in range(10)])
    )


def test_two():
    A = "position control hand research staff market court course evidence government view point time man minister action state effect mother country"
    assert (
        python_basics.solution_two(A)
        == "ptsioitn ctnortl hand research soaff markeo cturo cturse evidence gtvernmeno view ptino oime man minisoer acoitn soaoe effeco mtoher ctunory"
    )


def test_three():
    A = ["country", "form", "Name", "order", "god", "information", "child", "Night", "policy", "development", "question", "end", "Work", "mother", "Problem", "Age", "Road", "Company", "Head", "home"]
    assert (python_basics.solution_three(A) == "Name, Night, Work, Problem, Age, Road, Company, Head")


def test_four():
    A = np.array(range(0, 25)).reshape(5, 5)
    assert np.array_equal(python_basics.solution_four(A), np.array([[0, 5, 10, 15, 20]]))


def test_five():
    A = np.array([[3, 10, 2, 11, 9, 17], [18, 11, 5, 16, 13, 12], [6, 5, 1, 14, 11, 17], [7, 1, 7, 19, 8, 13], [5, 16, 18, 1, 13, 5], [19, 2, 9, 10, 1, 19]])
    assert np.array_equal(python_basics.solution_five(A), np.array([[0, 0, 0, 11, 0, 17], [18, 11, 0, 16, 13, 12], [0, 0, 0, 14, 11, 17], [0, 0, 0, 19, 0, 13], [0, 16, 18, 0, 13, 0], [19, 0, 0, 0, 0, 19]]))

