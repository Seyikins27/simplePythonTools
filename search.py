import os
from difflib import SequenceMatcher

def is_directory(directory):
    if os.path.isdir(directory):
        return True
    print ('Enter a valid Directory')
    exit()

def similar(string, file):
    return SequenceMatcher(None,string,file).ratio()

def main():
    print('___ This is a simple file search tool in Python ___')
    directory=input('Enter The Directory you want to search through: ')
    is_directory(directory)
    string=input('Enter you search query')
    similar_files=[]
    for r,d,f in os.walk(directory):
        for file in f:
            if similar(string,file)>=0.5:
                similar_files.append(file)

    print(similar_files)

if __name__=="__main__":
    main()
