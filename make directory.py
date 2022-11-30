'''Make a folder input given by the user'''
import os
path=input("enter a folder name-")
try:
    os.mkdir(path)
except OSError as error:
    print(error)
