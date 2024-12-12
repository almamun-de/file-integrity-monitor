# File Integrity Monitor Script

## Description

This Python script monitors specified files for any changes by calculating their SHA-256 hashes at regular intervals. If a file is modified, the script will notify the user. It is useful for detecting unauthorized or accidental file changes.

## How to Use

### 1. Clone the repository:

```bash
git clone https://github.com/almamun-de/file-integrity-monitor.git
cd file-integrity-monitor

Run the script:
python3 file_integrity_monitor.py

Enter the required information:
Enter a list of file paths (comma-separated) that you want to monitor.
Enter the time interval (in seconds) between file checks.
