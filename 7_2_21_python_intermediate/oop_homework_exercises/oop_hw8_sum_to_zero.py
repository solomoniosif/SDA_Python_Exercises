
#  TODO: Write a Python class to find the three elements that sum to zero from a set of n real numbers.
# * Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# * Output : [[-10, 2, 8], [-7, -3, 10]]

from itertools import combinations

class SumToZero:
    def __call__(self, input_list):
        if isinstance(input_list, list) and len(input_list) >= 3:
            return self.sum_to_zero(input_list)
        return "Input argument must be a list of at least 3 integers."

    @staticmethod
    def sum_to_zero(input_list):
        zero_sum_combinations = []
        for combination in combinations(input_list, 3):
            if sum(combination) == 0:
                zero_sum_combinations.append(list(combination))
        return zero_sum_combinations if zero_sum_combinations else "No combination of 3 numbers whose sum equals 0 was found in given list."


if __name__ =='__main__':
    sum_to_zero = SumToZero()

    print(sum_to_zero([-25, -10, -7, -3, 2, 4, 8, 10]))
    print(sum_to_zero([1, 2, -3, -2, -5, -6, 5, -7, 3, 4, -9]))
    print(sum_to_zero([-5, 34, 21, -19, 93]))
    print(sum_to_zero([-5, 5]))