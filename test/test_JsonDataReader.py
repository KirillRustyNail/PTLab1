# -*- coding: utf-8 -*-
import pytest
import json
from src.Types import DataType
from src.JsonDataReader import JsonDataReader


class TestTextDataReader:
    @pytest.fixture()
    def json_file_and_data_content(self) -> tuple[str, DataType]:
        text = '''
            {
            "Аншаков Кирилл Игоревич": {
                "математика": 91,
                "химия": 100,
                "программирование": 76
            },
            "Палкин Дмитрий Алексеевич": {
                "русский язык": 90,
                "химия": 81,
                "литература": 78
            }
            }
        '''
        data = {
            "Аншаков Кирилл Игоревич":
                [("математика", 91), ("химия", 100), ("программирование", 76)],
            "Палкин Дмитрий Алексеевич":
                [("русский язык", 90), ("химия", 81), ("литература", 78)],
        }
        return text, data

    @pytest.fixture()
    def json_filepath_and_data(
            self, json_file_and_data_content: tuple[str, DataType], tmpdir
    ) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.json")
        data = json.loads(json_file_and_data_content[0])
        with open(str(p), "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        return str(p), json_file_and_data_content[1]

    def test_read(self, json_filepath_and_data: tuple[str, DataType]) -> None:
        file_content = JsonDataReader().read(json_filepath_and_data[0])
        assert file_content == json_filepath_and_data[1]
