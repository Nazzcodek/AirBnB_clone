#!/usr/bin/python3
"""This is the module for cosole test"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
import console
import sys
import tests
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class ConsoleTest(unittest.TestCase):
    """This is the consoleTest istance object"""

    def tear_down(self):
        """Remove file.json"""
        try:
            os.remove("../file.json")
        except Exception:
            pass

    def test_do_quit(self):
        """test when `quit` is entered"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        self.assertEqual(f.getvalue(), '')

    def test_emptyline(self):
        """Test when no input and enter is pressed"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("            \n")
        self.assertEqual(f.getvalue(), '')

    def test_do_create(self):
        """test create instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create')
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create basemodel')
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
        self.assertIsNotNone(f.getvalue()) 

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.create()')
        self.assertIsNotNone(f.getvalue()) 

    def test_do_show(self):
        """Test show instance"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
        id = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show')
        self.assertEqual(f.getvalue(), '** class name missing **\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show basemodel')
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show BaseModel {id}')
        self.assertIsNotNone(f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show BaseModel')
        self.assertEqual(f.getvalue(), '** instance id missing **\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show BaseModel 123456')
        self.assertEqual(f.getvalue(), '** no instance found **\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.show()')
        self.assertEqual(f.getvalue(), '** instance id missing **\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'BaseModel.show({id})')
        self.assertIsNotNone(f.getvalue())

    def test_do_destroy(self):
        """Test destroy instance"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        id = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(f.getvalue(), '** class name missing **\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {id}")
        self.assertIsNotNone(f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy user")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 123456")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_do_all(self):
        """Test all instances"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        self.assertNotEqual(f.getvalue(), '')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        self.assertEqual(f.getvalue(), '')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all user")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
        self.assertEqual(f.getvalue(), '')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("user.all()")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all(123456)")
        self.assertNotEqual(f.getvalue(),
                         '** Unknown syntax: User.all(123456) **\n')

    def test_do_update(self):
        """Test update instace"""
        try:
            os.remove("file.json")
        except None:
            pass

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        id = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update basemodel")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 12345")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {id}")
        self.assertEqual(f.getvalue(), "** attribute name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {id} first_name")
        self.assertEqual(f.getvalue(), "** value missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update baseMode {id} first_name betty")
        self.assertIsNotNone(f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {id} first_name betty")
        self.assertEqual(f.getvalue(), '')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"basemodel.update()")
        self.assertEqual(f.getvalue(), "** class doesn\'t exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")


if __name__ == '__main__':
    unittest.main()
