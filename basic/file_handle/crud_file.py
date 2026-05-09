from pathlib import Path
import os
import shutil


def create_folder():
    try:
        name = input("Please tell your folder name: ")
        if not name:
            print("Folder name not be empty")
        else:
            p = Path(name)
            p.mkdir()
            print(f"Folder created with `{name}` name")
    except Exception as err:
        print(f"Some error occured when folder created, {err}")

def read_file_folder():
    try:
        p = Path("")
        items = list(p.rglob("*"))
        for i, v in enumerate(items):
            print(f"{i+1} : {v}")
    except Exception as err:
        print(f"Some error occured when read file and folder, {err}")

def update_folder_name():
    try:
        read_file_folder()
        name = input("\nWhich one folder name you want to update: ")
        p = Path(name)
        if p.exists() and p.is_dir():
            new_name = input("Enter new name for folder: ")
            if not new_name:
                print("Folder name cannot be empty")
            else:
                new_dir = Path(new_name)
                p.rename(new_dir)
                print(f"New folder name `{new_name}` update successfully")
        else:
            print(f"{name} this name folder does not exists")
    except Exception as err:
        print(f"Some error occured when folder name update, {err}")

def delete_folder_name():
    try:
        read_file_folder()
        name = input("\nEnter folder name, you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)
            print(f"`{name}` folder delete successfully")
        else: 
            print(f"{name}, this name folder not exist")
    except Exception as err:
        print(f"Some error occured when delete folder, {err}")

def create_file():
    try:
        name = input("Enter your file name: ")
        if not name:
            print("File name cannot be empty")
        else:
            p = Path(name)
            if p.exists() and p.is_file():
                print("Sorry, this file name alredy exist")
            else:
                with open(name, 'w') as fs:
                    data = input("Write data you want to add your file: ")
                    fs.write(data)
                print("File created successfully")
    except Exception as err:
        print(f"Some error occured when create a file, {err}")

def read_file():
    try:
        read_file_folder()
        name = input("Which one file you want to read: ")
        if not name:
            print("File name cannot be empty")
        else:
            p = Path(name)
            if p.exists() and p.is_file():
                with open(name, 'r') as fs:
                    print(fs.read())
            else:
                print("Sorry, this file name not exist")
    except Exception as err:
        print(f"Some error occured when read a file, {err}")

def update_file():
    try:
        read_file_folder()
        name = input("Tell your file name: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Options")
            print("1. For remaining the file")
            print("2. For append data in a file")
            print("3. For overwrite data in a file")
            choice = int(input("Which one operation you perform on the file: "))
            
            if choice == 1:
                new_name = input("Enter new file name with extension: ").strip()
                new_p = Path(new_name)
                if new_p.exists() and new_p.is_file():
                    print(f"{new_name} this file name already exist")
                else:
                    p.rename(new_p)
                    print("File name is changed successfully")
            elif choice == 2:
                data = input("Write your data for appending: ")
                with open(name, 'a') as fs:
                    fs.write(f"\n{data}")
            elif choice == 3:
                data = input("Write your data for overwrite: ")
                with open(name, 'w') as fs:
                    fs.write(f"\n{data}")
            else:
                print("You choose wrong input.")
    except Exception as err:
        print(f"Some error occure, when file is updated: {err}")

def delete_file():
    try:
        read_file_folder()
        name = input("Which one file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("File delete successfully")
        else:
            print("File not found")

    except Exception as err:
        print(f"Some error occure with {err}")

while True: 
    print("1. Create a folder")
    print("2. Read file and folder")
    print("3. Update the folder name")
    print("4. Delete the folder")
    print("5. Create a file")
    print("6. Read a file")
    print("7. Update a file")
    print("8. Delete a file")
    print("0. For exist")

    choice = int(input("Choose your option: "))

    if choice == 1:
        create_folder()

    if choice == 2:
        read_file_folder()

    if choice == 3:
        update_folder_name()

    if choice == 4:
        delete_folder_name()

    if choice == 5:
        create_file()

    if choice == 6:
        read_file()

    if choice == 7:
        update_file()

    if choice == 8:
        delete_file()
    
    if choice == 0:
        break




