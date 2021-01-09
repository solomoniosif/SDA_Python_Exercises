import random

def multiply_by(factor):
    number = random.random() * 10000
    str_number = str(number)
    result = []
    remainder = 0
    for digit in reversed(str_number):
        if digit == '.':
            result.append(digit)
            continue
        f = int(digit) * factor + remainder
        result.append(str(f % 10))
        remainder = f // 10
    if remainder > 0:
        result.append(str(remainder))
    print()
    print(number)
    print(float(''.join(reversed(result))))

multiply_by(2)
multiply_by(5)

########################################################################
# 1. Am șters 'import math' pentru că modulul math nu era folosit nicăieri în cod
# 2. Am înlocuit '[::-1]' cu 'reversed()' în prima parte a codului pentru că e mai eficient și pentru consistență cu restul codului
# 3. Pentru a nu repeta codul am creat o funcție numită 'multiply_by' care acceptă ca parametru al doilea factor al înmulțirii
