# Given the following list_1
list_1 = [1, 2, 3, 4, 5]
print(f"The initial list_1: {list_1}")
# a. Use len() to print its length.
length = len(list_1)
print(f"The length of the list_1 is: {length}")
# b. Use append() to append a sixth element: another 2.
list_1.append(2)
print(f"The list_1 after appending 2: {list_1}")
# c. Use count() to count the 2s in list_1.
count_of_2 = list_1.count(2)
print(f"Count of '2' in list_1: {count_of_2}")
# d. Use the same function to count 7s, which are not in the list_1. What's the result?
count_of_7 = list_1.count(7)
print(f"Count of '7' in list_1: {count_of_7}")
# e. Use extend() to extend it with: [6, 7, 8].
list_1.extend([6, 7, 8])
print(f"The list_1 after appending '[6, 7, 8]': {list_1}")
# f. Use index() to check index of the 7. Use indexing to check you got the correct result.
index_of_7 = list_1.index(7)
print(f"The index of 7: {index_of_7}")
# g. Use insert() to add a value 10 at index 0. Print the list_1 to check what it did.
list_1.insert(0, 10)
print(f"The list_1 after inserting '10' at index 0: {list_1}")
# h. Use [-1] indexing to check the value of the last element.
last_element = list_1[-1]
print(f"The last element in the list_1: {last_element}")
# i. Use pop() to check the value of the last element, removing it from the list_1.
last_element_poped = list_1.pop()
print(
    f"This is the last element: {last_element_poped}. And this is the list_1 after popping the last element: {list_1}")
# j. Use remove() to delete 4 from the list_1.
list_1.remove(4)
print(f"This is the list_1 after removing 4: {list_1}")
# k. Use reverse() and print the list_1..
list_1.reverse()
print(f"This is the list_1 after reversing it: {list_1}")
# l. Use sort() and print it again.
list_1.sort()
print(f"This is the list_1 after sorting it: {list_1}")
# m. Use clear() to empty the list_1.
list_1.clear()
print(f"This is the list_1 after clearing it: {list_1}")
# [1:10 PM]  Given list_1 users = ["User1", "UserChris", "User2", "Admin"]:
users = ["User1", "UserChris", "User2", "Admin"]
print(f"\nThe initial 'users' list: {users}")
# a. Print out a slice containing only "User2".
user_2 = users[2:3]
print(
    f"This is the slice containing only the third element from 'users' list: {user_2}")
# b. Print out a slice of all users, except the first one.
users_except_first = users[1:]
print(
    f"This is a slice of 'users' list except the first one: {users_except_first}")
# c. Print out a slice of all users, except the "Admin".
users_except_admin = users[:-1]
print(
    f"This is a slice of 'users' list except the last one: {users_except_admin}")
# d. Print out a slice of all users up to the 3rd one.
first_three_users = users[:3]
print(f"This is a slice of 'users' up to the third one: {first_three_users}")
