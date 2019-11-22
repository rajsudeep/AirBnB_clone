#!/usr/bin/python3
""" Console interpreter for the AirBnB clone """

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ commands for the interpreter to execute """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place", "State",
               "City", "Amenity", "Review"]

    def do_create(self, line):
        """ creates a new instance of base model """
        try:
            if line == "":
                print("** class name missing **")
                return
            new_base = eval("{}()".format(line))
            new_base.save()
            print(new_base.id)
        except NameError:
            print("** class doesn't exist **")

    def help_create(self):
        print("Creates a new instance of a given class\n")

    def do_show(self, line):
        """ prints string representation of an instance """
        if not line:
            print("** class name missing **")
            return
        args = line.split(" ")
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key not in objs:
            print("** no instance found **")
        else:
            print(objs[key])

    def help_show(self):
        """ show usage """
        print("Prints the string of an instance based on the class and id\n")

    def do_destroy(self, line):
        """ deletes an instances based on class and id """
        if not line:
            print("** class name missing **")
            return
        args = line.split(" ")
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key not in objs:
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def help_destroy(self):
        """ destroy usage """
        print("Deletes an instance based on the class name and id\n")

    def do_all(self, line):
        """ print all string representation of instances """
        if line != "":
            args = line.split(" ")
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            class_insts = [str(o) for k, o in storage.all().items()
                           if type(o).__name__ == args[0]]
            print(class_insts)
        else:
            all_insts = [str(o) for k, o in storage.all().items()]
            print(all_insts)

    def help_all(self):
        """ all usage """
        print("Prints all str instances based or not on the class name\n")

    def do_update(self, line):
        """ updates an instance based on class and id """
        if not line:
            print("** class name missing **")
            return
        args = line.split(" ")
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        val = objs[key]
        try:
            attr = getattr(val, args[2])
            setattr(val, args[2], type(attr)(args[3]))
        except:
            setattr(val, args[2], args[3])
        storage.save()

    def help_update(self):
        """ update usage """
        print("Updates an instance based on the class name and id\n")

    def do_count(self, line):
        """ counts the number of class instances """
        args = line.split(" ")
        count = 0
        if args[0] in HBNBCommand.classes:
            storage.reload()
            my_dict = storage.all()
            for key in my_dict.keys():
                if args[0] in str(my_dict[key]):
                    count += 1
            print(count)


    def do_User(self, line):
        if line == ".all()":
            self.do_all("User")
        if line == ".count()":
            self.do_count("User")
        if line == ".show(self.id)":
            self.do_show()

    def do_State(self, line):
        if line == ".all()":
            self.do_all("State")
        elif line == ".count()":
            self.do_count("State")

    def do_City(self, line):
        if line == ".all()":
            self.do_all("City")
        elif line == ".count()":
            self.do_count("City")

    def do_Amenity(self, line):
        if line == ".all()":
            self.do_all("Amenity")
        elif line == ".count()":
            self.do_count("Amenity")

    def do_Place(self, line):
        if line == ".all()":
            self.do_all("Place")
        elif line == ".count()":
            self.do_count("Place")

    def do_Review(self, line):
        if line == ".all()":
            self.do_all("Review")
        elif line == ".count()":
            self.do_count("Review")

    def do_BaseModel(self, line):
        if line == ".all()":
            self.do_all("BaseModel")
        elif line ==".count()":
            self.do_count("BaseModel")


    def do_quit(self, line):
        """ exits the program using quit """
        raise SystemExit

    def help_quit(self):
        """ quit usage """
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """ exits the program using EOF """
        return True

    def help_EOF(self):
        """ EOF usage """
        print("EOF command (Ctrl-D) to exit the program\n")

    def emptyline(self):
        """ executes nothing when entered """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
