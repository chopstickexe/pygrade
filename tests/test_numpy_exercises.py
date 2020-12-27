from numpy_exercises import __version__
from numpy_exercises import one
import numpy as np


def test_one():
    A = np.array(range(18, 34))
    assert np.array_equal(one.solution(A), np.array([range(18 + i, 18 + i + 7) for i in range(10)]))

