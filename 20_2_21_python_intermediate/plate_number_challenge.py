"""
Given the romanian dictionary available here, create a script that will generate
all the possible romanian plate numbers that can be considered a word if read.
There are three types of plates in Romania:
B XX YYY (Bucharest - two digits - three letters)
B XXX YYY (Bucharest - three digits - three letters)
ZZ XX YYY (2 letter code of a county - two digits - three letters)
The conversion between digit and letter is the following:
1 – I (I from India)
2 – Z
3 – E
4 – A
5 – S
6 – G
7 – T
0 - O
Examples of plate numbers:
B 01 ERI (spelled BOIERI)
PH 03 NIX (spelled PHOENIX)+
"""
import re
import json
import pprint


counties = ['B', 'AB', 'AG', 'AR', 'BC', 'BH', 'BN', 'BR', 'BT', 'BV', 'BZ', 'CJ', 'CL', 'CS', 'CT', 'CV', 'DB', 'DJ',
            'GJ', 'GL', 'GR', 'HD', 'HR', 'IF', 'IL', 'IS', 'MH', 'MM', 'MS', 'NT', 'OT', 'PH', 'SB', 'SJ', 'SM', 'SV',
            'TL', 'TM', 'TR', 'VL', 'VN', 'VS']


def generate_all_plate_combinations(county):
    digit_letters = {'I': 1, 'Z': 2, 'E': 3, 'A': 4, 'S': 5, 'G': 6, 'T': 7, 'O': 0}

    # Search for valid words for counties that have abbreviation of two letters
    if len(county) == 2:
        results = {}
        pattern = re.compile(fr"(^{county})(I|Z|E|A|S|G|T|O)(I|Z|E|A|S|G|T|O)([A-Z]{{3}}$)")
        with open('words.txt', 'r') as f:
            for word in f.readlines():
                word = word.strip()
                match = pattern.search(word)
                if match:
                    county, digit1, digit2, letters = match.group(1), match.group(2), match.group(3), match.group(4)
                    results[word] = f"{county} {digit_letters[digit1]}{digit_letters[digit2]} {letters}"
        return results

    # Search for valid words for Bucharest that has an abbreviation of a single letter -> 'B'
    if county == 'B':
        results = {}

        # Search for Bucharest plate numbers with 2 middle digits
        pattern = re.compile(fr"(^{county})(I|Z|E|A|S|G|T|O)(I|Z|E|A|S|G|T|O)([A-Z]{{3}}$)")
        with open('words.txt', 'r') as f:
            for word in f.readlines():
                word = word.strip()
                match = pattern.search(word)
                if match:
                    county, digit1, digit2, letters = match.group(1), match.group(2), match.group(3), match.group(4)
                    results[word] = f"{county} {digit_letters[digit1]}{digit_letters[digit2]} {letters}"

        # Search for Bucharest plate numbers with 3 middle digits
        pattern = re.compile(fr"(^{county})(I|Z|E|A|S|G|T|O)(I|Z|E|A|S|G|T|O)(I|Z|E|A|S|G|T|O)([A-Z]{{3}}$)")
        with open('words.txt', 'r') as f:
            for word in f.readlines():
                word = word.strip()
                match = pattern.search(word)
                if match:
                    county, digit1, digit2, digit3, letters = match.group(1), match.group(2), match.group(3), \
                                                              match.group(4), \
                                                              match.group(5)
                    results[word] = f"{county} {digit_letters[digit1]}{digit_letters[digit2]}{digit_letters[digit3]}" \
                                    f" {letters}"

        return results


if __name__ == "__main__":
    all_possible_combinations = {}

    for county in counties:
        county_combinations = generate_all_plate_combinations(county)
        all_possible_combinations[county] = county_combinations

    with open('all_plate_combinations.json', 'w') as out_file:
        json.dump(all_possible_combinations, out_file)

    pprint.pprint(all_possible_combinations)
