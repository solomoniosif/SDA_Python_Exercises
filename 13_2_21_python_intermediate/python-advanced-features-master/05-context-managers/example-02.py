"""example-02.py reimplements FileOpen from example-01.py as a
function-based context manager"""
import contextlib


@contextlib.contextmanager
def file_open(filename, mode):
    print("Opening file")
    f = open(filename, mode)
    print("Starting with... block")
    yield f  # yield keyword will be discussed more closely in 'Generators' module
    print("Closing file")
    f.close()


if __name__ == "__main__":
    path = "05-context-managers/example-01.py"
    with file_open(path, "r") as f:
        print(f"{path} has {len(f.readlines())} lines")

    print("Finished")
