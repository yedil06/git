import os
import shutil

# 1
def list_directories_files(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)
    
    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)
    
    print("\nAll Directories and Files:")
    for entry in os.listdir(path):
        print(entry)

# 2
def check_path_access(path):
    print(f"Path exists: {os.path.exists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")

# 3
def check_path_and_split(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

# 4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines in '{file_path}': {len(lines)}")

# 5
def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")
    print(f"List written to '{file_path}'.")

# 6
def generate_text_files():
    for letter in range(ord('A'), ord('Z') + 1):
        file_name = f"{chr(letter)}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is file {chr(letter)}.txt")
    print("26 text files generated from A.txt to Z.txt.")

# 7
def copy_file(source, destination):
    shutil.copy(source, destination)
    print(f"Contents of '{source}' copied to '{destination}'.")

# 8
def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(f"File '{file_path}' deleted.")
        else:
            print(f"No write access to '{file_path}'.")
    else:
        print(f"File '{file_path}' does not exist.")

# Main program
if __name__ == "__main__":
    path = input("Enter a directory path: ")
    
    # 1
    print("\nListing directories and files:")
    list_directories_files(path)
    
    # 2
    print("\nChecking path access:")
    check_path_access(path)
    
    # 3
    print("\nChecking path existence and splitting:")
    check_path_and_split(path)
    
    # 4
    file_path = input("\nEnter a file path to count lines: ")
    count_lines(file_path)
    
    # 5
    data = ["Apple", "Banana", "Cherry", "Date"]
    list_file_path = input("\nEnter a file path to write a list: ")
    write_list_to_file(list_file_path, data)
    
    # 6
    print("\nGenerating 26 text files:")
    generate_text_files()
    
    # 7
    source_file = input("\nEnter the source file path to copy: ")
    destination_file = input("Enter the destination file path: ")
    copy_file(source_file, destination_file)
    
    # 8
    file_to_delete = input("\nEnter the file path to delete: ")
    delete_file(file_to_delete)