import os
from shutil import move

def manage_files(path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            extensions = filename.split('.')[-1]
            destinations = os.path.join(path, extensions)
            if not os.path.exists(destinations):
                os.makedirs(destinations)
            move(os.path.join(path, filename), os.path.join(destinations,filename))

path = str(input("Enter path Directory : "))
manage_files(path)
print("your files managed by extension name .")
