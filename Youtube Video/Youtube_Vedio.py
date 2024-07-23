from pytube import YouTube
import arabic_reshaper
from bidi.algorithm import get_display
import sys
import time

def print_loading_effect():
    chars = "/—\|"  # Characters for a circular loading animation
    for _ in range(20):
        for char in chars:
            sys.stdout.write('\r' + f'Downloading... {char}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r')
    sys.stdout.flush()

link = str(input("Enter Your Video Link: "))
yt = YouTube(link)
title = arabic_reshaper.reshape(yt.title)
print("Title: ", get_display(title))
print("Views: ", yt.views)

download = input("For Continue Press Y To Break Q: ")
if download.upper() == "Y":
    print_loading_effect()
    yt = yt.streams.get_highest_resolution()
    yt.download('/home/november/Downloads')
    print("\nDownload completed!")
else:
    print("Download process stopped.")

