class GardenError(Exception):
    '''
    A child class for Exception class and parent class for other classes
    '''
    pass


class PlantError(GardenError):
    '''
    Child class for GardenError class and made for plant errors
    '''
    pass


class WaterError(GardenError):
    '''
    Child class for GardenError class and made for water errors
    '''
    pass


def plant_error():
    '''
    function that makes an user made error message for plant errors
    '''
    raise PlantError("The tomato plant is wilting!")


def water_error():
    '''
    function that makes an user made error message for water errors
    '''
    raise WaterError("Not enough water in the tank!")


def test_errors():
    '''
    function that test the user made error messages
    '''
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        plant_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
