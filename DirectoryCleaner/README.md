# Directory Cleaner & Duplicate File Remover


👨‍💻 Author :- Om Ravindra Wakhare

This Python script automates the process of scanning a directory, identifying duplicate files based on their **MD5 checksum**, and deleting the duplicates.  
It also supports generating logs and providing helpful instructions through command-line arguments.

---

## 📂 Features
- **Checksum Calculation**: Calculates the MD5 hash of every file to identify duplicates.
- **Duplicate Detection**: Finds all files with the same checksum (byte-by-byte identical).
- **Duplicate Deletion**: Deletes all duplicates except the first occurrence.
- **Logging**: Creates a log file with a timestamp.
- **Cross-Platform**: Works on Windows, Linux, and macOS.

---

## ⚙️ How It Works
1. **CalculateCheckSum**: Reads each file in binary mode and computes the MD5 hash.
2. **FindDuplicate**: Traverses the given directory recursively and maps checksums to file paths.
3. **DisplayResult**: Displays all duplicate files.
4. **DeleteDuplicate**: Deletes duplicate files, keeping only one copy of each.
5. **Command-Line Interface**: Handles arguments for help, usage instructions, and directory input.

---

## 🖥️ Usage

### 1️⃣ Basic Command
```bash
python ScriptName.py <DirectoryPath>
```
- `<DirectoryPath>`: Absolute or relative path of the directory you want to scan.

Example:
```bash
python ScriptName.py /home/user/Documents
```

### 2️⃣ Help
Displays help information about the script:
```bash
python ScriptName.py --h
```

### 3️⃣ Usage Instructions
Displays usage details:
```bash
python ScriptName.py --u
```

---

## 📝 Log File
- A log file is created in the current working directory with the format:
  ```
  Directorylog<timestamp>.log
  ```
- Example:  
  ```
  DirectorylogThu_Sep_18_10_30_00_2025.log
  ```

---

## 🛠️ Functions Overview
| Function Name       | Description                                                        |
|---------------------|--------------------------------------------------------------------|
| `CalculateCheckSum` | Calculates MD5 hash of a file in binary mode.                      |
| `DirectoryWatcher`  | Generates a log file for all files and their checksums.            |
| `FindDuplicate`     | Finds duplicate files in a directory using their checksum values.   |
| `DisplayResult`     | Prints duplicate file paths to the console.                         |
| `DeleteDuplicate`   | Deletes duplicate files, keeping only one copy.                     |
| `main`              | Handles command-line arguments and orchestrates the script logic.   |

---

## ⚠️ Important Notes
- **Irreversible Deletion**: Deleted duplicates cannot be recovered. Use with caution.
- **Permissions**: Make sure you have read & write permissions for the target directory.
- **Large Directories**: For very large directories, scanning might take some time.

---

## 🧩 Requirements
- **Python 3.x**
- Works on:
  - Windows
  - Linux
  - macOS

No external Python libraries are required; only built-in modules are used:
- `os`
- `sys`
- `time`
- `hashlib`

---

## 🧑‍💻 Example Output
```
-------------------------------------------------------------
----------------- Directory Automation ---------------------
-------------------------------------------------------------

/home/user/Documents/sample1.txt
/home/user/Documents/copy_of_sample1.txt
------------------------------------
Value of Count is : 2
------------------------------------
Deleted file : /home/user/Documents/copy_of_sample1.txt
Total deleted file : 1

-------------------------------------------------------------
------------- Thank you for using our script ----------------
-------------------------------------------------------------
```

---


## 👨‍💻 Author

Developed by **Swaraj Santoshrao More**
📧 Contact: moreswaraj9@gmail(mailto:your.moreswaraj9@gmail.com)