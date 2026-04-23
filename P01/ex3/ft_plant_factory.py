class Plant:
    '''
    Class that represent a plant with name age and height
    '''
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


Rose = Plant("Rose", 25, 30)
Oak = Plant("Oak", 200, 365)
Cactus = Plant("Cactus", 5, 90)
Sunflower = Plant("Sunflower", 80, 54)
Fern = Plant("Fern", 15, 120)

plants = [Rose, Oak, Cactus, Sunflower, Fern]

print("=== Plant Factory Output ===")
for plant in plants:
    print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")

len_plants = len(plants)
print(f"\nTotal plants created: {len_plants}")
