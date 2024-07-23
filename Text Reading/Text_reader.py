import pyttsx3
import os
import sys

path = str(input("Enter the Path of File : "))
if path.endswith('.txt'):
    with open(path) as file:
        file_text=file.readlines()
        engine = pyttsx3.init()
        for i in file_text:
            engine.say(i)
            engine.runAndWait()
else:
    print("Not Correct Extantion try (.txt)")
