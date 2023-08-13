#!/usr/bin/python3
"""
This model serializes instances to a JSON file and
deserializes JSON file to instances

Attributes:
    __file_path (str): path to save objects to.
    __objects (dict): A dictionary of objects instance.

Methods:
    all(): returns the dictionary __objects
    new(): set __object int the object with key
    save(): serializes __objects to the JSON file (path: __file_path)
    reload(): deserializes the JSON file to __objects
"""
import json
import os.path


class FileStorage:
    """This is the FileStorage model that
        - serialzes instances to a JSON file and
        - deserializez JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def classes(self):
        """ returns the dictionary classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State 
        from models.city import City 
        from models.amenity import Amenity 
        from models.place import Place 
        from models.review import Review
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
        return classes

    # public instance method
    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """This method sets __objects the obj with key <obj class name>.id"""
        obj_class_name = obj.__class__.__name__
        key = "{}.{}".format(obj_class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        This method serializes __objects to the JSON file
        (path: __file_path)
        """
        json_object = {}
        for k, v in FileStorage.__objects.items():
            json_object[k] = v.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='UTF-8') as f:
            json.dump(json_object, f)

    def reload(self):
        """This method deserializes the JSON file to __objects"""
        load_file = FileStorage.__file_path

        if os.path.exists(load_file):
            with open(load_file, "r", encoding="UTF-8") as f:
                load_dict_obj = json.load(f)
            for k, v in load_dict_obj.items():
                obj = self.classes()[v["__class__"]](**v)
                FileStorage.__objects[k] = obj
