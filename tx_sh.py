# make an input box where the user can exit input mode only by pressing Ctrl+X
import logging

import keyboard, platform, os, time
from rich import console
from backend.classes.file_class import file_opperations, JSON_read
from rich.syntax import Syntax
from rich.console import Console


color = JSON_read.read_color_hex # read the color hex from the config file
print = console.Console().print # print function
inputlines = []

s = True

def tx_open_themed(path, themes = 'one-dark'):
    console = Console()
    #check if the file exists in the directory
    if os.path.exists(path):
        try:
            syntax = Syntax.from_path(path, line_numbers=True, theme = themes, background_color='default')
            console.print(syntax)
            out = 'success'
        except Exception as e:
            print("Error: File or Theme not found", style = color('main', 0))
            out = 'success'
    else:
        path = f"data\\docs\\{path}"
        try:
            syntax = Syntax.from_path(path, line_numbers=True, theme = themes, background_color='default')
            console.print(syntax)
            out = 'success'
        except Exception as e:
            print("Error: File not found", style = color('main', 0))
            out = 'success'
        
    return out
    

def tx_open_raw(path, shell_color = 'quaternary', pallate = 0, args: str = None):
    
    line_number = 1

    with open(path, "r") as file:
        for line in file:
            if line_number < 10:
                print(f"  {line_number}│ ", style = color(shell_color, pallate), end = "")
            elif line_number < 100:
                print(f" {line_number}│ ", style = color(shell_color, pallate), end = "")
            elif line_number < 1000:
                print(f"{line_number}│ ", style = color(shell_color, pallate), end = "")
            print(line, end="")
            line_number += 1
        file.close()
    out = 'File has been successfully closed'
    return out


def save_file(path):
    global inputlines    
    if os.path.exists(path):
        print(f"File {path} already exists, do you want to overwrite it? (y/n)", style = color('main', 0), end = "")
        overwrite = input()
        if overwrite == 'y':
            with open(path, "w") as file:
                for line in inputlines:
                    file.write(line)
                    file.write("\n")
                file.close()
                print(f"File {path} has been saved", style = color('main', 0))
                inputlines = []
                return
        
        elif overwrite == 'n':
            print('Would you like to save it as a new file? (y/n) : ', style = color('main', 0), end = "")
            newfile = input()
            if newfile == 'y':
                print("Enter the new file name (example : C:/work/something) or only input file name to save in the data folder as '.txt': ", style = color('main', 0), end = "")
                newfilename = input()
                if '/' in newfilename and '.' in newfilename:
                    withoutext = newfilename.split(".")[0]
                    ext = newfilename.split(".")[-1]
                    path = f"{withoutext}.{ext}"
                    save_file(path)
                    return 'success'
                elif '\\' in newfilename and '.' in newfilename:
                    withoutext = newfilename.split(".")[0]
                    ext = newfilename.split(".")[-1]
                    path = f"{withoutext}.{ext}"
                    save_file(path)
                    return 'success'
                elif '/' in newfilename and '.' not in newfilename:
                    path = f"{newfilename}.txt"
                    save_file(path)
                    return 'success'
                elif '\\' in newfilename and '.' not in newfilename:
                    path = f"{newfilename}.txt"
                    save_file(path)
                    return 'success'
                elif '.' not in newfilename:
                    path = f"{newfilename}.txt"
                    save_file(path)
                    return 'success'
                return 'success'
            return 'success'
        else:
            print("Error, invalid input", style = color('main', 0))
            save_file(path)
    else:
        with open(path, "w") as file:
            for line in inputlines:
                file.write(line)
                file.write("\n")
            file.close()
        return 'success'
        


def save_func():
    print("Enter the save path (example : C:/work/something) or only input file name to save in the data folder as '.txt': ", style = color('main', 0), end = "")
    filename = input()
    
    # check if the filename is a path or just a file name, if it a path, split it and get the path and the extension, if it is just a file name, get the extension and the name
    
    if '/' in filename and '.' in filename:
        withoutext = filename.split(".")[0]
        ext = filename.split(".")[-1]
        path = f"{withoutext}.{ext}"
        save_file(path)
        return
    
    if '\\' in filename and '.' in filename:
        withoutext = filename.split(".")[0]
        ext = filename.split(".")[-1]
        path = f"{withoutext}.{ext}"
        save_file(path)
        return
    
    if '/' in filename and '.' not in filename:
        ext = "txt"
        path = f"{filename}.{ext}"
        save_file(path)
        return
    
    
    if '.' in filename and '/' not in filename and '\\' not in filename:
        ext = filename.split(".")[-1]
        name = filename.split(".")[0]
        path = f"data\\docs\\{name}.{ext}"
        save_file(path)
        return
        
    if filename == "":
        newname = str(time.strftime('%d-%m-%Y - %H-%M-%S',time.localtime(time.time())))
        print(f'File will be saved as {newname}.txt', style = color('main', 0))
        path = f"data\\docs\\{newname}.txt"
        save_file(path)
        return
    
    if filename != "":
        print(f'File will be saved as {filename}.txt', style = color('main', 0))
        path = f"data\\docs\\{filename}.txt"
        save_file(path)
        return
    
    print("Error, file name not valid", style = color('main', 0))
    save_func()


def tx_new(shell_color = 'quaternary', pallate = 0, args = None):
    os.system("cls" if platform.system() == "Windows" else "clear")
    global s, inputlines, print
    maxinput = False
    line_number = 1
    print("TX EDITOR", style = color(shell_color, pallate), justify="center")
    print("┌──────────────────┬─────────────────┬─────────────────┬──────────────────┬─────────────────┐", style = color(shell_color, pallate))
    print("│ Commands List:   │ Exit : Ctrl + X │ Save : Ctrl + S │ Clear : Ctrl + Q │ Help : Ctrl + K │", style = color(shell_color, pallate))
    print("└──┬───────────────┴─────────────────┴─────────────────┴──────────────────┴─────────────────┘", style = color(shell_color, pallate))
    while s == True:
        if line_number < 10:
            print(f"  {line_number}│ ", style = color(shell_color, pallate), end = "")
        elif line_number < 100:
            print(f" {line_number}│ ", style = color(shell_color, pallate), end = "")
        elif line_number < 1000:
            print(f"{line_number}│ ", style = color(shell_color, pallate), end = "")
            
        if line_number >= 1000:
            os.system("cls" if platform.system() == "Windows" else "clear")
            print("TX EDITOR", style = color(shell_color, pallate), justify="center")
            print(f"Max lines reached input will no longer work only options are, Save (Ctrl + S), Exit (Ctrl + X)", style = color('main', 0), justify="center")
            maxinput = True
            
        if maxinput == False:
            lineinput = input()
            inputlines.append(lineinput)
        if maxinput == True:
            print("Plsease enter your key combination: ", style = color('main', 0), end = "")
            lineinput = input()
            if lineinput == "\x18": # ctrl + x
                status = "Tx Editor exited without saving"
                s = False
                return status
            
            elif lineinput == "\x13": # if the user presses Ctrl+S, the program will save the input lines to a file
                s = False
                save_func()
                status = "Tx Editor exited and saved"
                return status
            else:
                print("INVALID", style = color('main', 0), end = "")
                time.sleep(0.25)
                os.system("cls" if platform.system() == "Windows" else "clear")
                lineinput = 'None'
                
            
        
        line_number += 1
        
        if lineinput == "\x18": # if the user presses Ctrl+X, the program will exit
            inputlines.remove("\x18")
            status = "Tx Editor exited without saving"
            s = False
            pass
        
        elif lineinput == "\x13": # if the user presses Ctrl+S, the program will save the input lines to a file
            inputlines.remove("\x13")
            s = False
            status = "Tx Editor exited and saved"
            save_func()
            pass
                
        elif lineinput == "\x11": # if the user presses Ctrl+Q, the program will clear the input lines
            inputlines.remove("\x11")
            os.system("cls" if platform.system() == "Windows" else "clear")
            print("TX EDITOR", style = color(shell_color, pallate), justify="center")
            print("┌──────────────────┬─────────────────┬─────────────────┬──────────────────┬─────────────────┐", style = color(shell_color, pallate))
            print("│ Commands List:   │ Exit : Ctrl + X │ Save : Ctrl + S │ Clear : Ctrl + Q │ Help : Ctrl + K │", style = color(shell_color, pallate))
            print("└──────────────────┴─────────────────┴─────────────────┴──────────────────┴─────────────────┘", style = color(shell_color, pallate))
            pass
        
        elif lineinput == "\x0b": # if the user presses Ctrl+K, the program will show the help message
            inputlines.remove("\x0b")
            print("┌───────────────────────────────────┐", style = color(shell_color, pallate))
            print("│ How to use the commands:          │", style = color(shell_color, pallate))
            print("├───────────────────────────────────┤", style = color(shell_color, pallate))
            print("│ To activate the command you have  │", style = color(shell_color, pallate))
            print("│ to press the key combination      │", style = color(shell_color, pallate))
            print("│ followed by the enter key.        │", style = color(shell_color, pallate))
            print("├───────────────────────────────────┤", style = color(shell_color, pallate))
            print("│ Exit: will exit the text editor.  │", style = color(shell_color, pallate))
            print("│ Save: will save the current file  │", style = color(shell_color, pallate))
            print("│ Clear: will clear the screen.     │", style = color(shell_color, pallate))
            print("│ Help: will print this dialog box. │", style = color(shell_color, pallate))
            print("└───────────────────────────────────┘", style = color(shell_color, pallate))
            pass
    
    return status

def tx_open(args, shell_color = 'quaternary', pallate = 0):
    if args[-1] == '-tc':
        print("Please eneter a theme \nAll Themes: 'one-dark', 'solarized-dark', 'github-dark', 'vim', 'fruity'\n Input: ", style = color(shell_color, pallate), end = "")
        themes = input()
        out = tx_open_themed(args[-2], themes)
    
    else:
        out = tx_open_themed(args[2], 'one-dark')
    
    return out
        
    
def tx_sh(shell_color = 'quaternary', pallate = 0, args = None):
    
    if args == None:
        return "Args not set"
    
    if args[1] == '-o':
        out = tx_open(args, shell_color, pallate)
        return out
    
    if args[1] == '-n':
        status = tx_new(shell_color, pallate)
        print(status)
        out = 'success'
        return out
        
    else:
        print("Invalid command", style = color(shell_color, pallate))
        out = 'error: no arguments given'
        pass
    
    return out

if __name__ == '__main__':
    out = tx_sh()
    print(out, style = color('main', 0))
    
