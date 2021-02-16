"""
1. Write a parametric decorator `check_types` which takes any number of class names 
and checks whether each of the function `args` is instance of respective class. If 
not - print a warning.
2. Use it with a function of your invention."
"""
import functools


def check_types(*wrapper_args):
    def wrapper(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            for i, arg in enumerate(args):
                if not isinstance(arg, wrapper_args[i]):
                    print(
                        f"Warning: argument #{i+1} ({arg}) is not an instance of {wrapper_args[i]}!"
                    )
            return func(*args, **kwargs)

        return wrap

    return wrapper


@check_types(str, str, int)
def record(name, surname, age):
    return {"name": name, "surname": surname, "age": age}


if __name__ == "__main__":
    record("Alan", "Moore", 60)  # should proceed without a warning
    record("Bethany", "Smiles", 70.5)  # should print a warning
