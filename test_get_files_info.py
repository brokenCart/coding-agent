from functions.get_files_info import get_files_info


def test_get_files_info():
    # Valid directory within the working directory
    print("Result for current directory:")
    print(get_files_info("calculator", "."))
    print("---\n")

    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))
    print("---\n")

    # Outside the working directory
    print("Result for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))
    print("---\n")

    print("Result for '../' directory:")
    print(get_files_info("calculator", "../"))
    print("---\n")

    # Not a directory
    print("Result for 'main.py' file:")
    print(get_files_info("calculator", "main.py"))
    print("---\n")

    # Non-existent directory
    print("Result for 'non_existent_dir' directory:")
    print(get_files_info("calculator", "non_existent_dir"))
    print("---\n")


if __name__ == "__main__":
    test_get_files_info()
