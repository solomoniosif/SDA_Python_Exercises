import functools


def html_tag(tag_name):
    def wrapper(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{tag_name}>{result}</{tag_name}>"

        return wrap

    return wrapper


@html_tag("h1")
def prepare_h1_title(title_string):
    return title_string.title()


@html_tag("h2")
def prepare_h2_title(title_string):
    return title_string.lower()


if __name__ == "__main__":
    print(prepare_h1_title("a H1 title!"))
    print(prepare_h2_title("a H2 subtitle!"))
