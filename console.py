#!/usr/bin/python3
"""This is the consele module"""

import cmd
import models
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Thiss is the console module class"""
    prompt = '(hbnb) '
    classes = {
            "BaseModel": BaseModel,
            }

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """EOF method to exit the console"""
        print()
        return True

    def emptyline(self):
        """ Do nothing on empty line"""
        pass

    def do_create(self, line):
        """Create a new instance of base model"""
        if not line:
            print("** class name missing **")
            return

        if line not in self.classes:
            print("** class doesn't exist **")
        else:
            instance = self.classes[line]()
            instance.save()
            print("{}".format(instance.id))

    def do_show(self, line):
        """Show the string representation of instances"""
        arg_line = line.split()

        if not arg_line:
            print("** class name is missing **")
        elif arg_line[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            if len(arg_line) < 2:
                print("** instance id missing **")
            else:
                objects = storage.all()
                key = "{}.{}".format(arg_line[0], arg_line[1])
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        arg_line = line.split()

        if not arg_line:
            print("** class name is missing **")
        elif arg_line[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            if len(arg_line) < 2:
                print("** instance id missing **")
            else:
                objects = storage.all()
                key = "{}.{}".format(arg_line[0], arg_line[1])
                if key in objects:
                    del objects[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """ Print srting representation of all object """
        arg_line = line.split() if line else []
        instance_strings = []

        if not arg_line:
            all_instances = storage.all().values()
            for obj in all_instances:
                instance_strings.append(str(obj))
            print(instance_strings)
        elif arg_line[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for obj in storage.all().values():
                if arg_line[0] == obj.to_dict()["__class__"]:
                    instance_strings.append(str(obj))

        if instance_strings:
            print(instance_strings)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
