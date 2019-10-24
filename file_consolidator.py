import os
import hashlib

def is_directory(directory):
    if os.path.isdir(directory):
        return True
    print ('Enter a valid Directory')
    exit()

def file_size(file):
    return os.path.getsize(file)

def is_same_name(file1,file2):
    if file1==file2:
        return True
    return False

def get_file_checksum(file):
    filesum=hashlib.sha1()
    with open(file,'rb') as file:
        file_bits =0
        while file_bits != b'':
            file_bits= file.read(1024)
            filesum.update(file_bits)
    return filesum.hexdigest()

def check_item_exists(item, list):
    for items in list:
        if items==item:
            return True
    return False

def main():
    files=[]
    duplicates=[]
    directory=input('Input the directory that you want to scan')
    is_directory(directory)



if __name__=='__main__':
    main()