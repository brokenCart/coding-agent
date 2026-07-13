from functions.run_python_file import run_python_file


def test_run_python_file():
    # Valid file within the working directory
    print(run_python_file("calculator", "main.py"))
    print("---\n")

    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("---\n")

    print(run_python_file("calculator", "tests.py"))
    print("---\n")

    # Outside the working directory
    print(run_python_file("calculator", "../main.py"))
    print("---\n")

    # Non-existent file
    print(run_python_file("calculator", "nonexistent.py"))
    print("---\n")

    # Non-Python file
    print(run_python_file("calculator", "lorem.txt"))
    print("---\n")


if __name__ == "__main__":
    test_run_python_file()
