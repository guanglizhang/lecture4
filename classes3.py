class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

    def delay(self, amount):
        self.duration += amount

# Note that writing methods like delay and print_info, 
# as well just the idea of Flight class in general, allow for abstraction. 

# The Flight class and all of its methods can be used in a logical and easily 
# understood way without needing to know or even understand how Flight may be implemented

def main():

    f1 = Flight(origin="New York", destination="Paris", duration=540)
    f1.delay(10)
    f1.print_info()


if __name__ == "__main__":
    main()
