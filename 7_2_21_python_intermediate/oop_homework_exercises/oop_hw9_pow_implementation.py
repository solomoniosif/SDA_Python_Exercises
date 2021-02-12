
# TODO: Write a Python class to implement pow(x, n)


class CustomPow:
    def __call__(self, base, exponent):
        if isinstance(base, int) and isinstance(exponent, int):
            return self.custom_pow(base, exponent)
        return 'This custom power function only works with integer base and exponent.'

    @staticmethod
    def custom_pow(base, exponent):
        def pos_exp_pow(base, exponent):
            result = 1
            for _ in range(exponent):
                result *= base
            return result
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base
        elif exponent > 0:
            return pos_exp_pow(base, exponent)
        elif exponent < 0:
            return 1 / pos_exp_pow(base, abs(exponent))


if __name__ =='__main__':
    custom_pow = CustomPow()
    print(custom_pow(2, -3), pow(2, -3))
    print(custom_pow(3, 5), pow(3, 5))
    print(custom_pow(100, 0), pow(100, 0))