import os

def remove_empty_d(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
                print(f"{folder} is empty so will removed .")

path = str(input("Enter Path Of Folders : "))
remove_empty_d(path)
