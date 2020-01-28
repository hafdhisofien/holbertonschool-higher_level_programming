#!/usr/bin/python3
"""This class will be the “base” of all other classes in this project
"""

import json
"""
importing json functions
"""
import csv
"""
importing csv functions
"""


class Base:
    """
    the goal of this class is to manage
    id attribute in all your future classes
    and to avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode='w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        list_instance = []
        try:
            with open(filename, mode="r") as f:
                list_dict = cls.from_json_string(f.read())
            for i in list_dict:
                list_instance.append(cls.create(**i))
            return list_instance
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv file
        """

        fieldnames = [item.to_dictionary() for item in list_objs]
        with open(cls.__name__ + ".csv", mode="w") as csvfile:
            write_to = csv.DictWriter(csvfile, fieldnames[0].keys())
            write_to.writeheader()
            write_to.writerows(fieldnames)

    @classmethod
    def load_from_file_csv(cls):
        """load from csv file
        """

        fieldnames = []
        fieldnames_dict = {}
        with open(cls.__name__ + ".csv", mode="r") as csvfile:
            csvfile = csv.DictReader(csvfile)
            for item in csvfile:
                for i, j in dict(item).items():
                    fieldnames_dict[i] = int(j)
                fieldnames.append(cls.create(**fieldnames_dict))
        return fieldnames
