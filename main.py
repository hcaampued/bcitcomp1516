# hero caampued

import assignment2


def main():
    """
    This script imports assignment2.py, then calls assignment2.write_countries_capitals_to_file("0123456789.txt"),
    and finally calls assignment2.save_filtered_places().

    :return: None
    """
    assignment2.write_countries_capitals_to_file("0123456789.txt")
    assignment2.save_filtered_places()


if __name__ == "__main__":
    main()
