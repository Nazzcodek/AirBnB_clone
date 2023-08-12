#!/usr/bin/python3
"""
The BaseModel class is a base class for all other models in the application.
It provides common attributes and methods for other models,
such as a unique identifier, creation time, and modification time.

Attributes:
    id: A unique identifier for each instance of the BaseModel class.
    create_at: The creation time of the instance.
    update_at: The modification time of the instance.

Methods:
    to_dict(): dictionary representation of the model
    save(): Saves the model to the database.
    __str__(): string representation of the model
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """This is the base model object"""

    # Constructor
    def __init__(self, *args, **kwargs):
        """
        This is the instance attribute of the Basemodel class

        Return:
            args: Variable lenght arguments
            kwargs: variable lenght key world arguments
        """
        time = '%Y-%m-%dT%H:%M:%S.%f'

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k in ['created_at', 'updated_at']:
                    new_value = datetime.strptime(v, time)
                    setattr(self, k, new_value)
                else:
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def save(self):
        """ the public attribute to update instance with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """The dictionary representation of the base model"""
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr

    def __str__(self):
        """String representation of the base model"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
