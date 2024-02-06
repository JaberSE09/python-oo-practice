"""Python serial number generator."""

class SerialGenerator:
    def __init__(self, START):
        self.START=START
        self.increment=START
       
    def generate(self):
        print(self.increment)
        self.increment= self.increment + 1
    def reset(self):
        self.increment=self.START
       
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

serial = SerialGenerator(START=100)
serial.generate()
serial.generate()
serial.generate()
serial.reset()
serial.generate()
    

