import numpy as np
from numpy_exercises import dshc


def test_dshc_one():
    A = np.array(range(18, 34))
    assert np.array_equal(
        dshc.solution_one(A), np.array([range(18 + i, 18 + i + 7) for i in range(10)])
    )


def test_dshc_two():
    A = "position control hand research staff market court course evidence government view point time man minister action state effect mother country"
    assert (
        dshc.solution_two(A)
        == "ptsioitn ctnortl hand research soaff markeo cturo cturse evidence gtvernmeno view ptino oime man minisoer acoitn soaoe effeco mtoher ctunory"
    )
