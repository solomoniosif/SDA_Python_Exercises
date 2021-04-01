from contextlib import contextmanager


@contextmanager
def file_manager(name, mode):
    f = open(name, mode)
    yield f
    f.close()


if __name__ == '__main__':
    with file_manager('test.txt', 'w') as f:
        f.write('hello')
