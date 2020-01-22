#!/usr/bin/python3
class Student:

    """
    a simple class
    """

    def __init__(self, first_name, last_name, age):
        """
        constructing our class.
        Args:
        first_name: first name passed. 
        last_name: last name passed.
        age: age passed.
        Returns: None.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """
        that retrieves a dictionary representation of a Student instance
        Returns: the dictionary in json
        """
        return (self.__dict__)
