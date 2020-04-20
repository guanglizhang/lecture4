class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):

        # Keep track of id number.
        self.id = Flight.counter
        Flight.counter += 1

        # Keep track of passengers.
        self.passengers = []

        # Details about flight.
        self.origin = origin
        self.destination = destination
        self.duration = duration

# Note that counter is defined outside of the __init__ function and is not specific to individual flights (it’s not defined as self.counter. 
# This means that all flight objects can see this same counter variable, which allows for the implementation the id property shown here. 
# Similar to the SQL database which had an auto-incrementing id column, 
# the id property of flights will automatically incrememt as new flight objects are created.

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

        print()
        print("Passengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id

# In add_passenger, p.flight_id is created, because flight_id is not defined in the Passenger class’s __init__.
# The passengers property of Flights is going to be a list of Passenger objects.

class Passenger:

    def __init__(self, name):
        self.name = name

def main():

    # Create flight.
    f1 = Flight(origin="New York", destination="Paris", duration=540)

    # Create passengers.
    alice = Passenger(name="Alice")
    bob = Passenger(name="Bob")

    # Add passengers.
    f1.add_passenger(alice)
    f1.add_passenger(bob)

    f1.print_info()


if __name__ == "__main__":
    main()
