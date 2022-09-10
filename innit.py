'''
 !/usr/bin/env python3
 Path: innit.py
 Description: This file is used to innitiate the project. It is run when the project is started and it creates the innit.py file and the logs folder. It also deletes old log files.
 Author: @Ze7111
'''

# ====================================================================================== Default imports =======================================================================================================
import sys, os, time, logging, shutil; from rich import console; print = console.Console().print; from backend.core.basic_handler import file_actions; from backend.modules.admin import main as admin #       |
# ==============================================================================================================================================================================================================

# ================================ Global Variables ================================
runadmin = False # set runadmin to false                                           |
backup = file_actions.create_zip_backup # set backup to create_zip_backup function |
clearLogs = file_actions.delete_logs # set clearLogs to delete_logs function       |
# ==================================================================================

class innit(): # innit class
    def __init__(): # innit function
        backup() # create zip backup
        clearLogs() # delete logs
        pass # pass
    
    
    def main(): # main function
        pass # pass
        
if __name__ == '__main__': # check if file is being run directly
    if runadmin is True: # if runadmin is true
        admin() # run admin module ---------------------------------------- use this only if you want to run the admin module ----------------------------------------
    innit.__init__() # run innit function
else: # if file is not being run directly
    print('This file is not meant to be imported.', style='bold red') # print error if file is imported