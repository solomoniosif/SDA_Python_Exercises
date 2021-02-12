
# TODO: Write a Python class to get all possible unique subsets from a set of distinct integers.
# * Input : [4, 5, 6]
# * Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

from itertools import combinations


class UniqueSubsets:
    def __call__(self, input_set):
        if isinstance(input_set, set) or isinstance(input_set, list):
            return self.get_all_unique_subsets(set(input_set))
        return "Input argument must be a set or list."

    @staticmethod
    def get_all_unique_subsets(input_set):
        all_subsets = set()
        for i in range(len(input_set)+1):
            i_combinations = combinations(input_set, i)
            for sub_set in i_combinations:
                all_subsets.add(sub_set)
        return sorted([list(sub_set) for sub_set in all_subsets])


if __name__ == "__main__":
    get_unique_subsets = UniqueSubsets()

    print(get_unique_subsets([4, 5, 6]))
    print(get_unique_subsets([]))
    print(get_unique_subsets({'a', 'b', 'x', 'y'}))
    print(get_unique_subsets('superset'))