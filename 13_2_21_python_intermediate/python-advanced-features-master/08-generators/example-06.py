import time
import itertools

start_time = time.time()
list_of_cubes = [x ** 3 for x in range(1_000_000)]
delta = time.time() - start_time
print(f"Creating a list of 1 000 000 cubes in memory took {delta:03f}s")

start_time = time.time()
generator_of_cubes = (x ** 3 for x in range(1_000_000))
delta = time.time() - start_time
print(f"Creating a generator of 1 000 000 cubes in memory took {delta:03f}s")

print(list_of_cubes[:10])
print(list(itertools.islice(generator_of_cubes, 10)))
