import argparse
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from JsonDataReader import JsonDataReader
from CalcQuartile import CalcQuartile


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument(
        "-p", dest="path", type=str, required=True, help="Path to datafile"
    )
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    if path.endswith(".json"):
        reader = JsonDataReader()
    elif path.endswith(".txt"):
        reader = TextDataReader()

    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    qr = CalcQuartile(rating).calc_last_quartile()
    print("Quartile: ", qr)

    students_in_last_qr = CalcQuartile(rating).\
        show_all_students_last_quartile(qr)
    print("Students in Quartile: ", students_in_last_qr)


if __name__ == "__main__":
    main()
