#!/usr/bin/python3
"""This is the consele module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Thiss is the console module class"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """End Of File method"""
        print()
        return True

    def emptyline(self):
        """ Do nothing on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
