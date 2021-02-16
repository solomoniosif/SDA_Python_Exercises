class HTMLHeader:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return f"<h1>{result}</h1>"


@HTMLHeader
def prepare_title(title_string):
    return title_string.title()


if __name__ == "__main__":
    print(prepare_title("this is a section title!"))
