from functions.get_file_content import get_file_content


def test_get_file_content():
    # Valid file paths within the working directory
    # Truncation for large files
    print("Result for 'lorem.txt' file:")
    result = get_file_content("calculator", "lorem.txt")
    print(result)
    print(f"lorem.txt truncated: {'truncated' in result}")
    print("---\n")

    # No truncation for small files
    print("Result for 'main.py' file:")
    result = get_file_content("calculator", "main.py")
    print(result)
    print(f"main.py truncated: {'truncated' in result}")
    print("---\n")

    print("Result for 'pkg/calculator.py' file:")
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)
    print(f"pkg/calculator.py truncated: {'truncated' in result}")
    print("---\n")

    # Outside the working directory
    print("Result for '/bin/cat' file:")
    result = get_file_content("calculator", "/bin/cat")
    print(result)
    print("---\n")

    print("Result for '../main.py' file:")
    result = get_file_content("calculator", "../main.py")
    print(result)
    print("---\n")

    # Non-existent file
    print("Result for 'pkg/does_not_exist.py' file:")
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)
    print("---\n")


if __name__ == "__main__":
    test_get_file_content()
