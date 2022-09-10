###################################################################################################
#   Function     #   Description    #  Return Type   #   Return Value  #   Return Description     #
#----------------#------------------#----------------#-----------------#--------------------------#
#   __init__     #   Initializes    #   None         #   None          #         None             #
#    write       #   Writes user    #   Boolean      #   True/False    #  True if user is created #
#    check       #   Checks user    #   Boolean      #   True/False    #  True if info is correct #
#    manual      #   Encrypts file  #   None         #   None          #         None             #
#    manual      #   Decrypts file  #   None         #   None          #         None             #
#    delete      #   Deletes user   #   Boolean      #   True/False    #  True if user is deleted #
###################################################################################################

from cryptography.fernet import Fernet # import cryptography
import os # import os

usernames, passwords, username_index, password_index = [], [], [], [] # initialize lists for usernames, passwords, and indexes

class Encryptor: # create class
    def encrypt_file(file): # encrypts file
        with open('frontend/data/credentials.key', 'rb') as filekey: # open key file
            key = filekey.read() # read key
            filekey.close() # close key file    
        fernet = Fernet(key) # create fernet object
        with open(file, 'rb') as f: # open file
            original = f.read() # read file
            f.close() # close file
        encrypted = fernet.encrypt(original) # encrypt file
        with open(file, 'wb') as encrypted_file: # open file
            encrypted_file.write(encrypted) # write encrypted file
            encrypted_file.close() # close file
        return True # return true
        
    def decrypt_file(file): # decrypts file
        with open('frontend/data/credentials.key', 'rb') as filekey: # open key file
            key = filekey.read() # read key
            filekey.close() # close key file
        fernet = Fernet(key) # create fernet object
        with open(file, 'rb') as enc_file: # open file
            encrypted = enc_file.read() # read file
            enc_file.close() # close file
        decrypted = fernet.decrypt(encrypted) # decrypt file
        with open(file, 'wb') as dec_file: # open file 
            dec_file.write(decrypted) # write decrypted file
            dec_file.close() # close file
        return True # return true

    def generate_key(): # generates key
        key = Fernet.generate_key() # generate key
        with open('frontend/data/credentials.key', 'wb') as filekey: # open key file 
            filekey.write(key) # write key
        return True # return true
        
class rCredentials: # create class
    def read_usernames(): # reads usernames
        global usernames, username_index # make global
        with open("frontend/data/credentials.db", "r") as f: # open file
            data = f.readlines() # read file
            f.close() # close file
        for i in data: # loop through file
            if i.startswith("user"): # if line starts with user
                username = i.split("=")[1].strip() 
                try: # try    
                    username = username.replace('"', '') # replace quotes with nothing
                except Exception: # except 
                    pass # pass
                usernames.append(username) # append username to list
                index = int(i.split("user")[1].split("=")[0].strip()) # get index of username by splitting line and stripping
                username_index.append(index) # append index to list
    
    def read_passwords(): # reads passwords
        global passwords, password_index # make global
        with open("frontend/data/credentials.db", "r") as f: # open file
            data = f.readlines() # read file
            f.close() # close file
        for i in data: # loop through file
            if i.startswith("pass"): # if line starts with pass
                password = i.split("=")[1].strip() # get password by splitting line and stripping
                try: # try
                    password = password.replace('"', '') # replace quotes with nothing
                except Exception: # except
                    pass # pass
                passwords.append(password) # append password to list
                index = int(i.split("pass")[1].split("=")[0].strip()) # get index of password by splitting line and stripping
                password_index.append(index) # append index to list
    
class wCredentials: # create class
    def write_usernames(user): # writes usernames
        global usernames, username_index # make global
        index = max(username_index) + 1 # get index
        new_data = f'user{index} = "{user}"\n' # create new data
        with open("frontend/data/credentials.db", "r") as f: # open file
            for i in f.readlines(): # loop through file
                if i.split("=")[1].strip() == f'"{user}"': # if username is already in file
                    return False # return false
            f.close() # close file
        with open("frontend/data/credentials.db", "a") as f: # open file 
            f.write(new_data) # write new data
            f.close()
        return True # return true
    
    def write_passwords(password): # writes passwords
        global passwords, password_index # make global
        index = max(password_index) + 1 # get index 
        new_data = f'pass{index} = "{password}"\n' # create new data
        with open("frontend/data/credentials.db", "a") as f: # open file
            f.write(new_data) # write new data
            f.close() # close file
            
class cCredentials: # create class
    def check_pass(password, check_index): # checks passwords
        global passwords, password_index # make global
        for i in passwords: # loop through passwords
            if password == i and passwords.index(i) == check_index: # if password is correct
                return True # return true
        return False # return false
    
    def check_user(username, password): # checks usernames
        global usernames, username_index # make global 
        for i in usernames: # loop through usernames
            if username == i: # if username is correct
                check_index = usernames.index(i) # get index of username
                boolean = cCredentials.check_pass(password, check_index) # check password
                return boolean # return boolean
        return False # return false

class dCredentials: # create class
    def delete_user(username, password): # deletes user
        global usernames, username_index, passwords, password_index # make global
        if cCredentials.check_user(username, password): # if user is correct
            for i in usernames: # loop through usernames
                if username == i: # if username is correct
                    check_index = usernames.index(i) + 1 # get index of username 
                    with open("frontend/data/credentials.db", "r") as f: # open file
                        data = f.readlines() # read file
                        f.close() # close file
                    with open("frontend/data/credentials.db", "w") as f: # open file
                        for i in data: # loop through file
                            if i.startswith("user") and int(i.split("user")[1].split("=")[0].strip()) == check_index: # if line starts with user and index is correct
                                pass # pass
                            elif i.startswith("pass") and int(i.split("pass")[1].split("=")[0].strip()) == check_index: # if line starts with pass and index is correct
                                pass  # pass
                            else: # if line is not user or pass
                                f.write(i) # write data
                        f.close() # close file
                    return True # return true
        else: # if user is not correct
            return False # return false

class Credentials: # create class
    def __init__(self) -> None: # init function
        if os.path.exists("frontend/data/credentials.key"): # if key exists
            Encryptor.decrypt_file("frontend/data/credentials.db") # decrypt file
        else: # if key does not exist
            Encryptor.generate_key() # generate key
        rCredentials.read_usernames() # read usernames
        rCredentials.read_passwords() # read passwords
        Encryptor.encrypt_file("frontend/data/credentials.db") # encrypt file
        
    def write(self, user, password) -> bool: # write function
        if os.path.exists("frontend/data/credentials.key"): # if key exists
            Encryptor.decrypt_file("frontend/data/credentials.db") # decrypt file
        check = wCredentials.write_usernames(user) # write usernames
        if check is True: # if username is not already in file
            wCredentials.write_passwords(password) # write passwords
            Encryptor.encrypt_file("frontend/data/credentials.db") # encrypt file
            return True # return true
        else: # if username is already in file
            Encryptor.encrypt_file("frontend/data/credentials.db") # encrypt file
            return False # return false
    
    def check(self, username, password) -> bool: # check function
        return cCredentials.check_user(username, password) # return check user
    
    def manual_encrypt(): # manual encrypt function
        Encryptor.encrypt_file("frontend/data/credentials.db") # encrypt file
        return True # return true
        
    def manual_decrypt(): # manual decrypt function
        Encryptor.decrypt_file("frontend/data/credentials.db") # decrypt file
        return  True # return true
    
    def delete(self, username) -> bool: # delete function 
        if os.path.exists("frontend/data/credentials.key"): # if key exists
            Encryptor.decrypt_file("frontend/data/credentials.db") # decrypt file
        check = dCredentials.delete_user(username) # delete user
        if check is True: # if user is deleted
            Encryptor.encrypt_file("frontend/data/credentials.db") # encrypt file
            return True # return true
        else: # if user is not deleted
            Encryptor.encrypt_file("frontend/data/credentials.db") # encrypt file
            return False # return false
        
if __name__ == "__main__": # if file is run directly
    cred = Credentials() # create credentials object
    print(usernames) # print usernames
    print(passwords) # print passwords
    print(cred.write("testuser", "user")) # write user
    print("The next function will not work until the program is restarted") # print message
    print(cred.check("testuser", "user")) # check user
    print("The next function will not work until the program is restarted") # print message
    print(cred.delete("testuser")) # delete user