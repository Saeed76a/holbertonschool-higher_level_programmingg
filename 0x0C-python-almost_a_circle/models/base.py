#!/usr/bin/python3
"""
Module that contain the first class Base
"""
import json


class Base:
    """
    This class will be the “base” of all other
    classes in this project.
    """
    # private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor with its
        assign the public instance attribute id
        Args:
            id - value greater than 0
        """
        if id is not None:
            # b = base (12)
            # public instance attribute
            self.id = id
        else:
            Base.__nb_objects += 1
            # assign the new value to the public instance attribute id
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """"
        static method to_json_string: Serialize obj to a JSON
        formatted str.
        Args:
            list_dictionaries: a list of dictionaries
        Return:
            returns the JSON string representation[] of a list_dictionarires
        """
        # If list_dictionaries is None or empty, return the string: "[]"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        # Serialize obj to a JSON formatted str.
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file classmethod: writes the Kson string
        representation of list_objs to a file
        Args:
            cls: the class itself
            list_objs: a list of instances who inherits of Base
        """
        # <Class name>.json - example: Rectangle.json
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode='w', encoding='utf-8') as f:
            # If list_objs is None, save an empty list
            if list_objs is None:
                f.write('[]')
            else:
                # You must overwrite the file if it already exists
                # to_dictionary(self) that returns the dictionary
                # representation of a Square:
                list_dict = [obj.to_dictionary()for obj in list_objs]
                # json_string returns the JSON string representation
                # of list_dictionaries:
                f.write(cls.to_json_string(list_dict))
