letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'z', 'r', 't', 'q']
numbers = [2, 5, 7, 10, 22, 5, 7, 1]

letters.append("y")
numbers.extend([3, 54, 12])

sorted_letters = sorted(letters)
numbers.sort()

print(sorted_letters)
print(numbers)
