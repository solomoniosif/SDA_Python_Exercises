
# ? Given dictionary {1: "one", 2: "two", 3: "three"}:
dict_1 = {1: "one", 2: "two", 3: "three"}
print(f"The inital dictionary: {dict_1}")

# ? a. Use len() to print out its length.
dict_length = len(dict_1)
print(f"a. The length of the dictionary: {dict_length}")

# ? b. Using set-item operator [], add a new key-pair: 4:"four".
dict_1[4] = "four"
print(
    f"b. The dictionary after using the set-item operator [] to add a new key-pair: 4:'four': {dict_1}")

# ? c. Using get-item operator [], print out the value assigned to key 2.
val_2 = dict_1[2]
print(f"c. The value assigned to '2': {val_2}")

# ? d. Using get-item operator [], print out value for unassigned key, like 10. What happens?
# ! If you uncomment the code below you will get a KeyError
# val_10 = dict_1[10]
# print(val_10)

# ? e. Using dictionary function get(key), replace the previous get-item operator [] and print
# ? out the value for key 10. What happens?
val_10_get = dict_1.get(10)
print(
    f"e. The return of get function applied to a nonexistent key in the dictionary without specifing a default value: {val_10_get}")

# ? f. Using dictionary function get(keĀ, default), print out the value for key 10, this time
# ? setting default value to "unknown".
val_10_get_default = dict_1.get(10, 'unknown')
print(
    f"f. The return of get function applied to a nonexistent key in the dictionary with a default value: {val_10_get_default}")

# ? g. Using dictionary function get(keĀ, default), print out the value for key 3. Set default
# ? value to "unknown".
val_3_get_default = dict_1.get(3, 'unknown')
print(
    f"g. The return of get function applied to a key that exists in the dictionary with a default value: {val_3_get_default}")

# ? h. Use pop() to print out value assigned to 2. Print out the dictionary after using pop().
val_2 = dict_1.pop(2)
print(f"h. The return value of .pop(2) function on the dictionary: {val_2}")
print(f"   The dictionary after poping the item '2': {dict_1}")

# ? i. Create a new dictionary {0: "zero"}. Using update(), update main dictionary with
# ? values from the new dictionary. Print out the main dictionary.
dict_2 = {0: "zero"}
dict_1.update(dict_2)
print(
    f"i. The initial dictionary after updating it with a new dictionary {{0: 'zero'}}: {dict_1}")

# ? j. Using clear(), clear the dictionary.
dict_1.clear()
print(f"j. The dictionary after clearing it: {dict_1}")
