class GardenError(Exception):
    '''
    class that inherit from the Exception class
    '''
    pass


class PlantError(GardenError):
    '''
    Class that inherit from the GardenError class
    '''
    pass


class WaterError(GardenError):
    '''
    class that inherit from the GardenError class
    '''
    pass


class GardenManager:
    '''
    Class that manages the garden with adding plants
    and checking errors
    '''
    def __init__(self):
        '''
        A constructor that initialize the object and its attributes
        '''
        self.plants = []

    def add_plant(self, plant):
        '''
        A method that check plant's name validity and add it to the list
        '''
        if plant is None:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant)
        print(f"Added {plant} successfully")

    def water_plants(self):
        '''
        Method that simulate plants watering process
        '''
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant is None:
                    raise WaterError(f"Cannot water {plant} - invalid plant")
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Error : {e}")
        finally:
            print("Closing Watering system (cleanup)")

    def plant_health(self, name, water_level, sun_level):
        '''
        A method that checks the plant's health
        '''
        if name is None:
            raise PlantError("Plant name cannot be empty!")
        elif water_level < 1:
            raise WaterError(f"Water level {water_level} is too low (min 1)")
        elif water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        elif sun_level < 2:
            raise PlantError(f"Sunlight hours {sun_level} is too low (min 2)")
        elif sun_level > 12:
            raise PlantError(f"Sunlight hours {sun_level} is too high(max 12)")
        else:
            print(f"{name}: healthy (water: {water_level}, sun: {sun_level})")

    def recovery(self):
        '''
        a method that proves the class inheritence between GardenError
        WaterError
        '''
        raise WaterError("Not enough water in tank")


def test_garden():
    '''
    A function that test all methods and the errors
    '''
    print("=== Garden Management System ===\n")

    plant = GardenManager()
    print("Adding plants to garden...")
    plant.add_plant("tomato")
    plant.add_plant("lettuce")
    try:
        plant.add_plant(None)
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    plant.water_plants()

    print("\nChecking plant health...")
    plant.plant_health("tomato", 5, 8)
    try:
        plant.plant_health("lettuce", 15, 8)
    except WaterError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        plant.recovery()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("system recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden()
