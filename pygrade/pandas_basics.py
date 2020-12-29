from typing import Dict

import numpy as np
import pandas as pd


def one(A: np.ndarray):
    return A[A >= 8]

def two(A: np.ndarray, B: np.ndarray):
    return A + B

def three(A: np.ndarray):
    A.sort(axis=1)
    return A

def four(A: np.ndarray):
    return A[(A < 4) | (13 < A)]

def five(A: np.ndarray):
    return np.ceil(A)

def six(A: np.ndarray):
    return np.dot(A, B)

def seven(A: np.ndarray):
    return A.max(axis=0)

def eight(A: np.ndarray):
    A[A < 7] = 0
    return A

def nine(A: np.ndarray):
    # A[[i, j]] equals to A[[i, j], :]
    # Ref: https://stackoverflow.com/questions/54069863/swap-two-rows-in-a-numpy-array-in-python
    A[[1, 4]] = A[[4, 1]]
    return A

def ten(A: np.ndarray):
    # How can I get 0.125 from 2, 1.0 from 9, and 0.25 from 3?
    return True

def eleven(df: pd.DataFrame):
    return df.set_index("education")

def twelve(df: pd.DataFrame):
    return df[0:6]

def thirteen(df: pd.DataFrame, random_state: int = 78):
    return df.sample(6, random_state=random_state)

def fourteen(df: pd.DataFrame):
    return df["order"].describe()

def fifteen(df: pd.DataFrame):
    return df.loc[[0, 1, 11, 12, 13, 14]]

def sixteen(df: pd.DataFrame):
    # NG: return df["a"] (Must return a dataframe)
    return df[["a"]].T

def seventeen(df: pd.DataFrame):
    return df.between_time("7:30", "0:30")

def eighteen(df: pd.DataFrame):
    # NG: 2 bytes over & the returned series doesn't have a "Size" col
    # return df.groupby(by="world").size()
    return True  # Give up

def nineteen(df: pd.DataFrame):
    # Must use asfreq(), not resample() as resample() makes groups by 2 days and cannot return NaN for non-existing dates
    # Ref: https://note.nkmk.me/python-pandas-time-series-resample-asfreq/
    return df.asfreq("2D")

def twenty(df: pd.DataFrame, labels: Dict[int, str]):
    return return df["job"].replace(labels).value_counts()
