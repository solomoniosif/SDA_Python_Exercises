"""
Write a `timeit` context manager which saves a current `time.time()` 
value on entry and prints time passed since entry on exit. Try 
splitting the following chunk of text a million times inside the 
context to test it. Use punctuation mark as a delimiter.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do 
    eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut 
    enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
    in reprehenderit in voluptate velit esse cillum dolore eu 
    fugiat nulla pariatur. Excepteur sint occaecat cupidatat non 
    proident, sunt in culpa qui officia deserunt mollit anim id est
    laborum.
"""
import time
import contextlib


@contextlib.contextmanager
def timeit():
    start_time = time.time()
    yield
    delta_time = time.time() - start_time
    print(f"Operation took {delta_time:.3f}s")


if __name__ == "__main__":
    paragraph = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do 
    eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut 
    enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
    in reprehenderit in voluptate velit esse cillum dolore eu 
    fugiat nulla pariatur. Excepteur sint occaecat cupidatat non 
    proident, sunt in culpa qui officia deserunt mollit anim id est
    laborum.
    """

    with timeit():
        for _ in range(1_000_000):
            paragraph.split(".")
