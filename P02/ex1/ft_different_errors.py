def garden_operations():
    '''
    function that checks python built in errors
    '''
    print("Testing ValueError...")
    try:
        n = int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        nb = 5 / 0
        print(f"{nb}")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        something = {"idk": 50}
        print(something["plant"])
    except KeyError:
        print("Caught KeyError: 'missing: plant'\n")

    print("Testing multiple errors together...")
    try:
        x = 4 / 0
        n = int("abc")
        open("bruh.txt")
        something = {"lol": 67}
        print(f"{x}, {something['peee']}, {n}")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


def test_error_types():
    '''
    function that test garden_operations function
    '''
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
