from numpy_exercises import __version__
from numpy_exercises import one, two
import numpy as np


def test_one():
    A = np.array(range(18, 34))
    assert np.array_equal(one.solution(A), np.array([range(18 + i, 18 + i + 7) for i in range(10)]))

def test_two():
    A = "position control hand research staff market court course evidence government view point time man minister action state effect mother country"
    assert two.solution(A) == "ptsioitn ctnortl hand research soaff markeo cturo cturse evidence gtvernmeno view ptino oime man minisoer acoitn soaoe effeco mtoher ctunory"
