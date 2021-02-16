"""
- Given a list of `User` objects, try sorting them using:
    -  `registered_on` 
    - `number_of_logins` 
    - `last_seen`
- To do that, use either `list.sort()` or `sorted()`. Both support a keyword parameter `key=callable`. 
- Result of `callable` will be compared using comparison operators to determine order in list
"""

import datetime


class User:
    def __init__(self, name, registered_on, number_of_logins, last_seen):
        self.name = name
        self.registered_on = registered_on
        self.number_of_logins = number_of_logins
        self.last_seen = last_seen

    def __repr__(self):
        return f"'{self.name}'"

    def __str__(self):
        return f"User '{self.name}', registered on {self.registered_on}, last seen on {self.last_seen}, with {self.number_of_logins} logins."


users = [User('admin', datetime.date(2018, 1, 5), 134, datetime.datetime.now()-datetime.timedelta(days=1)), 
        User('john05', datetime.date(2021, 1, 21), 7, datetime.datetime.now()-datetime.timedelta(days=10, hours=7, minutes=7)),
        User('andy34', datetime.date(2020, 9, 7), 19, datetime.datetime.now()-datetime.timedelta(hours=21)),
        User('greyOwl', datetime.date(2019, 11, 12), 117, datetime.datetime.now()-datetime.timedelta(days=1, hours=1))
        ]


if __name__ == '__main__':
    sorted_by_register_date = sorted(users, key=lambda x: x.registered_on)
    sorted_by_last_seen = sorted(users, key=lambda x: x.last_seen, reverse=True)
    sorted_by_no_of_logins = sorted(users, key=lambda x: x.number_of_logins)

    print(sorted_by_register_date)
    print(sorted_by_last_seen)
    print(sorted_by_no_of_logins)

    print("\nUsers sorted by da date of registration:")
    for user in sorted_by_register_date:
        print(user)

    print("\nUsers by last time seen online:")
    for user in sorted_by_last_seen:
        print(user)

    print("\nUsers by numbers of logins:")
    for user in sorted_by_no_of_logins:
        print(user)