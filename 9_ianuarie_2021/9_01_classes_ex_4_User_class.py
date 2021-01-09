
# 1. Create User class with name and password fields.
# 2. The name field should be accessible and the password field should be private and accessed
# through a property.
# 3. The initialization method should accept only the name field.
# 4. The password's setter should check if the password is at least 6 characters long, if it is less
# then it should extend the provided value to 6 characters by adding appropriate number of "#"
# characters ('ab' -> 'ab####'). If the password is 6 or more characters long then it should not
# modify it.
# 5. The getter should return the password in an encrypted format, that is replacing all letters
# except first and last with the "*" character ('password' -> 'p******d').
# 6. The deleter should delete the password.


class User():
    def __init__(self, name):
        self.name = name
        self.__password = None

    @property
    def password(self):
        # encrypted_password = ['*' for ch in self.__password]
        # encrypted_password[0] = self.__password[0]
        # encrypted_password[-1] = self.__password[-1]
        # return "".join(encrypted_password)
        return self.__password[0] + "*" * (len(self.__password) - 2) + self.__password[-1]

    @password.setter
    def password(self, password):
        if len(password) < 6:
            self.__password = password + '#' * (6 - len(password))
        else:
            self.__password = password

    @password.deleter
    def password(self):
        del self.__password


iosif = User("Iosif")
iosif.password = 'abc1'
print(iosif.password)

andrei = User("Andrei")
andrei.password = 'sdofjghbopw45u89ufg'
print(andrei.password)

del andrei.password
try:
    print(andrei.password)
except:
    print(f"User {andrei.name} has no password set.")