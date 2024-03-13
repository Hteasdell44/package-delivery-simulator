class Truck:

    def __init__(self, truckId, packages, depart_time):
        # Initialize truck attributes
        self.truckId = truckId
        self.capacity = 16
        self.speed = 18
        self.load = None
        self.packages = packages
        self.mileage = 0
        self.address = "4001 South 700 East"
        self.depart_time = depart_time
        self.time = depart_time

    def __str__(self):
        # Return a formatted string representation of the truck
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.truckId, self.capacity, self.speed, self.load, self.packages, self.mileage, self.address, self.depart_time)