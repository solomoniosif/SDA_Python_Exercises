def is_leap(year):
    # Write your logic here
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap


def is_leap2(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    return leap



for year in range(1200, 2021):
    if is_leap(year) != is_leap2(year):
        print(year)
    



