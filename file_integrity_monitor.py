import hashlib
import os
import time

def hash_file(filename):
    """
    Generates SHA-256 hash of the specified file.
    
    :param filename: The file to hash.
    :return: The SHA-256 hash of the file.
    """
    sha256_hash = hashlib.sha256()
    
    try:
        with open(filename, "rb") as file:
            while chunk := file.read(4096):
                sha256_hash.update(chunk)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None
    
    return sha256_hash.hexdigest()

def monitor_files(file_list, interval):
    """
    Monitors the specified files for changes by comparing their hashes.
    
    :param file_list: A list of files to monitor.
    :param interval: Time interval (in seconds) between file checks.
    """
    file_hashes = {file: hash_file(file) for file in file_list}

    while True:
        time.sleep(interval)
        for file in file_list:
            new_hash = hash_file(file)
            if new_hash is None:
                continue
            if file_hashes[file] != new_hash:
                print(f"Warning: File '{file}' has been modified!")

