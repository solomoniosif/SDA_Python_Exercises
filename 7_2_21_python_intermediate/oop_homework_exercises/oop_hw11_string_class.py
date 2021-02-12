
# TODO: Write a Python class which has two methods get_String and print_String. 
# * get_String accept a string from the user and print_String print the string in upper case.


class String:
    def get_string(self):
        self._string = input('Enter a string: ') 

    def print_upper_string(self):
        print(self._string.upper())


if __name__ == '__main__':
    s = String()
    s.get_string()
    s.print_upper_string()