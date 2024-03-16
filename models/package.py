import datetime
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

    # Return a formatted string representation of the package
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip_code, self.deadline, self.weight, self.delivery_time, self.status)

    # Update the status of the package based on the provided time
    def update_status(self, convert_timedelta):
        # Prevents trucks two and three from leaving before their designated times.
        if self.ID in [2, 4, 5, 7, 8, 9, 10, 11, 12, 25, 28, 32, 33] and convert_timedelta < datetime.timedelta(hours=10, minutes=20) or self.ID in [3, 6, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39] and convert_timedelta < datetime.timedelta(hours=9, minutes=5):
            self.status = "At The Hub!"

        # Prevents any truck from leaving before 8, if after 8 and elgible to leave the package is marked en route.
        elif convert_timedelta >= datetime.timedelta(hours=8):
            self.status = "En Route!"

        # Check if the package has been delivered
        if self.delivery_time <= convert_timedelta:
            self.status = "Delivered!"