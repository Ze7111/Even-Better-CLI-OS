from rich import console; print = console.Console().print
import os, time, getpass, maskpass
from backend.modules.credentials import Credentials
from backend.classes.sort_input import checkLine

color: str = "grey74"
seperator: str = "─"

def get_terminal_size():
    tw = os.get_terminal_size().columns
    return tw

def login():
    cred = Credentials()
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to the dev-env command line interface. Please login to continue.", style="bold bright_black")
    print("Username: ", end="", style="bold green")
    username = input()
    print("Password: ", end="", style="bold green")
    password = maskpass.askpass(prompt="", mask="*")
    if cred.check(username, password):
        os.system("cls" if os.name == "nt" else "clear")
        command_line(username)
    else:
        print("Invalid username or password. Please try again.", style="bold red")
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        login()    
    
def command_line(username = "default"):
    global color, seperator
    tw = get_terminal_size()
    
    print(f"[bold {color}]┌─[bold bright_black]([bold green]{os.getcwd()}[bold bright_black])[bold {color}]{seperator*int((tw-(len(username)+8+len(os.getcwd())+11)))}([bold red]{username}[bold bright_black]@[bold green]dev-env:pts[bold bright_black])")
    print(f"[bold {color}]└─[bold bright_black]([bold red]{time.strftime('%H:%M:%S')}[bold bright_black] on [bold green]main [bold dark_cyan]✭[bold bright_black])[bold {color}]──> ", end="")
    
    command = input()
    
    if checkLine.CheckLine(command, "color -<>", username):
        try:
            color = command.split(" ")[1]
        except IndexError:
            print("[bold red]The term color need exactly 1 more argument and should follow the format, color <any color>.\n[bold green]All supported formats are, Default ASCII Colors, HEX Color, or rgb colors.\n[bold green]Examples: 'color red', 'color #ff0000', 'color rgb(255,0,0)'.", style="bold red")
        print(" ")
        command_line(username)
        
    elif checkLine.CheckLine(command, "sep -<>", username):
        try:
            seperator = command.split(" ")[1]
        except IndexError:
            print("[bold red]The term seperator need exactly 1 more argument and should follow the format, seperator <any character>.\n[bold green]Examples: 'seperator -'.", style="bold red")
        print(" ")
        command_line(username)
    
    elif checkLine.CheckLine(command, "clear", username):
        os.system("cls" if os.name == "nt" else "clear")
        command_line(username)
        
    elif checkLine.CheckLine(command, None, username):
        print(" ")
        command_line(username)
        
    else:
        print("Invalid command. Please try again.", style="bold red")
        time.sleep(3)
        print(" ")
        command_line(username)
