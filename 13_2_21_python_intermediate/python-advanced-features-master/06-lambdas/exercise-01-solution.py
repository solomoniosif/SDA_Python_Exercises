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
    def __init__(self, name):
        self.name = name
        self.registered_on = datetime.datetime.now()
        self.last_seen = self.registered_on
        self.number_of_logins = 1


users = [User("mouse123"), User("XXcatXX"), User("DoGgO")]
users[0].number_of_logins = 16
users[1].number_of_logins = 3
users[0].last_seen -= datetime.timedelta(days=1)
users[2].last_seen -= datetime.timedelta(days=7)


if __name__ == "__main__":
    by_registered_on = sorted(users, key=lambda user: user.registered_on)
    by_last_seen = sorted(users, key=lambda user: user.last_seen)
    by_logins = sorted(users, key=lambda user: user.number_of_logins)

    print(f"Users in order of registration: {[u.name for u in by_registered_on]}")
    print(f"Users in order of last logins: {[u.name for u in by_last_seen]}")
    print(f"Users in order of login count: {[u.name for u in by_logins]}")
