import os
import re
import sys

def fix_non_ascii_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace non-ASCII characters
        fixed_content = re.sub(r'[^\x00-\x7F]+', '', content)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(fixed_content)
        
        print(f"Fixed: {file_path}")
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")

def fix_non_ascii_in_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            fix_non_ascii_in_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fix_non_ascii.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        if os.path.isdir(directory_path):
            fix_non_ascii_in_directory(directory_path)
        else:
            print(f"Invalid directory: {directory_path}")
