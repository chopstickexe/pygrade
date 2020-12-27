import numpy as np
import re


def solution(A):
    # Must be less than 45 bytes
    return np.stack(A[i : i + 7] for i in range(10))
