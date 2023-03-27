################################################################################
## Author: Selegean Marius                                                     #
## Email: marius.selegean@yahoo.com                                            #
## Description: Move files in named folders grouped by their extensions types  #
## Date: 22/03/2023                                                            #
# This version is removes all the inputs from user                             #
################################################################################
"""
If needed, this script can be inserted into an automatic task, running in background
and can be set at certain days at specific hours to run and find the mentioned files
moving them automatically in specified folders.
Always please remember to change the os.chdir with your path.
Place the script into the folder you want to organize your files.
"""

# Import packages
import os
import glob
import sys
import time
import logging
import datetime

'''
Create a new folders for each configured extensions
'''

# Path - please change ot by your needs.
os.chdir  # = (r'C:\Users\mselegean\Documents\Personal\Test_move_files')

"""
This code will check if the folders already exist.
If the folders exist then creation is skipped
If folder does not exist, then the folder will be created.
"""
log = open("logs.log", "a")
# Create folders
if not os.path.exists('MP3'):
    os.mkdir('MP3')
    print('New folder MP3 created.')
    log.write(f"[{datetime.datetime.now()}]\tNew folder MP3 created.\n")
if not os.path.exists('TEXT'):
    os.mkdir('TEXT')
    print('New folder TEXT created.')
    log.write(f"[{datetime.datetime.now()}]\tNew folder TEXT created.\n")
if not os.path.exists('PDF'):
    os.mkdir('PDF')
    print('New folder PDF created.')
    log.write(f"[{datetime.datetime.now()}]\tNew folder PDF created.\n")
if not os.path.exists('Excel'):
    os.mkdir('Excel')
    print('New folder Excel created.')
    log.write(f"[{datetime.datetime.now()}]\tNew folder Excel created.\n")
if not os.path.exists('Word'):
    os.mkdir('Word')
    print('New folder Word created.')
    log.write(f"[{datetime.datetime.now()}]\tNew folder Word created.\n")
if not os.path.exists('Pictures'):
    os.mkdir('Pictures')
    print('New folder Pictures created.')
    log.write(f"[{datetime.datetime.now()}]\tNew folder Pictures created.\n")
else:
    print('\n''Folders already created.''\n')
    log.write(f"[{datetime.datetime.now()}]\tFolders already created.\n")

# 1 second break
time.sleep(1)

# Variables
TEXT = '*.txt'
MP3 = '*.mp3'
PDF = '*.pdf'
Excel = '*.xlsx'
Word = '*.docx'
Pictures1 = '*.jp*'
# |*.jpeg|*.png'
Pictures2 = '*.png'

# Template
# Variable = '*.'


# Find and count TEXT files
count = 0
for file in glob.glob(TEXT, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} Text files."'\n')
log.write(f"[{datetime.datetime.now()}]\tFound {count} Text files..\n")

# Input from user - Move files
if count == 0:
    print("Skipping... moving to next folder.")
    log.write(f"[{datetime.datetime.now()}]\tSkipping... moving to next folder.\n")
else:
     '''move files found to TEXT folder'''
     for file in glob.glob(TEXT, recursive=False):
         os.rename(file, os.path.join('TEXT', os.path.basename(file)))
         print(f'{file} moved to TEXT folder')
         log.write(f"[{datetime.datetime.now()}]\t{count} moved to TEXT folder\n")

# 1 second break
time.sleep(1)

# Find and count MP3 files
count = 0
for file in glob.glob(MP3, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} Text files."'\n')
log.write(f"[{datetime.datetime.now()}]\tFound {count} MP3 files..\n")

# Input from user - Move files
if count == 0:
    print("Skipping... moving to next folder.")
    log.write(f"[{datetime.datetime.now()}]\tSkipping... moving to next folder.\n")
else:
    '''move files found to MP3 folder'''
    for file in glob.glob(MP3, recursive=False):
        os.rename(file, os.path.join('MP3', os.path.basename(file)))
        print(f'{file} moved to MP3 folder')
        log.write(f"[{datetime.datetime.now()}]\t{count} moved to MP3 folder\n")

# 1 second break
time.sleep(1)

# Find and count PDF files
count = 0
for file in glob.glob(PDF, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} Text files."'\n')
log.write(f"[{datetime.datetime.now()}]\tFound {count} PDF files..\n")

# Input from user - Move files
if count == 0:
    print("Skipping... moving to next folder.")
    log.write(f"[{datetime.datetime.now()}]\tSkipping... moving to next folder.\n")
else:
    '''move files found to PDF folder'''
    for file in glob.glob(PDF, recursive=False):
        os.rename(file, os.path.join('PDF', os.path.basename(file)))
        print(f'{file} moved to PDF folder')
        log.write(f"[{datetime.datetime.now()}]\t{count} moved to PDF folder\n")

# 1 second break
time.sleep(1)

# Find and count Excel files
count = 0
for file in glob.glob(Excel, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} Text files."'\n')
log.write(f"[{datetime.datetime.now()}]\tFound {count} Excel files..\n")

# Input from user - Move files
if count == 0:
    print("Skipping... moving to next folder.")
    log.write(f"[{datetime.datetime.now()}]\tSkipping... moving to next folder.\n")
else:
    '''move files found to Excel folder'''
    for file in glob.glob(Excel, recursive=False):
        os.rename(file, os.path.join('Excel', os.path.basename(file)))
        print(f'{file} moved to Excel folder')
        log.write(f"[{datetime.datetime.now()}]\t{count} moved to Excel folder\n")

# 1 second break
time.sleep(1)

# Find and count Word files
count = 0
for file in glob.glob(Word, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} Text files."'\n')
log.write(f"[{datetime.datetime.now()}]\tFound {count} Word files..\n")

# Input from user - Move files
if count == 0:
    print("Skipping... moving to next folder.")
    log.write(f"[{datetime.datetime.now()}]\tSkipping... moving to next folder.\n")
else:
    '''move files found to Word folder'''
    for file in glob.glob(Word, recursive=False):
        os.rename(file, os.path.join('Word', os.path.basename(file)))
        print(f'{file} moved to Word folder')
        log.write(f"[{datetime.datetime.now()}]\t{count} moved to Word folder\n")

# 1 second break
time.sleep(1)

# Template

"""
# Find and count Variable files
count = 0
for file in glob.glob(Word, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} Text files."'\n')
log.write(f"[{datetime.datetime.now()}]\tFound {count} Word files..\n")

# Input from user - Move files
if count == 0:
    print("Skipping... moving to next folder.")
    log.write(f"[{datetime.datetime.now()}]\tSkipping... moving to next folder.\n")
else:
    confirm = input('Do you want to move files to Word Folder? (y/n)')
    if confirm in ["Y", "y"]:
        '''move files found to Word folder'''
        for file in glob.glob(Word, recursive=False):
            os.rename(file, os.path.join('Word', os.path.basename(file)))
            print(f'{file} moved to Word folder')
            log.write(f"[{datetime.datetime.now()}]\t{count} moved to Word folder\n")


# 1 second break
time.sleep(1)
"""

# Find and count Pictures files
for file in glob.glob(Pictures1, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")
for file in glob.glob(Pictures2, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} Picture files."'\n')
log.write(f"[{datetime.datetime.now()}]\tFound {count} Picture files..\n")

# Input from user - Move files
if count == 0:
    # Because this is the last folder to scan and there is no other folder to be scanned, we can comment the print line.
    # If more folders will be added, uncomment the print line with message and comment the empty print.
    # print("Skipping... moving to next folder.")
    print("")
else:
    '''move files found to Pictures folder'''
    for file in glob.glob(Pictures1, recursive=False):
        os.rename(file, os.path.join('Pictures', os.path.basename(file)))
    for file in glob.glob(Pictures2, recursive=False):
        os.rename(file, os.path.join('Pictures', os.path.basename(file)))
    print(f'{file} moved to Pictures folder')
    log.write(f"[{datetime.datetime.now()}]\t{count} moved to Pictures folder\n")

print('\n''Operation completed!''\n')
log.write(f"[{datetime.datetime.now()}]\tOperation completed!\n")
log.close()
