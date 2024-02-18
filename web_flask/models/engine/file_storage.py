#!/usr/bin/python3
""" Module for FileStorage class """
import json
from models.base_model import BaseModel


class FileStorage:
    """ Serializes instances to a JSON file and deserializes JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        dict_to_save = {}
        for key, value in FileStorage.__objects.items():
            dict_to_save[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dict_to_save, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                FileStorage.__objects = json.load(file)
                for key, value in FileStorage.__objects.items():
                    class_name = value['__class__']
                    del value['__class__']
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass

    def close(self):
        """ Calls reload() method for deserializing the JSON file to objects """
        self.reload()
