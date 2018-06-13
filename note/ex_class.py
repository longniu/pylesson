# define a Car class
class Car:
    # class parameter
    count = 0
    maker = "PEACE"
    
    # inital method
    def __init__(self, color = "white") :
        Car.countup()
        self.mynumber = Car.count
        self.color = color
        self.mileage = 0

    # instanse Method
    def drive(self, km) :
        self.mileage += km
        msg = f"Drived {km}km. And total mile age is {self.mileage} km."
        print(msg)

    # class method
    @classmethod
    def countup(cls) :
        cls.count += 1
        print(f"Produced : {cls.count} cars")
