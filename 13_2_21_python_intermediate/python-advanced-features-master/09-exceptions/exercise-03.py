"""
1. Define your own exceptions:
    1. `PasswordTooShort`
    2. `PasswordTooLong`
    3. `InvalidPassword`
2. Write a function `validate_password()`:
    1.  check whether user input collected via `input()` equals 
        `secret_password` variable.
    2. If the input is too short (less than 3 characters) or too long
       (longer than 30 characters), raise appropriate exceptions
    3. If the password does not match, raise `InvalidPassword`
3. Handle all exceptions raised in `validate_password` by printing a 
   nice message.
"""
secret_password = "It's a secret!"


def validate_password():
    user_pass = input("Password: ")
    if len(user_pass) < 3:
        raise PasswordTooShort()
    elif len(user_pass) > 30:
        raise PasswordTooLong()
    if user_pass != secret_password:
        raise InvalidPassword()
    print("Bingo!")


class PasswordTooShort(Exception):
    pass


class PasswordTooLong(Exception):
    pass


class InvalidPassword(Exception):
    pass


if __name__ == "__main__":
    try:
        validate_password()
    except PasswordTooShort:
        print("Password too short!")
    except PasswordTooLong:
        print("Password too long!")
    except InvalidPassword:
        print("Invalid password!")
