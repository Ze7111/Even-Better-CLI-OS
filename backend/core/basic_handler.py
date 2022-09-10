'''
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
        