from backend.classes.check_syntax import Check
from rich import console; print = console.Console().print

check = Check.check


def Help(line):
    global check, print
    try:
        if check(line, "help -<>")[-1][0] == "user":
            print("Add a user: add user <username> <password>", style="bold green")
            print("Remove a user: remove user <username>", style="bold green")
            print("List users: ls users", style="bold green")
            return True
        elif check(line, "help -<>")[-1][0] == "exit":
            print("Exits the program: exit", style="bold green")
            return True
        elif check(line, "help -<>")[-1][0] == "ls":
            print("List all users: ls users", style="bold green")
            print("List all files: ls f", style="bold green")
            print("List all directories: ls d", style="bold green")
            return True
        elif check(line, "help -<>")[-1][0] == "add":
            print("Add a user: add user <username> <password>", style="bold green")
            return True
        elif check(line, "help -<>")[-1][0] == "remove":
            print("Remove a user: remove user <username>", style="bold green")
            return True
    except IndexError:
        print("""[bold green]All Available Commands are...[/bold green]
              
add user <username> <password>  [bold green]: Adds a user with the given credentials[/bold green]
remove user <username>          [bold green]: Remove a user with the given username[/bold green]
ls                              [bold green]: List based on given arg[/bold green]
cd <directory>                  [bold green]: Change directory to the given directory[/bold green]
exit                            [bold green]: Exits the program[/bold green]

[bold blue]For more information on a command, type help <command>[/bold blue]""", style="bold red")