# hero caampued

# tester fails all files when newlines are formatted as instructed in the assignment (\r\n)
# fixed when changed to \n only

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

    while not re.search(valid_filename_pattern, valid_filename):
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

    filenames_and_patterns = {
        "vowel_vowel_vowel.txt": r"[aeiou]{3}",  # 1
        "notvowel_notvowel.txt": r"[aeiou]{2}",  # 2
        "cons_cons_cons.txt": r"[bcdfghjklmnpqrstvwxyz]{3}",  # 3
        "i_before_e.txt": r"i.*e",  # 4
        "a_a.txt": r"^a.*a$",  # 5
        "start_end_same.txt": r"[a-z]",  # 6 a bit weird, but this is the workaround I found
        "weird.txt": r"[' \-]",  # 7
        "not_start.txt": r"^[^a-el-ps]",  # 8
        "multiple.txt": r".* .*",  # 9
        "city_town.txt": r"(city|town)$",  # 10
        "hyphen.txt": r"-",  # 11
        "consonant_vowel.txt": r"^([bcdfghjklmnpqrstvwxyz].*[aeiou]|[aeiou].*[bcdfghjklmnpqrstvwxyz])$",  # 12
        "spaces.txt": r" ",  # 13
        "not_aeio.txt": r"^[^aeio]*$",  # 14
        "alternating.txt": r"^(([aeiou][bcdfghjklmnpqrstvwxyz])+|([bcdfghjklmnpqrstvwxyz][aeiou])+)$",  # 15
        "double.txt": r"aa|bb|cc|dd|ee|ff|gg|hh|ii|jj|kk|ll|mm|nn|oo|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz",  # 16
    }

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

    for filename, pattern in filenames_and_patterns.items():
        with open(filename, "w") as file:

            for capital, country in places.items():

                # 2
                if filename == "notvowel_notvowel.txt":
                    if not re.search(pattern, country):
                        file.write(country + "\n")
                    if not re.search(pattern, capital):
                        file.write(capital + "\n")

                # 6
                elif filename == "start_end_same.txt":
                    start_country = re.findall(rf"^{pattern}", country)
                    end_country = re.findall(rf"{pattern}$", country)
                    if start_country and end_country and start_country[0] == end_country[0]:
                        file.write(country + "\n")

                    start_capital = re.findall(rf"^{pattern}", capital)
                    end_capital = re.findall(rf"{pattern}$", capital)
                    if start_capital and end_capital and start_capital[0] == end_capital[0]:
                        file.write(capital + "\n")

                # 13
                elif filename == "spaces.txt":
                    spaces_country = re.findall(pattern, country)

                    if len(spaces_country) > 1:
                        file.write(country + "\n")

                    spaces_capital = re.findall(pattern, capital)
                    if len(spaces_capital) > 1:
                        file.write(capital + "\n")

                else:
                    if re.search(pattern, country):
                        file.write(country + "\n")

                    if re.search(pattern, capital):
                        file.write(capital + "\n")


# print(write_countries_capitals_to_file("a.txt"))
# print(write_countries_capitals_to_file("5x.txt"))
# print(write_countries_capitals_to_file("AbcE123z.txt"))
