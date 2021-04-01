"""Given function random_exception which raises a random exception every time,
write a try-except block which handles each of the possible exceptions by counting
their occurrences. Print the tally."""
import random


def get_all_subclasses(cls):
    all_subclasses = []

    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))

    return list(set(all_subclasses))


all_exceptions = get_all_subclasses(Exception)


def raise_random_exception(list_of_exceptions):
    raise random.choice(list_of_exceptions)


def count_exceptions(run_times):
    exceptions_count = {ex.__name__: 0 for ex in all_exceptions}
    for _ in range(run_times):
        try:
            raise_random_exception(all_exceptions)
        except Exception as ex:
            ex = ex.__class__.__name__
            exceptions_count[ex] += 1
    return exceptions_count


if __name__ == "__main__":
    ex_count = count_exceptions(50)
    for exception, count in sorted(ex_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{exception}: {count}")
    print(f"\nTotal exceptions: {sum([count for count in ex_count.values()])}")
