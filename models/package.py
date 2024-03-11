class Package:

    def __init__(self, packageID, address, city, state, zip_code, deadline, weight, status):
        # Initialize package attributes
        self.ID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        # Return a formatted string representation of the package
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip_code, self.deadline, self.weight, self.delivery_time, self.status)

    def update_status(self, convert_timedelta):
        # Update the status of the package based on the provided time

        # Check if the package has been delivered
        if self.delivery_time < convert_timedelta:
            self.status = "Delivered!"

        # Check if the package is currently en route
        elif self.departure_time > convert_timedelta:
            self.status = "En Route!"

        # If neither condition is met, the package is at the hub
        else:
            self.status = "At The Hub!"