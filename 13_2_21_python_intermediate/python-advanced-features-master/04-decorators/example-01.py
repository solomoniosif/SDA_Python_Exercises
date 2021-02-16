import functools


def example_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Wrapper: Before function execution")
        result = func(*args, **kwargs)
        print("Wrapper: After function execution")
        return result

    return wrapper


@example_decorator
def greetings(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    greetings("Jane")
