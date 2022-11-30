import os
def getfileSize(filename):
    return os.stat(filename).st_size

filename=input('enter a file name-:')
size = getfileSize(filename)
print('filesize=',size)

print("the current working directory :", os.getcwd())

