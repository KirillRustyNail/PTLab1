from Types import DataType
from DataReader import DataReader
import json


class JsonDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
            for key, subject_scores in data.items():
                scores_list = [(subject, score) for
                               subject, score in subject_scores.items()]
                self.students[key] = scores_list
        return self.students
