# Super class
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Sub class
class Player(Person):
    def __init__(self, name, age, number, position):

        # notice: donot type in self in super init method
        super().__init__(name, age)
        
        self.number = number
        self.position = position
