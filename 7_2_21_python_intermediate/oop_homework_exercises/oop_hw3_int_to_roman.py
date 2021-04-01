# TODO: Write a Python class to convert an integer to a roman numeral.

class IntToRoman:
    def __call__(self, value):
        if isinstance(value, int):
            return self.generate_roman_numeral(value)
        return "Can only convert an integer to a roman numeral."

    @staticmethod
    def generate_roman_numeral(arabic_num):
        roman_numerals = {1: ('I', 'V', 'X'),
                          2: ('X', 'L', 'C'),
                          3: ('C', 'D', 'M'),
                          4: ('M', 'V̅', 'X̅'),
                          5: ('X̅', 'L̅', 'C̅'),
                          6: ('C̅', 'D̅', 'M̅')
                          }

        def partial(n, level):
            one, five, ten = roman_numerals[level]
            if n == 0:
                return ""
            elif n == 1:
                return one
            elif n == 2:
                return one * 2
            elif n == 3:
                return one * 3
            elif n == 4:
                return one + five
            elif n == 5:
                return five
            elif n == 6:
                return five + one
            elif n == 7:
                return five + (one * 2)
            elif n == 8:
                return five + (one * 3)
            elif n == 9:
                return one + ten

        result = ""
        level = len(str(arabic_num))
        for n in str(arabic_num):
            result += partial(int(n), level)
            level -= 1
        return result


if __name__ == "__main__":
    int_to_roman = IntToRoman()

    print(int_to_roman(90))  # XC
    print(int_to_roman(2021))  # MMXXI
    print(int_to_roman(99000))  # X̅C̅MX̅
    print(int_to_roman(989898))  # C̅M̅L̅X̅X̅X̅MX̅DCCCXCVIII
