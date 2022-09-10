'''
 !/usr/bin/env python3
 Path: make.pyc / make.py
 Description: This program will create a good starting point for a python program.
 Author: @Ze7111
 License: MIT
'''
try: # try
    from rich import console; import os, logging, sys, time; import shutil; print = console.Console().print; import random;  # import modules
except: # if error
    import os # import os
    os.system('pip install rich') # install rich
    os.system('pip install shutil') # install shutil
    os.system('pip install random') # install random
    os.system('pip install logging') # install logging
    os.system('pip install sys') # install sys
    os.system('cls' if os.name == 'nt' else 'clear') # clear screen
    os.system('color a' if os.name == 'nt' else 'printf "\033[32m"') # set color to green
    print('Please run the program again.') # print error if file is imported
    exit() # exit program

print('Enter path to projects root dir (leave blank if already in the dir): ', style='bold red', end=''); path = input(); logging_file = f'make.py.log' # set logging file
if path == '':
    path = os.getcwd()
logging.basicConfig(level=logging.NOTSET,filename=logging_file, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%m-%y  %H:%M:%S') # Logging setup
logging.warning('Starting script...'); logging.info(f'Path: {path}')
admin_module_data = r"""'''
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
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1) # re-run the program with admin rights"""
basic_handling_data = (r"""'''
 !/usr/bin/env python3
 Path: backend/core/basic_handling.py
 Description: This file is used to innitiate the innit.py file and the logs folder. It also deletes old log files. and makes backups
 Author: @Ze7111
'''

# ====================================================================================== Default imports ======================================================================================
import sys, os, time, logging, shutil, tarfile; from rich import console; print = console.Console().print # import basic modules and rich                                                     |
log_datetimefmt = time.strftime('%d-%m-%Y %H-%M-%S',time.localtime(time.time())) # set log datetime format                                                                                    |
logging_file = f'logs/{log_datetimefmt}.log' # set logging file                                                                                                                               |
# =============================================================================================================================================================================================

# ====================== Global Variables ======================
rundone = False # set rundone to false                         |
rundone2 = False # set rundone2 to false                       |
#                                                              |
logging_maxFiles = 5 # set max number of log files             |
max_backups = 4 # set max backups to 10                        |
#                                                              |
this_file = os.path.basename(__file__) # get name of this file |
log_folder_name = f'{os.getcwd()}/logs/' # set log folder name |
# ==============================================================

# ================================================================================ Logging Setup ================================================================================
logging.basicConfig(level=logging.NOTSET,filename=logging_file, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%m-%y  %H:%M:%S') # Logging setup |
# ===============================================================================================================================================================================


class file_actions():  # log_file_actions class
    def count_log_files(directory): # count log files function
        global rundone # set rundone to global
        if rundone is not True: # if rundone is not true
            logging.info(f'count_log_files function is starting in file {__file__}') # log that count_log_files function is starting
        try: # try
            list_of_files = os.listdir(directory) # get list of files in directory
            log_files_path = ['logs/{0}'.format(x) for x in list_of_files] # get path of log files
        except Exception as e: # if error
            logging.error(f'count_log_files function FAILED in file {__file__} with error: {e}') # log that count_log_files function failed
            return None # return none
        if rundone is not True: # if rundone is not true
            logging.info(f'count_log_files function is finsihed in file {__file__}') # log that count_log_files function is finsihed
            rundone = True # set rundone to true
        return log_files_path # return log files path

    def count_backup_files(directory): # count log files function
        global rundone2 # set rundone to global
        if rundone2 is not True: # if rundone is not true
            logging.info(f'count_backup_files function is starting in file {__file__}') # log that count_log_files function is starting
        try: # try
            list_of_files = os.listdir(directory) # get list of files in directory
            log_files_path = ['backups/{0}'.format(x) for x in list_of_files] # get path of log files
        except Exception as e: # if error
            logging.error(f'count_backup_files function FAILED in file {__file__} with error: {e}') # log that count_log_files function failed
            return None # return none
        if rundone2 is not True: # if rundone is not true
            rundone2 = True # set rundone to true
        return log_files_path # return log files path
    
    def delete_logs(): # delete logs function
        global logging_maxFiles, log_folder_name # set logging_maxFiles and log_folder_name to global
        if len(file_actions.count_log_files(log_folder_name)) >= logging_maxFiles: # if number of files in ./logs is greater than 10 
            logging.info(f'Number of log files in ./logs is {len(file_actions.count_log_files(log_folder_name))} before deletion') # log number of files ./logs
            while len(file_actions.count_log_files(log_folder_name)) > logging_maxFiles: # while number of files in ./logs is greater than 10
                oldest_file = min(file_actions.count_log_files(log_folder_name), key=os.path.getctime) # get oldest file in ./logs
                os.remove(oldest_file) # remove oldest file in ./logs
                logging.info(f'Removed log file {oldest_file} in ./logs') # log number of files ./logs
            logging.info(f'Number of log files in ./logs is {len(file_actions.count_log_files(log_folder_name))} after deletion') # log number of files ./logs
            
    def create_zip_backup():
        logging.info(f'create_zip_backup function is starting in file {__file__}') # log that create_zip_backup function is starting
        global max_backups # set max_backups to global
        backup_path = f'{os.getcwd()}\\backups\\' # set backup path
        project_name = os.path.basename(os.getcwd()) # get project name
        temp_dir = os.path.join('C:\\Temp', project_name) # set temp_dir to C:\Temp\project_name
        folder_time = time.strftime('%d-%m-%Y %H-%M-%S',time.localtime(time.time())) # set log datetime format
        logging.info(f'Folder time set to {folder_time}') # log folder time
        try: # try
            logging.info(f'Creating backup of {project_name} in {temp_dir}') # log that backup is being created
            shutil.copytree(os.getcwd(), temp_dir + folder_time) # copy all files in current directory to temp directory
            shutil.rmtree(temp_dir + folder_time + '\\backups') # remove backups folder
            logging.info(f'Backup of {project_name} created in {temp_dir}') # log that backup is created
            shutil.make_archive(backup_path + folder_time, 'zip', temp_dir + folder_time) # create zip file
            logging.info(f'Zip file of {project_name} created in {backup_path}') # log that zip file is created
            time.sleep(0.5) # sleep for 0.5 seconds
            shutil.rmtree(temp_dir + folder_time, ignore_errors=True) # delete temp directory
            logging.info(f'Temp directory {temp_dir + folder_time} deleted') # log that temp directory is deleted
            shutil.rmtree(temp_dir, ignore_errors=True) # delete temp directory
            logging.info(f'Temp directory {temp_dir} deleted') # log that temp directory is deleted
        except Exception as e: # if error
            logging.error(f'Backup of {project_name} FAILED with error: {e}') # log that backup failed
            return 'failed' # return failed
        #delete old backups
        try: # try
            if len(file_actions.count_backup_files(backup_path)) >= max_backups: # if number of files in ./logs is greater than 10 
                while len(file_actions.count_backup_files(backup_path)) > max_backups: # while number of files in ./logs is greater than 10
                    oldest_file = min(file_actions.count_backup_files(backup_path), key=os.path.getctime) # get oldest file in ./logs
                    logging.info(f'Removed backup file {oldest_file} in ./backups') # log number of files ./logs
                    os.remove(oldest_file) # remove oldest file in ./logs
        except FileNotFoundError as e: # if error
            logging.error(f'create_zip_backup function FAILED in file {__file__} with error: {e}') # log that create_zip_backup function failed

        logging.info(f'create_zip_backup function is finsihed in file {__file__}') # log that create_zip_backup function is finsihed
        return 'success' # return success
        """)
innit_data = (r"""'''
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
    print('This file is not meant to be imported.', style='bold red') # print error if file is imported""")

license = (r"""Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License
By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.

Section 1 – Definitions.

Adapted Material means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.
Copyright and Similar Rights means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section 2(b)(1)-(2) are not Copyright and Similar Rights.
Effective Technological Measures means those measures that, in the absence of proper authority, may not be circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar international agreements.
Exceptions and Limitations means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.
Licensed Material means the artistic or literary work, database, or other material to which the Licensor applied this Public License.
Licensed Rights means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.
Licensor means the individual(s) or entity(ies) granting rights under this Public License.
NonCommercial means not primarily intended for or directed towards commercial advantage or monetary compensation. For purposes of this Public License, the exchange of the Licensed Material for other material subject to Copyright and Similar Rights by digital file-sharing or similar means is NonCommercial provided there is no payment of monetary compensation in connection with the exchange.
Share means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.
Sui Generis Database Rights means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.
You means the individual or entity exercising the Licensed Rights under this Public License. Your has a corresponding meaning.
Section 2 – Scope.

License grant.
Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:
reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and
produce and reproduce, but not Share, Adapted Material for NonCommercial purposes only.
Exceptions and Limitations. For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.
Term. The term of this Public License is specified in Section 6(a).
Media and formats; technical modifications allowed. The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section 2(a)(4) never produces Adapted Material.
Downstream recipients.
Offer from the Licensor – Licensed Material. Every recipient of the Licensed Material automatically receives an offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.
No downstream restrictions. You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.
No endorsement. Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section 3(a)(1)(A)(i).
Other rights.

Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.
Patent and trademark rights are not licensed under this Public License.
To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties, including when the Licensed Material is used other than for NonCommercial purposes.
Section 3 – License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the following conditions.

Attribution.

If You Share the Licensed Material, You must:

retain the following if it is supplied by the Licensor with the Licensed Material:
identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);
a copyright notice;
a notice that refers to this Public License;
a notice that refers to the disclaimer of warranties;
a URI or hyperlink to the Licensed Material to the extent reasonably practicable;
indicate if You modified the Licensed Material and retain an indication of any previous modifications; and
indicate the Licensed Material is licensed under this Public License, and include the text of, or the URI or hyperlink to, this Public License.
For the avoidance of doubt, You do not have permission under this Public License to Share Adapted Material.
You may satisfy the conditions in Section 3(a)(1) in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.
If requested by the Licensor, You must remove any of the information required by Section 3(a)(1)(A) to the extent reasonably practicable.
Section 4 – Sui Generis Database Rights.

Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:

for the avoidance of doubt, Section 2(a)(1) grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database for NonCommercial purposes only and provided You do not Share Adapted Material;
if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material; and
You must comply with the conditions in Section 3(a) if You Share all or a substantial portion of the contents of the database.
For the avoidance of doubt, this Section 4 supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.
Section 5 – Disclaimer of Warranties and Limitation of Liability.

Unless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.
To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.
The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.
Section 6 – Term and Termination.

This Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.
Where Your right to use the Licensed Material has terminated under Section 6(a), it reinstates:

automatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or
upon express reinstatement by the Licensor.
For the avoidance of doubt, this Section 6(b) does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.
For the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.
Sections 1, 5, 6, 7, and 8 survive termination of this Public License.
Section 7 – Other Terms and Conditions.

The Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.
Any arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and conditions of this Public License.
Section 8 – Interpretation.

For the avoidance of doubt, this Public License does not, and shall not be interpreted to, reduce, limit, restrict, or impose conditions on any use of the Licensed Material that could lawfully be made without permission under this Public License.
To the extent possible, if any provision of this Public License is deemed unenforceable, it shall be automatically reformed to the minimum extent necessary to make it enforceable. If the provision cannot be reformed, it shall be severed from this Public License without affecting the enforceability of the remaining terms and conditions.
No term or condition of this Public License will be waived and no failure to comply consented to unless expressly agreed to by the Licensor.
Nothing in this Public License constitutes or may be interpreted as a limitation upon, or waiver of, any privileges and immunities that apply to the Licensor or You, including from the legal processes of any jurisdiction or authority.
Creative Commons is not a party to its public licenses. Notwithstanding, Creative Commons may elect to apply one of its public licenses to material it publishes and in those instances will be considered the “Licensor.” The text of the Creative Commons public licenses is dedicated to the public domain under the CC0 Public Domain Dedication. Except for the limited purpose of indicating that material is shared under a Creative Commons public license or as otherwise permitted by the Creative Commons policies published at creativecommons.org/policies, Creative Commons does not authorize the use of the trademark “Creative Commons” or any other trademark or logo of Creative Commons without its prior written consent including, without limitation, in connection with any unauthorized modifications to any of its public licenses or any other arrangements, understandings, or agreements concerning use of licensed material. For the avoidance of doubt, this paragraph does not form part of the public licenses.

Creative Commons may be contacted at creativecommons.org.""")

def exit_seq(): # exit sequence
    global path # set path to global
    logging.info('Exiting Program...') # log that program is exiting
    try: # try
        with open(f'{path}/make.py.log', 'r') as f: # open make.py.log
            data = f.readlines() # read lines
            for line in data: # for line in data
                line = line.replace('\n', '') # remove \n
                print(line, style='bold red') # print error if file is imported
                time.sleep(random.uniform(0.0, 0.2)) # sleep for 0.0 to 0.2 seconds
            f.close() # close file
    except Exception as e: # if error
        logging.error(f'Error reading log file: {e}') # log error
    finally: # finally
        logging.warning('Finished :)') # log that program is exiting
        logging.shutdown() # shutdown logging
        sys.exit() # exit program

class files(): # files class
    def innit_file(): # innit file
        logging.warning('Creating innit file...') # log that innit file is being created
        global path, innit_data # set innit_data to global
        path2 = f"{path}/innit.py" # set path2 to innit.py
        logging.info(f'Innit.py File Path: {path2}') # log innit.py file path
        with open(path2, 'w') as f: # open innit.py
            logging.info('Writing innit file...') # log that innit file is being written
            f.write(innit_data) # write innit_data to innit.py
            logging.info(f'Data being written to innit file :\n{innit_data}\n') # log innit_data
            logging.warning('Innit file created.') # log that innit file is created
            f.close # close innit.py
        with open(f"{path}/LICENSE", 'w') as f:
            f.write(license)
            f.close()
            
    def basic_handeler(): # basic handeler file
        logging.warning('Creating basic_handeler file...') # log that basic_handeler file is being created
        global path, basic_handling_data # set basic_handling_data to global
        path2 = f"{path}/backend/core/basic_handler.py" # set path2 to backend/core/basic_handler.py
        logging.info(f'basic_handling.py File Path: {path2}') # log basic_handling.py file path
        with open(path2, 'w') as f: # open basic_handling.py
            logging.info('Writing basic_handeler file...') # log that basic_handeler file is being written
            f.write(basic_handling_data) # write basic_handling_data to basic_handling.py
            logging.info(f'Data being written to basic_handler file :\n{basic_handling_data}\n') # log basic_handling_data
            logging.warning('basic_handeler file created.') # log that basic_handeler file is created
            f.close # close basic_handling.py     
            
    def admin_module(): # admin module file
        logging.warning('Creating admin_module file...') # log that admin_module file is being created
        global path, admin_module_data # set admin_module_data to global
        path2 = f"{path}/backend/modules/admin.py" # set path2 to backend/modules/admin.py
        logging.info(f'admin.py File Path: {path2}') # log admin.py file path
        with open(path2, 'w') as f: # open admin.py
            logging.info('Writing admin_module file...') # log that admin_module file is being written
            f.write(admin_module_data) # write admin_module_data to admin.py
            logging.info(f'Data being written to admin_module file :\n{admin_module_data}\n') # log admin_module_data
            logging.warning('admin_module file created.') # log that admin_module file is created
            f.close # close admin.py 
            
class folders(): # folders class
    def innit_folder_structure(): # innit folder structure function
        try: # try
            logging.warning('Creating innit folder structure...') # log that innit folder structure is being created
            global path # set path to global
            
            os.mkdir(f'{path}/logs') # create logs folder
            logging.warning('Created logs folder.') # log that logs folder is created

            os.mkdir(f'{path}/database') # create database folder
            logging.warning('Created database folder.') # log that database folder is created

            os.mkdir(f'{path}/config') # create config folder
            logging.warning('Created config folder.') # log that config folder is created

            os.mkdir(f'{path}/backups') # create backups folder
            logging.warning('Created backups folder.') # log that backups folder is created

            os.mkdir(f'{path}/build') # create build folder
            logging.warning('Created build folder.') # log that build folder is created

            os.mkdir(f'{path}/backend') # create backend folder
            logging.warning('Created backend folder.') # log that backend folder is created

            os.mkdir(f'{path}/backend/classes') # create backend/classes folder
            logging.warning('Created backend/classes folder.') # log that backend/classes folder is created

            os.mkdir(f'{path}/backend/functions') # create backend/functions folder
            logging.warning('Created backend/functions folder.') # log that backend/functions folder is created

            os.mkdir(f'{path}/backend/core') # create backend/core folder
            logging.warning('Created backend/core folder.') # log that backend/core folder is created

            os.mkdir(f'{path}/backend/data') # create backend/data folder
            logging.warning('Created backend/data folder.') # log that backend/data folder is created

            os.mkdir(f'{path}/backend/modules') # create backend/modules folder
            logging.warning('Created backend/modules folder.') # log that backend/modules folder is created

            os.mkdir(f'{path}/frontend') # create frontend folder
            logging.warning('Created frontend folder.') # log that frontend folder is created

            os.mkdir(f'{path}/frontend/client') # create frontend/client folder
            logging.warning('Created frontend/client folder.') # log that frontend/client folder is created

            os.mkdir(f'{path}/frontend/server') # create frontend/server folder
            logging.warning('Created frontend/server folder.') # log that frontend/server folder is created

            os.mkdir(f'{path}/frontend/assets') # create frontend/assets folder
            logging.warning('Created frontend/assets folder.') # log that frontend/assets folder is created

            os.mkdir(f'{path}/frontend/data') # create frontend/data folder
            logging.warning('Created frontend/data folder.') # log that frontend/data folder is created

            os.mkdir(f'{path}/frontend/core') # create frontend/core folder
            logging.warning('Created frontend/core folder.') # log that frontend/core folder is created
 
            os.mkdir(f'{path}/frontend/functions') # create frontend/functions folder
            logging.warning('Created frontend/functions folder.') # log that frontend/functions folder is created

            os.mkdir(f'{path}/frontend/classes') # create frontend/classes folder
            logging.warning('Created frontend/classes folder.') # log that frontend/classes folder is created

            os.mkdir(f'{path}/src') # create src folder
            logging.warning('Created src folder.') # log that src folder is created

            os.mkdir(f'{path}/src/client') # create src/client folder
            logging.warning('Created src/client folder.') # log that src/client folder is created

            os.mkdir(f'{path}/src/server') # create src/server folder
            logging.warning('Created src/server folder.') # log that src/server folder is created

            os.mkdir(f'{path}/src/assets') # create src/assets folder
            logging.warning('Created src/assets folder.') # log that src/assets folder is created

            os.mkdir(f'{path}/src/data') # create src/data folder
            logging.warning('Created src/data folder.') # log that src/data folder is created

            os.mkdir(f'{path}/src/core') # create src/core folder
            logging.warning('Created src/core folder.') # log that src/core folder is created

            os.mkdir(f'{path}/src/functions') # create src/functions folder
            logging.warning('Created src/functions folder.') # log that src/functions folder is created

            os.mkdir(f'{path}/src/classes') # create src/classes folder
            logging.warning('Created src/classes folder.') # log that src/classes folder is created

            os.mkdir(f'{path}/src/dependencies') # create src/dependencies folder
            logging.warning('Created dependencies folder.') # log that dependencies folder is created
            
            logging.warning('Innit folder structure created.') # log that innit folder structure is created
            
        except FileExistsError: # if folder already exists
            logging.warning('Innit folder structure already exists.') # log that innit folder structure already exists
            
        except Exception as e: # if error
            logging.error(f'Error creating innit folder structure: {e}') # log error creating innit folder structure
            
        return True # return True
           
if __name__ == '__main__': # if __name__ == __main__
    try: # try
        files.innit_file() # innit file
        folders.innit_folder_structure() # innit folder structure
        files.basic_handeler() # run basic_handeler function
        files.admin_module() # run admin_module function
        exit_seq() # exit sequence
    except KeyboardInterrupt: # if keyboard interrupt
        print('Keyboard Interrupt Detected. Exiting...', style='red') # print keyboard interrupt detected
        exit_seq() # exit sequence
    except Exception as e: # if error
        print(f'Error: {e}', style='red') # print error
    finally: # finally
        exit() # exit