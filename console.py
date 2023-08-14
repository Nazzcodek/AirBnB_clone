#!/usr/bin/python3
"""This is the consele module"""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Thiss is the console module class"""
    prompt = '(hbnb) '
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
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
            print("** class name missing **")
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

    def do_update(self, line):
        """Update an Instance base on class name and id"""
        arg_line = line.split()
        objects = storage.all()
        
        if not line:
            print("** class name missing **")
            return

        if arg_line[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg_line) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(arg_line[0], arg_line[1])
        if key not in objects:
            print("** no instance found **")
            return

        if len(arg_line) == 2:
            print("** attribute name missing **")
            return

        if len(arg_line) == 3:
            print("** value missing **")
            return

        else:
            instance = objects[key]
            attr_name = arg_line[2]
            attr_value = arg_line[3]

            setattr(instance, attr_name, attr_value)
            storage.save()

    def do_count(self, line):
        """Retrieve the number of instances of a given class."""
        arg_line = line.split()
        count = 0
        for obj in storage.all().values():
            if arg_line[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, line):
        """This changes the default method of all instances"""
        methods = {
                "all": self.do_all,
                "show": self.do_show,
                "update": self.do_update,
                "destroy": self.do_destroy,
                "count": self.do_count,
                }
        find = re.search(r"\.", line)
        if find:
            arg_line = [line[:find.span()[0]], line[find.span()[1]:]]
            find = re.search(r"\((.*?)\)", arg_line[1])
            if find:
                command = [arg_line[1][:find.span()[0]], find.group()[1:-1]]
                if command[0] in methods.keys():
                    call = "{} {}".format(arg_line[0], command[1])
                    return methods[command[0]](call)
        print("*** Unknown syntax: {}".format(line))
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
