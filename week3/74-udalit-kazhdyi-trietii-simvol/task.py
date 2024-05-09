import io


def main():
    with (open("input.txt") as input_file,
          open("output.txt", "w") as output_file):
        stream = FileCharStream(input_file)
        i = 0
        for char in stream:
            if i % 3 != 0:
                output_file.write(char)
            i += 1


class FileCharStream:
    def __init__(self, file):
        self.f = file
        pass

    def __iter__(self):
        return self

    def __next__(self):
        self.current = self.f.read(1)
        if self.current != "":
            return self.current
        raise StopIteration


if __name__ == "__main__":
    main()
