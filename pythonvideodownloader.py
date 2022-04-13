import imp
from multiprocessing.connection import wait
import os
from pytube import Playlist, YouTube
import time

 

def downloadplaylist():
    link = input("Enter link: ")
    try :
        count = 0
        p = Playlist(link)
        print("\nFetching Details ...")
        print("-----------------------------------\n")
        
        # making a new folder with the title name
        
        directory = p.title
        parent_dir = "/Users/aniketgupta/Downloads"
        # add your own path here ⬆️
        # Path
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)

        for url in p.video_urls:
            count = count+1
            vid = YouTube(url)
            vid = vid.streams.get_highest_resolution()
            print("Downloading .. ", count," : ",  YouTube(url).title)
            vid.download(path)
            print("Download Complete !")
            wait(key)
            print("\n")

        return 0

    except:
        print("\n\nAn Error occured while connecting whith YouTube Servers", end="")
        for i in range (0, 5):
            time.sleep(1)
            print(". ", end="")

def download():
    link = input("Enter link: ")
    try:
        vid = YouTube(link)
        print("Video Title : ", vid.title)
        ch = input("Do you wish to continue ? : y/n\n")
        if(ch == 'y'):
            vid = vid.streams.get_highest_resolution()
            print("Downloading ", vid.title)
            vid.download("/Users/aniketgupta/Downloads") 
            # add your own path here ⬆️
            print("Download Complete !")
            return 0

        else:
            return 0

    except:
        print("\n\nAn Error occured while connecting whith YouTube Servers", end="")
        for i in range (0, 3):
            time.sleep(1)
            print(". ", end="")

# driver code:
choice = int(input('''
Do you want to download a video or a playlist:
* the videos will be downloaded in highest possible resolution
    Enter :
        1. For playlist
        2. For single video
        0. To exit\n'''))

if choice == 1:
    downloadplaylist()
elif choice == 2:
    download()
else:
    exit
    