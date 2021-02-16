
class FileOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.opened_file = None

    def __enter__(self):
        print("Opening file")
        self.opened_file = open(self.filename, self.mode)
        return self.opened_file

    def __exit__(self, *exc):
        print("Closing file")
        self.opened_file.close()
        self.opened_file = None

    
if __name__ == "__main__":
    file_path = "D:\\Python\\SDA_Python\\README.md"
    with FileOpen(file_path, 'r') as f:
        for line in f.readlines():
            print(line)
    print("Finished.")
