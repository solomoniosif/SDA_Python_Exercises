
# TODO: Create a class using dataclass that:

    # * will have 4 constructor arguments:
        # => first_int by int type
        # => multiplier by int type
        # => list_of_ints by int list type
        # => second_int by int type and default value 0
    # * will have 1 field:
        # => calculated_val by float type
    # => calculated_val value is (first_int * multiplier * sum(list_of_ints)) - second_int
    # => comparing objects is to be based only on the values of the calculated_val field
    # => the created object should be callable and as a result of execution, return the value of the calculated_val field
    # => the form of displaying the object by the print function is to be as shown below in the examples:

#           ... t = Test(2, 2, [2, 1], 9)
#           ... print(t)
#           ... print(t())
#           Test(calculated_val=3)
#           3

#           ... t1 = Test(3, 2, [2, 2], 1)
#           ... t2 = Test(4, 1, [2, 4], 1)
#           ... print(t1 == t2)
#           True

from dataclasses import dataclass


@dataclass
class Test:
    first_int: int
    multiplier: int
    list_of_ints: list
    second_int: int

    def calculated_val(self):
        return self.first_int * self.multiplier * sum(self.list_of_ints) - self.second_int

    def __str__(self):
        return f"Test(calculated_val={self.calculated_val()})"

    def __repr__(self):
        return f"Test(first_int={self.first_int}, multiplier={self.multiplier}, list_of_ints={self.list_of_ints}, second_int={self.second_int})"

    def __call__(self):
        return self.calculated_val()

    def __eq__(self, other):
        if isinstance(other, Test):
            return self.calculated_val() == other.calculated_val()
        return NotImplemented


if __name__ == '__main__':
    t = Test(2, 2, [2, 1], 9)

    print(t)
    print(t())

    t1 = Test(3, 2, [2, 2], 1)
    t2 = Test(4, 1, [2, 4], 1)

    print(t1 == t2)