class Rectangle:
    def __init__(self, length: int, width: int):
        """
        Initialize a Rectangle instance with length and width.
        Args:
            length (int): The length of the rectangle.
            width (int): The width of the rectangle.
        """
        self.length = length
        self.width = width
    def __iter__(self):
        """
        Enable iteration over the Rectangle instance.
        Yields:
            dict: A dictionary containing the length or width.
        """
        yield {'length': self.length}
        yield {'width': self.width}
        
        rect = Rectangle(5, 3)
        for attr in rect:
            print(attr)
       
       
"""output:
    {'length': 5}
    {'width': 3}"""