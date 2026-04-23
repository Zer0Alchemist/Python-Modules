def water_plants(plants_list):
    '''
    function that water plants and check for an error
    '''
    print("Opening watering system")

    try:
        for plant in plants_list:
            print("Watering " + plant)
    except TypeError:
        print(f"Error: Cannot water {plant} - Invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    '''
    function that test water_plants function with and without errors
    '''
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(["tomato", None])

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
