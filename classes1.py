class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration


def main():

    # Create flight.
    f = Flight(origin="New York", destination="Paris", duration=540)

    # Change the value of a variable.
    f.duration += 10

    # Print details about flight.
    print(f.origin)
    print(f.destination)
    print(f.duration)

if __name__ == "__main__":
    main()

# Note that only flight information is passed in to Flight(); 
# the self argument to the __init__ method is automatically specified.
# f is a variable of type Flight, just like a variable might be of type str or int.
