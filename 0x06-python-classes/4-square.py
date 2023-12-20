#!/usr/bin/python3
"""
This is module uses setters, property operators
and getters
"""


class Square:
    """
    This method runs each time a new instance
    of a class is created
    """
    def __init__(self, size=0):
        self.__size = size
    """
    This method return the area when called
    """
    def area(self):
        return(self.__size*self.__size)

    @property
    """
    returns the protected value to be available for 
    size module setter
    """
    def size(self):
        return self.__size

    @size.setter
    """
    The size module getting the value of protected size
    property and then assigning it to value for modifications
    """
    def size(self, value):
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
