from backend.modules.credentials import Credentials
credentials = Credentials()

from rich import console
print = console.Console().print

from rich.table import Table
from rich import box

class User:
    def list_users(current_user):
        data = credentials.list_users()[0]
        
        table = Table(box=box.ASCII2, style="bold gray74", header_style="bold green")

        table.add_column("User", style="bold green", justify="centre")
        table.add_column("Status", style="bold green", justify="centre")

        for i in data:
            if i == current_user:
                table.add_row(i, "Active", style="bold green")
            else:
                table.add_row(i, "Inactive", style="bold red")
                
        print(table)
        return True
    
    
    def add_User(line, username):
        global credentials, print
        if username == line.split(" ")[2]:
            print("You cannot add yourself as a user.", style="bold red")
            return True
        if len(line.split(" ")) != 4:
            print("Invalid syntax. Please use the following syntax: add user <username> <password>", style="bold red")
            return False
        else:
            credentials.add(line.split(" ")[2], line.split(" ")[3])
            print("User added successfully", style="bold green")
            print("You can login with the new credentials after restarting.", style="bold red")
            return True

    def remove_user(line, username):
        global credentials, print
        if username == line.split(" ")[2]:
            print("You cannot remove yourself.", style="bold red")
            return True
        if len(line.split(" ")) != 3:
            print("Invalid syntax. Please use the following syntax: remove user <username>", style="bold red")
            return False
        else:
            print("[bold purple]Are you sure you want to remove the user? [bold red]This action cannot be undone.[bold bright_black] ([bold green]y[bold bright_black]/[bold red]n[bold bright_black]) : ", end="")
            if input() == "y":
                print("Enter the password of the user to confirm: ", end="", style="bold green")
                check_pass = input()
                if credentials.check(line.split(" ")[2], check_pass):
                    credentials.delete(line.split(" ")[2], check_pass)
                    print("User removed successfully", style="bold green")
                    print("This will be reflected after restarting.", style="bold red")
                    return True
                else:
                    print("Invalid username or password. Please try again.", style="bold red")
                    return True
            else:
                return True