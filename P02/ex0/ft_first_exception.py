def check_temperature(temp_str):
    '''
    function that checks the temp, and if it is valid or no
    '''
    print(f"Testing temperature: {temp_str}")

    try:
        n = int(temp_str)
        if n < 0:
            print(f"Error: {n}C is too cold for the plants (min 0C)\n")
        elif n > 40:
            print(f"Error: {n}C is too hot for plants (max 40C)\n")
        else:
            print(f"Temperature {n}C is perfect for plants!\n")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_tempurature_input():
    '''
    function that test the check_temperature function
    '''
    print("=== Garden Temperature Checker ===\n")

    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")

    print("All tests completed - program didin't crash!")


if __name__ == "__main__":
    test_tempurature_input()
