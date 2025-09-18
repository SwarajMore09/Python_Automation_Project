# Sys_Mon - Process Monitor

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![psutil](https://img.shields.io/badge/dependency-psutil-green.svg)](https://pypi.org/project/psutil/)

**Sys_Mon** (*Process Monitor*) is a lightweight Python tool to monitor running processes and generate detailed log files with timestamped filenames. It helps in auditing, debugging, and analyzing system activity.

---

## ✨ Features

* 🔍 Scan all running processes with:

  * Process ID (PID)
  * Process Name
  * Username
  * Virtual Memory Size (in MB)
* 🗂️ Generate timestamped log files automatically.
* 📁 Store logs in a dedicated `Sys_MonLogs` directory.
* ⚡ Works on Windows, Linux, and macOS.

---

## 🛠️ Requirements

* Python 3.7+
* psutil library

Install dependencies:

```bash
pip install psutil
```

---

## 🚀 Usage

Run the script:

```bash
python Sys_Mon.py
```

A new log file will be created in the `Sys_MonLogs` folder.

Example log file name:

```
Sys_Mon_ThuSep18_2025_17_45_23.log
```

---

## 📄 Example Log Output

```
--------------------------------------------------------------------------------
        Sys_Mon - Process Log
        Log File created at: Thu Sep 18 17:45:23 2025
--------------------------------------------------------------------------------

{'pid': 1234, 'name': 'python.exe', 'username': 'Om', 'vms': 55.81}
{'pid': 5678, 'name': 'chrome.exe', 'username': 'Om', 'vms': 220.12}

--------------------------------------------------------------------------------
```

---

## 📂 Project Structure

```
.
├── Sys_Mon.py          # Main script
├── README.md           # Documentation
└── Sys_MonLogs/        # Auto-generated log files
```

---

## 🧑‍💻 Development

Clone the repository:

```bash
git clone https://github.com/your-username/Sys_Mon.git
cd Sys_Mon
```

Run locally:

```bash
python Sys_Mon.py
```

---

## 🤝 Contributing

Contributions are welcome!

* Open an [issue](https://github.com/your-username/Sys_Mon/issues)
* Submit a [pull request](https://github.com/your-username/Sys_Mon/pulls)

---


---

## 👨‍💻 Author

Developed by **Swaraj Santoshrao More**
📧 Contact: moreswaraj9@gmail(mailto:your.moreswaraj9@gmail.com)
