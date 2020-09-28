class Job():
    def __init__(self, arrival, length):
        self.arrival = arrival
        self.length = length

        self.virtual_start = None
        self.virtual_finish = None

    def __str__(self):
        return "arrival: " + str(self.arrival) + ", length: " + str(self.length)