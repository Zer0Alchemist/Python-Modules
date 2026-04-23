def check_plant_health(plant_name, water_level, sunlight_hours):
    '''
    function that checks plant health with error checkings aswell
    '''
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours}"
            f" is too high (max 12)")
    elif sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours}"
            f" is too low (min 2)")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    '''
    function that test check_plant_health function with and without errors
    '''
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    check_plant_health("tomato", 5, 6)

    print("\nTesting empty plant_name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 6)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunglight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
