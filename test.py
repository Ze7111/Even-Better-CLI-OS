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
usernames, passwords, username_index, password_index = [], [], [], []
class Encryptor:
    def encrypt_file(file):
        with open('frontend/data/credentials.key', 'rb') as filekey:
            key = filekey.read()
            filekey.close()
            
        fernet = Fernet(key)
        
        with open(file, 'rb') as f:
            original = f.read()
            f.close()
            
        encrypted = fernet.encrypt(original)
        
        with open(file, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            encrypted_file.close()
            
        return True
        
    def decrypt_file(file):
        with open('frontend/data/credentials.key', 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        with open(file, 'rb') as enc_file:
            encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
        with open(file, 'wb') as dec_file:
            dec_file.write(decrypted)
        return True

    def generate_key():
        key = Fernet.generate_key()
        with open('frontend/data/credentials.key', 'wb') as filekey:
            filekey.write(key)
        return True
        
class rCredentials:
    def read_usernames():
        global usernames, username_index
        with open("frontend/data/credentials.db", "r") as f:
            data = f.readlines()
        for i in data:
            if i.startswith("user"):
                username = i.split("=")[1].strip()
                try:
                    username = username.replace('"', '')
                except Exception:
                    pass
                usernames.append(username)
                index = int(i.split("user")[1].split("=")[0].strip())
                username_index.append(index)
    
    def read_passwords():
        global passwords, password_index
        with open("frontend/data/credentials.db", "r") as f:
            data = f.readlines()
        for i in data:
            if i.startswith("pass"):
                password = i.split("=")[1].strip()
                try:
                    password = password.replace('"', '')
                except Exception:
                    pass
                passwords.append(password)
                index = int(i.split("pass")[1].split("=")[0].strip())
                password_index.append(index)
    
class wCredentials:
    def write_usernames(user):
        global usernames, username_index
        index = max(username_index) + 1
        new_data = f'user{index} = "{user}"\n'
        with open("frontend/data/credentials.db", "r") as f:
            for i in f.readlines():
                if i.split("=")[1].strip() == f'"{user}"':
                    return False
        with open("frontend/data/credentials.db", "a") as f:
            f.write(new_data)
        return True
    
    def write_passwords(password):
        global passwords, password_index
        index = max(password_index) + 1
        new_data = f'pass{index} = "{password}"\n'
        with open("frontend/data/credentials.db", "a") as f:
            f.write(new_data)
            
class cCredentials:
    def check_pass(password, check_index):
        global passwords, password_index
        for i in passwords:
            if password == i and passwords.index(i) == check_index:
                return True
        return False
    
    def check_user(username, password):
        global usernames, username_index
        for i in usernames:
            if username == i:
                check_index = usernames.index(i)
                boolean = cCredentials.check_pass(password, check_index)
                return boolean
        return False

class dCredentials:
    def delete_user(username, password):
        global usernames, username_index, passwords, password_index
        if cCredentials.check_user(username, password):
            for i in usernames:
                if username == i:
                    check_index = usernames.index(i) + 1
                    with open("frontend/data/credentials.db", "r") as f:
                        data = f.readlines()
                    with open("frontend/data/credentials.db", "w") as f:
                        for i in data:
                            if i.startswith("user") and int(i.split("user")[1].split("=")[0].strip()) == check_index:
                                pass
                            elif i.startswith("pass") and int(i.split("pass")[1].split("=")[0].strip()) == check_index:
                                pass
                            else:
                                f.write(i)
                    return True
        else:
            return False

class Credentials:
    def __init__(self) -> None:
        if os.path.exists("frontend/data/credentials.key"):
            Encryptor.decrypt_file("frontend/data/credentials.db")
        else:
            Encryptor.generate_key()
        rCredentials.read_usernames()
        rCredentials.read_passwords()
        Encryptor.encrypt_file("frontend/data/credentials.db")
        
    def write(self, user, password) -> bool:
        if os.path.exists("frontend/data/credentials.key"):
            Encryptor.decrypt_file("frontend/data/credentials.db")
        check = wCredentials.write_usernames(user)
        if check is True:
            wCredentials.write_passwords(password)
            Encryptor.encrypt_file("frontend/data/credentials.db")
            return True
        else:
            Encryptor.encrypt_file("frontend/data/credentials.db")
            return False
    
    def check(self, username, password) -> bool:
        return cCredentials.check_user(username, password)
    
    def manual_encrypt():
        Encryptor.encrypt_file("frontend/data/credentials.db")
        return
        
    def manual_decrypt():
        Encryptor.decrypt_file("frontend/data/credentials.db")
        return 
    
    def delete(self, username) -> bool:
        if os.path.exists("frontend/data/credentials.key"):
            Encryptor.decrypt_file("frontend/data/credentials.db")
        check = dCredentials.delete_user(username)
        if check is True:
            Encryptor.encrypt_file("frontend/data/credentials.db")
            return True
        else:
            Encryptor.encrypt_file("frontend/data/credentials.db")
            return False
        
if __name__ == "__main__":
    cred = Credentials()
    print(usernames)
    print(passwords)
    print(cred.write("testuser", "user"))
    print("The next function will not work until the program is restarted")
    print(cred.check("testuser", "user"))
    print("The next function will not work until the program is restarted")
    print(cred.delete("testuser"))