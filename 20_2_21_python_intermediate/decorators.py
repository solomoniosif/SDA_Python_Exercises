def to_upper(func):
    print('Am apelat decoratorul')

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@to_upper
def hello(name):
    return f"Hello {name}"

# hello = to_upper(hello)
# print(to_upper(hello)('Iosif'))
# hello_to_upper = to_upper(hello)
# print(hello_to_upper('Iosif'))
