
# TODO: Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
# * These brackets must be close in the correct order, 
# * for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

from collections import defaultdict

class CheckBrackets:
    def __call__(self, value):
        if isinstance(value, str) and all([ch in '()[]{}' for ch in value]):
            return self.valid_brackets(value)
        return "The argument of the function must be a string and can only contain brackets."

    @staticmethod
    def valid_brackets(brackets_string):
        brackets = defaultdict(lambda: "N/A")
        brackets['('] = ')' 
        brackets['['] = ']'
        brackets['{'] = '}'
        while brackets_string:
            if len(brackets_string) == 1:
                break
            if brackets[brackets_string[0]] == brackets_string[1]:
                brackets_string = brackets_string[2:]
            else:
                break
        return len(brackets_string) == 0


if __name__ == '__main__':
    check_valid_brackets = CheckBrackets()
    print(check_valid_brackets("(){}[]"))
    print(check_valid_brackets("()[{)}"))
    print(check_valid_brackets("()"))
    print(check_valid_brackets("(){}[]{}["))