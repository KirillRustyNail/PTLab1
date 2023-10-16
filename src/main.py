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

    qr = CalcQuartile(rating)
    print("Quartile: ", qr.calc_last_quartile())


    #qr.show_all_last_quartile_students(rating)
    #print("Students in Quartile: ", students_quartile)


if __name__ == "__main__":
    main()
