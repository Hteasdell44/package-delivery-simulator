class Truck:

    def __init__(self, capacity, speed, load, packages, mileage, address, depart_time):
        # Initialize truck attributes
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time

    def __str__(self):
        # Return a formatted string representation of the truck
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages, self.mileage, self.address, self.depart_time)
