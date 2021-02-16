# Write a timeit context manager which saves a current time.time() value on entry
# and prints time passed since entry on exit. Try splitting the following chunk of text a
# million times inside the context to test it. Use punctuation mark as a delimiter. 

import time


class Timeit:
    def __enter__( self ):
        self.start_time = time.time()
        
    def __exit__(self, *exc):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {round(elapsed_time, 4)}")

sample_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
officia deserunt mollit anim id est laborum.
"""

with Timeit():
    for _ in range(1_000_000):
        sample_text.split(',')
