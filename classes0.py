class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration


# __init__ is a ‘method’, which is a function performed on individual objects. 
# __init__ in particular is a special, built-in method that describes what should happen when a flight object is created.
# Generally, methods take self as their first argument. self refers to the object being worked with. 
# The other three arguments are simply the information that should be stored about a particular flight. 
# That information is stored as ‘properties’ inside the object, using dot notation.