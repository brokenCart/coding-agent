from functions.write_file import write_file


def test_write_file():
    # Valid path within the working directory
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("---\n")

    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("---\n")

    # Outside the working directory
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print("---\n")


if __name__ == "__main__":
    test_write_file()
