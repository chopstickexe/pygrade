import numpy as np
import re


def solution_one(A):
    # Must be less than 45 bytes
    return np.stack(A[i : i + 7] for i in range(10))


def solution_two(A):
    # Must be less than 40 bytes
    # NG: 55 bytes
    # return A.replace('t', '*').replace('o', 't').replace('*', 'o')
    # NG: 61 bytes
    # return re.sub('_', '', re.sub(r'o(?!_)', 't', re.sub('t', 'o_', A)))
    # NG: 48 bytes
    # return A.translate(str.maketrans({'t': 'o', 'o': 't'}))
    # Ref: https://qiita.com/tag1216/items/df6c93bdb823dd48af6c
    return A.translate(str.maketrans('to', 'ot'))
