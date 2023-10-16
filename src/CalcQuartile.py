from Types import DataType
from typing import List
import numpy as np

LastQuartile = float
QuartileStudents = dict[str]
Rating = dict[str, float]


class CalcQuartile:
    def __init__(self, rating: DataType) -> None:
        self.rating: DataType = rating
        self.LastQuartile: LastQuartile = 0
        self.QuartileStudents: QuartileStudents = {}

    def calc_last_quartile(self) -> LastQuartile:
        ratings: List[float] = [self.rating[x] for x in self.rating]
        ratings.sort()
        self.LastQuartile = np.percentile(ratings, 75)

        all_student = []
        for name, rat in ratings:
            if rat > self.LastQuartile:
                all_student.append(name)

        for name in all_student:
            print(name)

        return self.LastQuartile
