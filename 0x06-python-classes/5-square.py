#!/usr/bin/python3
"""
This module prints the square using #
"""


class Square:
    """
    This module always runs
    """
    def __init__(self, size=0):
        self.__size = size
    """
    This method returns the area when called
    """
    def area(self):
        return(self.__size*self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
    """
    This module prints the square using #
    """
    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
