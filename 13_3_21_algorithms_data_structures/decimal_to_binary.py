def decimal_to_binary(d):
    """Function that returns the binary representation of a deciaml number"""
    if d < 0:
        raise ValueError("Number must be >= 0")
    if d == 0:
        return 0
    binary_string = ''
    while d > 0:
        r = d % 2
        if r == 1:
            binary_string = '1' + binary_string
        else:
            binary_string = '0' + binary_string
        d = d // 2
    return '0b' + binary_string


print(decimal_to_binary(122))


def from_base10(num, base):
    """Functions that returns a representation of a number from base 10 to a different base.
    Current implementation only supports converting up to base 10"""
    if base < 2:
        raise ValueError('Base must be >= 2')
    if num < 0:
        raise ValueError('Number must be > 0')
    if num == 0:
        return 0
    num_string = ''
    while num > 0:
        num, r = divmod(num, base)
        num_string = str(r) + num_string
    return num_string


print(from_base10(122, 6))
