class SecurePlant:
    '''
    A class that represent a plant with protected attributes
    '''
    def __init__(self, name, height, age):
        '''
        Constructor that initialize the object and
        its attributes
        '''
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        '''
        method that returns the current height
        '''
        return self._height

    def set_height(self, x):
        '''
        method that sets the plant height if it is valid
        '''
        if x < 0:
            print(
                f"Invalid operation attempted: height {x}cm"
                f" [REJECTED]"
                )
            print("Security: Negative height rejected")
        else:
            self._height = x

    def get_age(self):
        '''
        method that returns the current age
        '''
        return self._age

    def set_age(self, x):
        '''
        method that sets the plant age if it is valid
        '''
        if x < 0:
            print(f"Invalid operation attempted: age {x} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = x


Rose = SecurePlant("Rose", 25, 30)

print("=== Garden Security System ===")
print(f"Plant created: {Rose.name}")
print(f"Height updated: {Rose.get_height()}cm [OK]")
print(f"Age updated: {Rose.get_age()} days [OK]")
print("")
Rose.set_height(-5)
print(
    f"\nCurrent plant : {Rose.name} ({Rose.get_height()}cm,"
    f" {Rose.get_age()} days)"
     )
