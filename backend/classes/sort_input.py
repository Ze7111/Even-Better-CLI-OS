from backend.classes.check_syntax import Check
from rich import console; print = console.Console().print
from backend.modules.credentials import Credentials
from backend.functions.add_remove_user import User as user
from rich.pretty import pprint
from backend.functions.help import Help
import os


check = Check.check
credentials = Credentials()

class checkLine:
    def CheckLine(line, correctSyntax = None, username = None):
        if correctSyntax != None:
            if check(line, correctSyntax):
                return True
        
        elif check(line, "exit -<>"):
            exit()
        
        elif check(line, "ls -<>"):
            if check(line, "ls -<>")[-1][0] == "users":
                user.list_users(username)
                return True
            print("Invalid syntax. Please use the following syntax: ls <argument>", style="bold red")
            return True

        elif check(line, "add user -<> -<>"):
            user.add_User(line, username)
            return True
        
        elif check(line, "remove user -<>"):
            user.remove_user(line, username)
        
        elif check(line, "help -<>"):
            Help(line)
            
            return True
        
        else:
            return False