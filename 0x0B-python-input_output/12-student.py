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

    def to_json(self, attrs=None):
        """
        public method that retrieves a dictionary
        representation of a Student instance
        Args:
        self:self
        attrs:list of strings contains the attribute
        Returns: the dictionary
        """
        my_dict = {}
        if attrs is None:
            return self.__dict__
        for items in attrs:
            if hasattr(self, items):
                my_dict[items] = getattr(self, items)
        return my_dict
