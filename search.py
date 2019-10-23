import os
from difflib import SequenceMatcher

#checks if directory is a valid directory
def is_directory(directory):
    if os.path.isdir(directory):
        return True
    print ('Enter a valid Directory')
    exit()

#computes similarity between strings
def similar(string, file):
    return SequenceMatcher(None,string,file).ratio()

def list_items(list):
    for item in list:
        print(item)

#defines the level of string matches
def search_level(level):
    if level=='h' or level=='H':
        return 0.8
    elif level=='m' or level=='M':
        return 0.5
    elif level=='l' or level=='L':
        return 0.2
    else:
        return 0.5

#main function
def main():
    print('___ This is a simple file search tool in Python ___')
    directory=input('Enter The Directory you want to search through: ')
    is_directory(directory)
    string=input('Enter you search query')
    level=input('Specify string match level: L for Low, M for Medium, H for High')
    similar_files=[]
    for r,d,f in os.walk(directory):
        for file in f:
            if similar(string,file)>=search_level(level):
                similar_files.append(os.path.join(r,file))
    print(len(similar_files)," results found")
    list_items(similar_files)

if __name__=="__main__":
    main()
