import os

def list_directory_contents(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    list_directory_contents(directory_path)

import os

def report_file_sizes(directory):
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f"{entry.name}: {os.path.getsize(entry.path)} bytes")
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    report_file_sizes(directory_path)

import os
from collections import defaultdict

def count_file_extensions(directory):
    extension_count = defaultdict(int)
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    _, ext = os.path.splitext(entry.name)
                    ext = ext.lower()  # Normalize extension to lower case
                    extension_count[ext] += 1
        for ext, count in extension_count.items():
            print(f"{ext.upper()}: {count}")
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    count_file_extensions(directory_path)
