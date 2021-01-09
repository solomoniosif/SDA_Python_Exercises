import random
import math

aa = random.random() * 10000
print(aa)
print(type(aa))
b = str(aa)

print(b)
print(type(b))


# result = []
# r = 0
# for d in b[::-1]:
#     if d == '.':
#         result.append(d)
#         continue
#     e = int(d)
#     f = e * 2 + r
#     result.append(str(f % 10))
#     r = f // 10
# if r > 0:
#     result.append(str(r))
# print(aa)
# print(''.join(reversed(result)))
# print()
# aaa = random.random() * 10000
# b = str(aaa)
# result = []
# r = 0
# for d in b[::-1]:
#     if d == '.':
#         result.append(d)
#         continue
#     e = int(d)
#     f = e * 5 + r
#     result.append(str(f % 10))
#     r = f // 10
# if r > 0:
#     result.append(str(r))
# print(aaa)
# print(''.join(reversed(result)))
