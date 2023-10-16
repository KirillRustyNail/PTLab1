# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcQuartile import CalcQuartile
import pytest

RatingsType = dict[str, float]
StudentIn = [str]


class TestCalcRating:
    @pytest.fixture()
    def input_data(self) -> tuple[RatingsType, float, StudentIn]:
        rating: DataType = {
            "Иванов Иван Иванович": 82.0,
            "Петров Петр Петрович": 83.66666666666667,
            "Сидоров Сидор Сидорович": 72.33333333333333,
            "Васильев Василий Васильевич": 93.33333333333333,
        }

        lastquartile = 86.08333333333334

        rating_scores: StudentIn = ["Васильев Василий Васильевич"]

        return rating, lastquartile, rating_scores

    def test_calc_last_quartile(
        self, input_data: tuple[DataType, float, StudentIn]
    ) -> None:
        calc_rating = CalcQuartile(input_data[0])
        assert input_data[0] == calc_rating.rating

    def test_calc_quartile(self, input_data: tuple[DataType, float, StudentIn]
                           ) -> None:

        rating = CalcQuartile(input_data[0]).calc_last_quartile()
        assert pytest.approx(rating, abs=0.001) == input_data[1]

    def test_shows_calc_quartile(
        self, input_data: tuple[DataType, float, StudentIn]
    ) -> None:

        rating_scores: StudentIn = CalcQuartile(
            input_data[0]
        ).show_all_students_last_quartile(input_data[1])
        assert rating_scores == input_data[2]
