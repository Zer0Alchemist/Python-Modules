class Plant:
    '''
    Represents a plant with name, height and age
    '''
    def __init__(self, name, height, age):
        '''
        A constructor that automatically initialize an object and
        its attributes
        '''
        self.name = name
        self.height = height
        self.age = age


Rose = Plant("Rose", 25, 30)
Sunflower = Plant("Sunflower", 80, 45)
Cactus = Plant("Cactus", 15, 120)

print("=== Garden Plant Registry ===")
print(f"{Rose.name}: {Rose.height}cm, {Rose.age} days old")
print(f"{Sunflower.name}: {Sunflower.height}cm, {Sunflower.age} days old")
print(f"{Cactus.name}: {Cactus.height}cm, {Cactus.age} days old")
