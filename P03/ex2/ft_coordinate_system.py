import math


def pos_create(number: str):
    try:
        string = number.split(",")
        parts = [int(num) for num in string]
        pos = tuple(parts)
        zeros = (0, 0, 0)

        x2, y2, z2 = pos
        x1, y1, z1 = zeros
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

        print(f"Position created: {pos}")
        print(f"Distance between {zeros} and {pos}: {distance:.2f}")
    except ValueError as e:
        print(f"Error creating position: {e}")


def pars(number: str):
    print(f"\nParsing coordinates: \"{number}\"")
    try:
        string = number.split(",")
        parts = [int(num) for num in string]
        nums = tuple(parts)
        zero = [0, 0, 0]
        zeros = tuple(zero)

        x2, y2, z2 = nums
        x1, y1, z1 = zeros
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

        print(f"Parsed position: {nums}")
        print(f"Distance between {zeros} and {nums}: {distance:.2f}")
    except ValueError as e:
        (message, ) = e.args
        print(f"Error parsing coordinates: {message}")
        print(f"Error details - Type: ValueError, Args: (\"{message}\")")


def unpack(number: str):
    try:
        string = number.split(",")
        parts = [int(num) for num in string]
        number = tuple(parts)

        x, y, z = number

        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except ValueError as e:
        print(f"Error unpacking: {e}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    pos_create("10,20,5")

    pars("3,4,0")

    pars("abc,def,ghi")

    print("\nUnpacking demonstration")
    unpack("3,4,0")
