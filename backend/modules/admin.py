'''
 !/usr/bin/env python3
 Path: backend/modules/admin.py
 Description: This file is used to run the program with admin rights.
 Author: @Ze7111
'''

import ctypes, sys # import ctypes and sys
def main(): # main function
    def is_admin(): # check if user is admin
        try: # try
            return ctypes.windll.shell32.IsUserAnAdmin() # check if user is admin
        except: # if the user is not on windows
            return False # if not windows
    if is_admin(): # check if user is admin
        pass # pass
    else: # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1) # re-run the program with admin rights