"""
You have a text file with content:
{
   "right_side":[
      3,
      5,
      3,
      6,
      4,
      2,
      3,
      6,
      8,
      4,
      3,
      2
   ],
   "left_side":[
      1.2,
      4.3,
      5.4,
      6.9,
      9.9,
      7.2
   ]
}
Write a program that prints the average of the numbers in the "right_side" field,
the average of the "left_side" field, and the average of both fields.
"""
import csv
import json


with open('data.txt', 'r') as f:
    data = json.load(f)


def average(lst):
    lst = [el for el in lst if isinstance(el, (int, float))]
    return round(sum(lst) / len(lst), 2) if lst else None


right_side, left_side = data['right_side'], data['left_side']

print(f"The average of the numbers in the right_side: {average(right_side)}")
print(f"The average of the numbers in the left_side: {average(left_side)}")
print(f"The average of the numbers in both fields: {average(right_side + left_side)}")

# # with open('data.txt', 'r') as f:
# #     data = eval(f.read())


"""
Write a function that converts CSV to JSON. For example:

CSV data:
"""

csv_data = """album, year, US_peak_chart_post
The White Stripes, 1999, -
De Stijl, 2000, -
White Blood Cells, 2001, 61
Elephant, 2003, 6
Get Behind Me Satan, 2005, 3
Icky Thump, 2007, 2
Under Great White Northern Lights, 2010, 11
Live in Mississippi, 2011, -
Live at the Gold Dollar, 2012, -
Nine Miles from the White City, 2013, -"""

with open('albums.csv', 'r') as f:
    reader = csv.DictReader(f)
    with open('albums.json', 'a') as json_file:
        for row in reader:
            json.dump(row, json_file, indent=4)
