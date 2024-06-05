class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 5
        
    def get_descriptivename(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's milage."""
        print(f"This car has {self.odomoter_reading} miles on it.")
    
    
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptivename())
my_new_car.read_odometer() # This is not working for me
