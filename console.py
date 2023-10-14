#!/usr/bin/python3
"""
Commandline interpreter module
Defines class HBNBCommand()
"""
import cmd
import readline
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    A class that represents a command line interface
    for a specific application.

    Attributes:
        prompt (str): The prompt string displayed to the user.classes (dict):
        A dictionary that maps class names to their corresponding classes.
    """

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def emptyline(self):
        """
        Placeholder method that does nothing when the
        user enters an empty line.

        Example Usage:
        command = HBNBCommand()
        command.emptyline()  # No output

        Inputs: None
        Flow: The emptyline method does not take any inputs.
        Outputs: None
        """
        pass

    def do_EOF(self, arg):
        """
        Execute the do_EOF command.

        This command is called when the user enters Ctrl+D.
        It simply prints a newline character and returns True,
        indicating that the program should exit.

        Args:
            arg (str): The argument passed to the method.
            It is not used in this method.

        Returns:
            bool: True, indicating that the program should exit.

        Example:
            command = HBNBCommand()
            command.do_EOF("")  # Output: prints a
            newline character and returns True
        """
        print()
        return True

    def do_quit(self, arg):
        """
        Exit the command line interface program.

        :param arg: The argument passed to the method.
        It is not used in this method.
        :type arg: str
        :return: True, indicating that the program should exit.
        :rtype: bool
        """
        return True

    def help_quit(self):
        """
        Provides a brief explanation of how to use the `quit`
        command in the command line interpreter program.

        Example Usage:
        command = HBNBCommand()
        command.help_quit()

        Inputs:
        - None

        Flow:
        - The method simply prints the usage
        instructions for the `quit` command,
        which is "Usage: quit".
        - It also prints a brief description of what the command does,
        which is "command exits the command line interpreter program".

        Outputs:
        - None
        """
        print("Usage: quit")
        print("command exits the command line interpreter program")

    def do_create(self, arg):
        """
        Create a new instance of a class and save it to the database.

        Args:
            arg (str): The name of the class to create an instance of.

        Example Usage:
            command = HBNBCommand()
            command.do_create("User")  # Output: prints the id of the newly
            created User instance

        Raises:
            None

        Returns:
            None
        """
        if not arg or len(arg) == 0:
            print("** class name missing **")
            return

        if arg in HBNBCommand.classes.keys():
            new_instance = HBNBCommand.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """
        Provides a brief explanation of how to use the create command
        in the command line interpreter program.

        Example Usage:
        command = HBNBCommand()
        command.help_create()

        Inputs:
        - None

        Flow:
        - The method simply prints the usage
        instructions for the create command,
        which is "create <object_name>".

        Outputs:
        - None
        """
        print("create <object_name>")

    def do_show(self, arg):
        """
        Retrieve and print the string representation of an instance
        based on its class name and ID.

        Args:
            arg (str): The argument passed to the method.
            It should be in the format "class_name instance_id".

        Returns:
            None

        Example Usage:
            command = HBNBCommand()
            command.do_show("User 123")  # Output: prints the string
            representation of the User instance with ID 123
        """
        if not arg or len(arg) == 0:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        instances = storage.all()

        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def help_show(self):
        """
        Provides a brief explanation of how to use the show command
        in the command line interpreter program.

        Example Usage:
        command = HBNBCommand()
        command.help_show()

        Inputs:
        - None

        Flow:
        - The method simply prints the usage instructions for the show
        command, which is "show <object_name> <object_id>".

        Outputs:
        - None
        """
        print("show <object_name> <object_id>")

    def do_destroy(self, arg):
        """
        Delete an instance from the database based on its class name and ID.

        Args:
            arg (str): The argument passed to the method.
            It should be in the format "class_name instance_id".

        Returns:
            None

        Raises:
            None

        Example Usage:
            command = HBNBCommand()
            command.do_destroy("User 123")
        """
        if not arg or len(arg) == 0:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        instances = storage.all()

        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def help_destroy(self):
        """
        Provides documentation for the `destroy`
        command in the `HBNBCommand` class.

        Example Usage:
        command = HBNBCommand()
        command.help_destroy()

        Inputs:
        - None

        Flow:
        - The method simply prints the usage instructions
        for the `destroy` command, which is
        "destroy <object_name> <object_id>".

        Outputs:
        - None
        """
        print("destroy <object_name> <object_id>")

    def do_all(self, arg):
        """
        Retrieve and print a list of all instances of a
        specific class or all instances of all classes.

        Args:
            arg (str): The argument passed to the method.
            It can be an empty string, a class name,
            or a combination of a class name and an object ID.

        Returns:
            None

        Example Usage:
            command = HBNBCommand()
            command.do_all("")  # Output: prints a
            list of all instances of all classes
            command.do_all("User")  # Output: prints a
            list of all instances of the User class
        """
        args = arg.split()
        instances = storage.all()

        if not args:
            print([str(instance) for instance in instances.values()])
        elif args[0] in HBNBCommand.classes.keys():
            print([str(instance) for key, instance in instances.items()
                  if key.startswith(args[0] + ".")])
        else:
            print("** class doesn't exist **")

    def help_all(self):
        """
        Print the usage instructions and a
        brief description of the 'all' command.

        Usage: all [object_name]
        Description: Print list of all instances or of the object_name
        """
        print("all [object_name]")
        print("print list of all instances or of the object_name")

    def do_update(self, arg):
        """
        Update an object based on the class name and id.

        Args:
            self: The instance of the HBNBCommand class.
            arg (str): The argument passed to the method.

        Returns:
            None

        Example Usage:
            command = HBNBCommand()
            command.do_update("")  # Output: ** class name missing **

        Code Analysis:
            - The code checks if the arg is empty or missing.
            - If the arg is empty or missing, it prints the error message
            "** class name missing **" and returns.
        """
        if not arg or len(arg) == 0:
            print("** class name missing **")
            return

        args = arg.split()

        if len(args) >= 4:
            if args[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
                return

            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()

            if key in instances:
                instance = instances[key]
                setattr(instance, args[2], args[3])
                instance.save()
            else:
                print("** no instance found **")
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def help_update(self):
        """
        Provides a brief explanation of how to use the
        update command in the command line interpreter program.

        Example Usage:
        command = HBNBCommand()
        command.help_update()

        Inputs:
        - None

        Flow:
        The method simply prints the usage instructions for the
        update command, which is
        "update <class name> <id> <attribute name> "<attribute value>"".

        Outputs:
        None
        """
        print('update <class name> <id> <attribute name> "<attribute value>"')

    def do_count(self, arg):
        """
        Count the number of instances of a specific class in the database.

        Args:
            arg (str): The name of the class to count instances of.

        Example Usage:
            command = HBNBCommand()
            command.do_count("User")  # Output: prints the count of
            User instances in the database

        Raises:
            None

        Returns:
            None (the count is printed to the console)
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return

        instances = storage.all()
        count = sum(1 for key in instances if key.startswith(args[0] + "."))
        print(count)

    def default(self, arg):
        """
        Handle unrecognized commands.

        This method parses the input argument and calls the
        appropriate method based on the syntax of the command.

        Args:
            arg (str): The argument passed to the method.
            It represents the unrecognized command.

        Returns:
            None

        Example Usage:
            command = HBNBCommand()
            command.default("User.all()")  # Output:
            prints a list of all instances of the User class
        """
        args = arg.split('.')
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(arg))
            return

        class_name = args[0]
        if args[1] == "all()":
            HBNBCommand.do_all(self, class_name)
        elif args[1] == "count()":
            HBNBCommand.do_count(self, class_name)
        elif args[1].startswith("show(") and args[1].endswith(")"):
            instance_id = args[1][6:-2]
            show_command = "{} {}".format(class_name, instance_id)
            HBNBCommand.do_show(self, show_command)
        elif args[1].startswith("destroy(") and args[1].endswith(")"):
            instance_id = args[1][9:-2]
            destroy_command = "{} {}".format(class_name, instance_id)
            HBNBCommand.do_destroy(self, destroy_command)
        elif args[1].startswith("update(") and args[1].endswith(")"):
            instance_id = args[1].split(',')[0][7:].strip()
            update_args = ', '.join(args[1].split(',')[1:]).strip()

            if update_args.startswith("{") and update_args.endswith("}"):
                try:
                    update_dict = {
                        k.strip('\'\"'): v for k, v in update_dict.items()
                    }
                    if isinstance(update_dict, dict):
                        update_command = "{} {} {}".format(class_name,
                                                           instance_id,
                                                           update_dict)
                        HBNBCommand.do_update(self, update_command)
                    else:
                        print("** Invalid dictionary representation **")
                except Exception as e:
                    print("** Error evaluating dictionary \
                          representation: {} **".format(e))
            else:
                attribute_name = update_args.split(',')[0].strip()
                attribute_value = update_args.split(',')[1].strip()
                update_command = "{} {} {} {}".format(class_name,
                                                      instance_id,
                                                      attribute_name,
                                                      attribute_value)
                HBNBCommand.do_update(self, update_command)
        else:
            print("*** Unknown syntax: {}".format(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
