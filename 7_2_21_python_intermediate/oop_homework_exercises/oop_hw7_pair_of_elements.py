
# TODO:Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
# * Input: numbers= [10,20,10,40,50,60,70], target=50
# * Output: 3, 4

class FindPair:
    def __call__(self, numbers: list, target: int):
        if (isinstance(numbers, list) or isinstance(numbers, tuple)) and isinstance(target, int):
            return self.find_pair(numbers, target)
        return "Input arguments must be a list of numbers and a target of type int."

    @staticmethod
    def find_pair(numbers, target):
        for i, n in enumerate(numbers):
            for i2, n2 in enumerate(numbers):
                if n + n2 == target and i != i2:
                    return i, i2
        return f'No pair of numbers found whose sum equals {target}.'


if __name__ == "__main__":
    find_pair = FindPair()

    print(find_pair([10,20,10,40,50,60,70], target=50))
    print(find_pair((1, 3, 7, 9, 21, 13), 20))
    print(find_pair([1,2,3,4,5], '2'))
    print(find_pair([1,2,3,4,5], 10))