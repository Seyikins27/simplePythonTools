import os
from difflib import SequenceMatcher

def is_directory(directory):
    if os.path.isdir(directory):
        return True
    print ('Not a Directory')
    exit()

def main():
    print('___ This is a simple file search tool in Python ___')
    directory=input('Enter The Directory you want to search through: ')
    is_directory(directory)
    string=input('Enter you search query')

    for r,d,f in os.walk(directory):
        for file in f:
            print(file)


    return 0

if __name__=="__main__":
    main()
