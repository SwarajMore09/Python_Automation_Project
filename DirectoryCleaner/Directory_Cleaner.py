###############################################################
# Project        : Directory_Cleaner - Directory Automation Tool
# Description    : Identifies and deletes duplicate files in a directory
# Author         : Your Name
# Date           : 2025-09-18
# Version        : 1.0.0
###############################################################

import os
import sys
import time
import hashlib
import schedule

###############################################################
# Function Name  : calculate_checksum
# Description    : Calculates MD5 checksum of a given file
# Parameters     : path (str), BlockSize (int)
# Returns        : str (checksum)
###############################################################
def calculate_checksum(path, BlockSize=1024):
    with open(path, 'rb') as fobj:
        hobj = hashlib.md5()
        buffer = fobj.read(BlockSize)
        while buffer:
            hobj.update(buffer)
            buffer = fobj.read(BlockSize)
    return hobj.hexdigest()

###############################################################
# Function Name  : directory_watcher
# Description    : Scans directory and logs file checksums
# Parameters     : DirectoryName (str)
# Returns        : None
###############################################################
def directory_watcher(DirectoryName="TargetDir"):
    if not os.path.isabs(DirectoryName):
        DirectoryName = os.path.abspath(DirectoryName)

    if not os.path.exists(DirectoryName):
        print("The path is invalid")
        exit()

    if not os.path.isdir(DirectoryName):
        print("Path is valid but the target is not a directory")
        exit()

    for FolderName, _, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            checksum = calculate_checksum(fname)
            print(f"File name : {fname}")
            print(f"Checksum : {checksum}\n")

    timestamp = time.ctime()
    filename = f"Directory_CleanerLog_{timestamp}.log".replace(" ", "").replace(":", "")

    with open(filename, "w") as fobj:
        Border = "-" * 54
        fobj.write(Border + "\n")
        fobj.write("This is a log file of Directory_Cleaner Automation Script\n")
        fobj.write("This is a Directory Cleaner Script\n")
        fobj.write(Border + "\n")
        fobj.write(f"Log created at: {timestamp}\n")
        fobj.write(Border + "\n")

###############################################################
# Function Name  : find_duplicate
# Description    : Finds duplicate files based on checksum
# Parameters     : DirectoryName (str)
# Returns        : dict (checksum -> list of files)
###############################################################
def find_duplicate(DirectoryName="TargetDir"):
    if not os.path.isabs(DirectoryName):
        DirectoryName = os.path.abspath(DirectoryName)

    if not os.path.exists(DirectoryName):
        print("The path is invalid")
        exit()

    if not os.path.isdir(DirectoryName):
        print("Path is valid but the target is not a directory")
        exit()

    Duplicate = {}
    for FolderName, _, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            checksum = calculate_checksum(fname)
            Duplicate.setdefault(checksum, []).append(fname)

    return Duplicate

###############################################################
# Function Name  : display_result
# Description    : Displays duplicate files grouped by checksum
# Parameters     : MyDict (dict)
# Returns        : None
###############################################################
def display_result(MyDict):
    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))
    for group in Result:
        for file in group:
            print(file)
        print("-------------------------------")
        print(f"Duplicate count in group: {len(group)}")
        print("-------------------------------")

###############################################################
# Function Name  : delete_duplicate
# Description    : Deletes duplicate files, keeping one copy
# Parameters     : Path (str)
# Returns        : None
###############################################################
def delete_duplicate(Path="TargetDir"):
    MyDict = find_duplicate(Path)
    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    deleted_count = 0
    for group in Result:
        for idx, file in enumerate(group):
            if idx > 0:  # keep first file, delete rest
                print(f"Deleted file : {file}")
                os.remove(file)
                deleted_count += 1

    print(f"Total deleted files : {deleted_count}")

###############################################################
# Function Name  : main
# Description    : Entry point for script execution
# Parameters     : None
# Returns        : None
###############################################################
def main():
    Border = "-" * 54
    print(Border)
    print("------------- Directory_Cleaner Automation -------------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1].lower() == "--h":
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif sys.argv[1].lower() == "--u":
            print("Usage:")
            print("python duplicate_cleaner.py <DirectoryPath> <TimeInterval>")
            print("Provide valid absolute path and time interval in minutes")

    elif len(sys.argv) == 3:
        schedule.every(int(sys.argv[2])).minutes.do(lambda: delete_duplicate(sys.argv[1]))

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Flags:")
        print("--h : Display help")
        print("--u : Display usage")

    print(Border)
    print("----------- Thank you for using our script ------------")
    print("---------------- Directory_Cleaner Tool ----------------")
    print(Border)

if __name__ == "_main_":
    main()