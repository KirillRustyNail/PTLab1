from Types import DataType
from DataReader import DataReader
import json

class JsonDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
            for key, subjects in data.items():
                self.students[key] = [[(subj, score) for subj, score in subjects]]
        return self.students
