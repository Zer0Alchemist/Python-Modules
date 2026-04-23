class Plant:
    '''
    A class that represent a plant growth overtime
    '''
    def __init__(self, name, height, age):
        '''
        a constructor that initialize the object
        and its attributes
        '''
        self.name = name
        self.height = height
        self.plant_age = age

    def grow(self):
        '''
        method that increase height by 1
        '''
        self.height += 1

    def age(self):
        '''
        method that increase age by 1
        '''
        self.plant_age += 1

    def get_info(self):
        '''
        method that prints the info about the plant
        '''
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


Rose = Plant("Rose", 25, 30)
Carrot = Plant("Carrot", 20, 50)
plants = [Rose, Carrot]

print("=== Day 1 ===")
for i in plants:
    i.get_info()

for i in range(2, 8):
    print(f"=== Day {i} ===")
    for plant in plants:
        plant.grow()
        plant.age()
        plant.get_info()

print("Growth this week: +6cm")
