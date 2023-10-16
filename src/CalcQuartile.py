from Types import DataType
from typing import List
import numpy as np

LastQuartile = float
Rating = dict[str, float]
Studens_in = []


class CalcQuartile:
    def __init__(self, rating: DataType) -> None:
        self.rating: DataType = rating
        self.LastQuartile: LastQuartile = 0
        self.QuartileStudents: Studens_in = {}

    def calc_last_quartile(self) -> LastQuartile:
        ratings: List[float] = [self.rating[x] for x in self.rating]
        ratings.sort()
        self.LastQuartile = np.percentile(ratings, 75)
        return self.LastQuartile

    def show_all_students_last_quartile(self, quartile: float) -> Studens_in:
        for k, v in self.rating.items():
            if v > quartile:
                Studens_in.append(k)
        return Studens_in
