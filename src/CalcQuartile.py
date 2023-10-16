from Types import DataType
from typing import List
import numpy as np

LastQuartile = dict[str, float]


class CalcQuartile:
    def __init__(self, rating: DataType) -> None:
        self.rating: DataType = rating
        self.LastQuartile: LastQuartile = {}

    def calc(self) -> LastQuartile:
        ratings: List[float] = [self.rating[x] for x in self.rating]
        ratings.sort()
        self.LastQuartile = np.percentile(ratings, 75)
        return self.LastQuartile
