#!/usr/bin/python3
"""This is the consele module"""

import cmd
import models
from models import storage
from models.base_model import BaeModel


classes = {
        'BaseModel': BaseModel
        }

def check_class(class_name):
    """Checks if the given class name exists and
        returns the class object if it does."""
    if class_name in classes:
        return classes[class_name]
    else:
        return None

class HBNBCommand(cmd.Cmd):
    """Thiss is the console module class"""
    prompt = '(hbnb) ' 

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

        class_obj = check_class(line)
        if class_obj is None:
            print("** class doesn't exist **")
        else:
            instance = class_obj()
            instance.save()
            print("{}".format(instance.id))

    def do_show(self, line):
        """Show the string representation of instances"""
        arg_line = line.split()

        class_obj = check_class(arg_line[0])
        if not line:
            print("** class name is missing **")
        elif class_obj is None:
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
        class_obj = check_class(arg_line[0])

        if not arg_line[0]:
            print("** class name is missing **")
        elif class_obj is None:
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
        arg_line = line.split()
        class_obj = check_class(arg_line[0])

        if not line or class_obj:
            all_instances = storage.all().values()
            instance_strings = []
            for obj in all_instances:
                instance_strings.append(str(obj))
            print(instance_strings)
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
