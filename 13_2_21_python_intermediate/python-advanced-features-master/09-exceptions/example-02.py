try:
    print("First statement")
    print("Second statement")
    raise Exception("Oh no!")
    print("Final statement")
except Exception:
    print("An exception occurred!")


try:
    l = []
    print(l[10])
except IndexError:
    print("IndexError has ocurred!")
