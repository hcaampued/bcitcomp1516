# hero caampued

import re

capitals = []
countries = []
places = {}


def write_countries_capitals_to_file(filename):
    """
    This function creates/opens a file for writing to write the countries capitals from places.txt if the user
        enters a valid file name.

    Valid filenames must follow the following rules:
        - Must contain only letters or digits.
        - Must be of length 1-8 characters, plus a ".txt" file extension.

    For example, these are all valid filenames:
        a.txt
        5x.txt
        AbcE123z.txt

    If the filename is not valid,
        - Prompt the user for another filename inside the function.
        - This process must continue over and over until the user enters a valid filename.
        - Once the user has entered a valid filename (e.g. data.txt), create/open the file for writing only,
            and write all the countries and capitals from places.txt to the new file in the following format:
                The capital of Afghanistan is Kabul
                The capital of Albania is Tirana (Tirane)

    Note:
        - For the newline character in this assignment, ALWAYS use "\r\n"
        - The country name and its capital city name are all in Title Case. Make sure to close your files.

    :param filename: a file name (string)
    :return: None
    """
    valid_filename_pattern = r"^[a-zA-Z0-9]{1,8}(\.txt)$"
    valid_filename = filename

    while not re.match(valid_filename_pattern, valid_filename):
        valid_filename = input("The file name must contain only letters or digits, be 1-8 characters in length, "
                               "and ends with a .txt file extension.\nPlease enter a valid file name: ")

    with open("places.txt", "r") as data:
        places_data = data.readlines()
        with open(valid_filename, "w") as file:
            for place in places_data:
                country, capital = place.strip().split(":")
                file.write("The capital of " + country + " is " + capital + "\r\n")

    print(f"The file {valid_filename} was created successfully.")

    return None


def save_filtered_places():
    """
    This function reads the places.txt file and copies the file data into three GLOBAL variables.
    Then, it creates/opens files for writing only. Uses regular expressions to find all the places
    that satisfies the patters, and write the results to the files with the associated file names.

    Three GLOBAL variables (all data is in lowercase):
        1. capitals  (a tuple of just the capitals, from places.txt file)
        2. countries  (a tuple of just the countries, from places.txt file)
        3. places  (a dictionary of capitals and countries, in the format such as this:
            {"ottawa": "canada", "mexico city": "mexico", …} from places.txt file)

    Filename, Capitals and countries to store in the file (containing the patterns):
        1. vowel_vowel_vowel.txt --> Contains three consecutive vowels
        2. notvowel_notvowel.txt --> Does NOT contain two consecutive vowels
        3. cons_cons_cons.txt --> Contain three consecutive consonants
        4. i_before_e.txt --> Contain i somewhere before e. For example: Ireland
        5. a_a.txt --> Start with a and end with a
        6. start_end_same.txt --> Starts and ends with the same character (e.g. warsaw)
        7. weird.txt --> Contains apostrophe, space, or dash
        8. not_start.txt --> Does not start with a-e, l-p, or s
        9. multiple.txt --> Consist of more than one word (e.g., New Delhi).
        10. city_town.txt --> End with "city" or "town"
        11. hyphen.txt --> Contain hyphen(s)
        12. consonant_vowel.txt --> Start with a consonant and end with a vowel, or vice versa
        13. spaces.txt --> Contains more than one space
        14. not_aeio.txt --> Do not contain any of a, e, i, or o
        15. alternating.txt --> Consist of entirely alternating vowels and consonants (e.g. starts with a vowel,
            followed by a consonant, and so on).
        16. double.txt --> Contain any double letters (e.g., Addis Ababa).

    Close each file when it's finished.

    :return: None
    """
    global capitals, countries, places

    with open("places.txt", "r") as data:
        places_data = data.readlines()

        capitals_list = []
        countries_list = []
        places_dict = {}

        for place in places_data:
            country, capital = place.lower().strip().split(":")
            capitals_list.append(capital)
            countries_list.append(country)
            places_dict[capital] = country

        capitals = tuple(capitals_list)
        countries = tuple(countries_list)
        places = places_dict

    filenames_and_patterns = [
        ("vowel_vowel_vowel.txt", r"^$"),
        ("notvowel_notvowel.txt", r"^$"),
        ("cons_cons_cons.txt", r"^$"),
        ("i_before_e.txt", r"^$"),
        ("a_a.txt", r"^$"),
        ("start_end_same.txt", r"^$"),
        ("weird.txt", r"^$"),
        ("not_start.txt", r"^$"),
        ("multiple.txt", r"^$"),
        ("city_town.txt", r"^$"),
        ("hyphen.txt", r"^$"),
        ("consonant_vowel.txt", r"^$"),
        ("spaces.txt", r"^$"),
        ("not_aeio.txt", r"^$"),
        ("alternating.txt", r"^$"),
        ("double.txt", r"^$"),
    ]

    for filename, pattern in filenames_and_patterns:

    pass


# print(write_countries_capitals_to_file("a.txt"))
# print(write_countries_capitals_to_file("5x.txt"))
# print(write_countries_capitals_to_file("AbcE123z.txt"))
write_countries_capitals_to_file("sdfsf.txt")
