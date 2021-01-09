
# ? Write a function which takes 3 arguments and print out which index of the 3 is the smallest. 
# ? Example: 0, 2 3. Output: The first one: 0 is the smallest

def get_smallest(a, b, c):
    if a <= b and a <= c:
        return  f"The first one: {a} is the smallest"
    elif b <= a and b <= c:
        return f"The second one: {b} is the smallest"
    else:
        return f"The third one: {c} is the smallest"

print(get_smallest(6,6,5))


def get_smallest2(a, b, c):
    smallest = min([a, b, c])
    smallest_index = [a, b, c].index(smallest)
    index_dic = {1: "first", 2: "second", 3: "third"}
    return f"The {index_dic[smallest_index+1]} one: {smallest} is the smallest"

print(get_smallest2(6,6,5))