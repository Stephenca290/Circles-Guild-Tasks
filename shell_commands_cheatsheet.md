# 🐚 Common Shell Command Cheatsheet

## 📁 Navigation
| Command      | Description                           |
|----------------|--------------------------------------|
| `pwd`           | Print working directory            |
| `ls`            | List files and directories         |
| `ls -la`        | List files with details (including hidden) |
| `cd <dir>`      | Change directory                  |
| `cd ..`         | Move to parent directory           |
| `cd ~`           | Move to home directory            |

---

## 📄 File Operations
| Command           | Description                      |
|-------------------|-----------------------------|
| `touch <filename>` | Create an empty file           |
| `cp <source> <dest>`| Copy files or directories     |
| `mv <source> <dest>`| Move or rename files/directories |
| `rm <filename>`     | Remove a file                |
| `rm -r <dir>`       | Remove a directory and its contents |
| `mkdir <dir>`       | Create a new directory       |
| `rmdir <dir>`       | Remove an empty directory    |
| `cat <filename>`    | View contents of a file       |
| `less <filename>`   | View contents page-by-page    |
| `head <filename>`  | View first lines of a file    |
| `tail <filename>`  | View last lines of a file     |

---

## 🔍 Searching and Viewing
| Command           | Description                      |
|-------------------|-----------------------------|
| `grep "pattern" <filename>` | Search for a pattern in a file |
| `find . -name "filename"`     | Find files by name |
| `locate <filename>`           | Quickly locate files by name |
| `wc <filename>`              | Count lines, words, and chars in a file |
| `sort <filename>`            | Sort lines in a file |
| `diff <file1> <file2>`      | Compare files line-by-line |

---

## 🛠️ System Info
| Command           | Description                      |
|-------------------|-----------------------------|
| `top`            | Show active processes           |
| `ps aux`        | List all running processes       |
| `kill <PID>`    | Kill process by ID               |
| `df -h`         | Disk usage information           |
| `du -h`         | Directory size usage             |
| `uptime`        | System uptime and load average  |
| `free -h`       | RAM and swap usage               |
| `history`       | List recently used commands      |
| `man <command>` | Show manual page for command     |

---

## 🗄️ Compression
| Command           | Description                      |
|-------------------|-----------------------------|
| `tar -cvf archive.tar <files>` | Create a tar archive |
| `tar -xvf archive.tar`           | Extract files from a tar archive |
| `gzip <filename>`               | Compress a file       |
| `gunzip <filename.gz>`           | Decompress a `.gz` file |
| `zip <archive.zip> <files>`      | Create a zip archive |
| `unzip <archive.zip>`            | Extract files from zip |

---

## 🔥 Networking
| Command            | Description                      |
|--------------------|-----------------------------|
| `ping <host>`       | Check connectivity to a host |
| `ifconfig` / `ip addr` | List IP addresses of interfaces |
| `curl <url>`        | Get the contents of a URL |
| `wget <url>`        | Download files from the internet |
| `ssh <user>@<host>` | Connect to a remote machine via SSH |
| `scp <source> <user>@<host>:<path>` | Copy files securely between hosts |

---

## ⚡️ Permissions
| Command            | Description                      |
|--------------------|-----------------------------|
| `chmod <mode> <filename>` | Change file or directory permission |
| `chown <user> <filename>` | Change owner of a file/directory |
| `chgrp <group> <filename>` | Change group of a file/directory |
| `sudo <command>`           | Run command as superuser |
