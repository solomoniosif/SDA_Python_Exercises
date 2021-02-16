class FileOpen:
    """FileOpen is an illustration of Context Manager's body,
    it does almost exactly what `with open() as ...` does"""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.opened_file = None

    def __enter__(self):
        print("Opening file")
        self.opened_file = open(self.filename, self.mode)
        return self.opened_file  # this enables us to use `as ...`

    def __exit__(self, *exc):
        print("Safely closing file")
        self.opened_file.close()


if __name__ == "__main__":
    path = "05-context-managers/example-01.py"
    with FileOpen(path, "r") as f:
        print(f"{path} has {len(f.readlines())} lines")

    print("Finished")
