
# TODO: Write a Python class to convert a roman numeral to an integer.

class RomanToInt:
    ROMAN_NUMERALS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'V̅': 5000, 'X̅': 10000, 'L̅': 50000, 'C̅': 100000, 'D̅': 500000, 'M̅': 1000000, u'\u0305': ''}
    def __call__(self, value):
        if isinstance(value, str) and all([ch in RomanToInt.ROMAN_NUMERALS for ch in value]):
            return self.roman_to_int(value)
        return "Provided value is not a valid roman numeral or is greater than 1000000."

    @staticmethod
    def roman_to_int(roman_num):
        def get_ch(roman_num):
            if len(roman_num) == 1:
                return roman_num[0], 1
            if roman_num[1] == u'\u0305':
                return roman_num[:2], 2
            return roman_num[0], 1

        ch_list = []
        while roman_num:
            current_ch,  ch_len = get_ch(roman_num)
            ch_list.append(RomanToInt.ROMAN_NUMERALS[current_ch])
            roman_num = roman_num[ch_len:]

        result = sum(ch_list)
        for i in range(len(ch_list)-1):
            if ch_list[i] < ch_list[i+1]:
                result -= ch_list[i] * 2
        return result


if __name__ == '__main__':
    roman_to_int = RomanToInt()

    print(roman_to_int('XC')) # 90
    print(roman_to_int('MMXXI')) # 2021
    print(roman_to_int('C̅MMMDCCLXXXIX')) # 103789
    print(roman_to_int('C̅M̅L̅X̅X̅X̅MX̅DCCCXCVIII')) # 989898
