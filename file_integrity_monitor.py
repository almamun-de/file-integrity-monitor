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


