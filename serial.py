"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__ (self, start=0):
        """ Initialize new generator with start and next starting at start """
        self.start = self.next = start

    def __repr__(self):
        """ Show generator specs """

        return f'Start serial#: {self.start}. Next serial# in sequence: {self.next}.'

    def generate(self):
        """ Start with start serial# and then continue to generate subsequent numbers"""

        self.next += 1
        return self.next - 1
    
    def reset(self):
        """ Reset next serial to the start """

        self.next = self.start