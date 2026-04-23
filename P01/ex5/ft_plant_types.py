class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


Rose = Flower("Rose", 25, 30, "red")
Lavender = Flower("Lavender", 40, 45, "purple")
Oak = Tree("Oak", 500, 1825, 50)
Pine = Tree("Pine", 300, 730, 15)
Tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
Carrot = Vegetable("Carrot", 20, 60, "autumn", "vitamin A")

print("=== Garden Plant Types ===")
print(
    f"{Rose.name} (Flower): {Rose.height}cm,"
    f" {Rose.age} days, {Rose.color} color")
print(
    f"{Lavender.name} (Flower): {Lavender.height}cm,"
    f" {Lavender.age} days, {Lavender.color} color")
Rose.bloom()
Lavender.bloom()
print(
    f"\n{Oak.name} (Tree): {Oak.height}cm,"
    f" {Oak.age} days, {Oak.trunk_diameter} diameter")
print(
    f"{Pine.name} (Tree): {Pine.height}cm,"
    f" {Pine.age} days, {Pine.trunk_diameter} diameter")
Oak.produce_shade()
Pine.produce_shade()
print(
    f"\n{Tomato.name} (Vegetable): {Tomato.height}cm,"
    f" {Tomato.age} days, {Tomato.harvest_season} harvest")
print(f"{Tomato.name} is rich in {Tomato.nutritional_value}")
print(
    f"{Carrot.name} (Vegetable): {Carrot.height}cm,"
    f" {Carrot.age} days, {Carrot.harvest_season} harvest")
print(f"{Carrot.name} is rich in {Carrot.nutritional_value}")
