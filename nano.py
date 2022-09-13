from rich import console; print = console.Console().print

class Vim:
    def __init__(self, color):
        self.color = color
        self.line = 1
        self.lineArray = []
        
    def editor(self):
        print(f"TX EDITOR", style = self.color, justify="center")
        print(f"┌──────────────────┬─────────────────┬─────────────────┬──────────────────┬─────────────────┐", style = self.color)
        print(f"│ Commands List:   │ Exit : Ctrl + X │ Save : Ctrl + S │ Clear : Ctrl + Q │ Help : Ctrl + K │", style = self.color)
        print(f"└──┬───────────────┴─────────────────┴─────────────────┴──────────────────┴─────────────────┘", style = self.color)
        while True:
            print(f"{self.line}  │ ", style = self.color, end="")
            self.line += 1
            self.lineArray.append(input())
            
            if self.lineArray[-1] == "\x18": # Ctrl + X
                print(f"┌──┴─────────────────────────────────────────────────────────────────┐", style = self.color)
                print(f"│ Are you sure you want to exit? [bold red]This action cannot be undone.[bold bright_black] ([bold green]y[bold bright_black]/[bold red]n[bold bright_black])[/bold red][/bold green][/bold bright_black][/bold bright_black][{self.color}] │ ", end="", style = self.color)
                if input() == "y":
                    print(f"└────────────────────────────────────────────────────────────────────┘", style = self.color)
                    break
                else:
                    print(f"└──┬─────────────────────────────────────────────────────────────────┘", style = self.color)
                    continue
            
            elif self.lineArray[-1] == "\x13": # Ctrl + S
                Vim.save(self)
    
    def save(self):
        print(f"┌──┴─────────────────────────────────────────────────────────────────┐", style = self.color)
        print(f"│ Enter the file name to save as: ", end="", style = self.color)
        filename = input()
        print(f"└────────────────────────────────────────────────────────────────────┘", style = self.color)
        with open(filename, "w") as f:
            for i in self.lineArray:
                f.write(i + "\n")
        print(f"┌────────────────────────────────────────────────────────────────────┐", style = self.color)
        print(f"│ File saved successfully.                                           │", style = self.color)
        print(f"└────────────────────────────────────────────────────────────────────┘", style = self.color)
                
                
                
vim = Vim('blue')
vim.editor()
